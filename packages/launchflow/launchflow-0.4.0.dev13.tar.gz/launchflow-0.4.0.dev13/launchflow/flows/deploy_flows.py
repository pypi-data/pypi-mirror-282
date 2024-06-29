import asyncio
import dataclasses
import datetime
import io
import logging
import time
from typing import List, Literal, Optional, Tuple, Union

import rich
from rich.console import Console
from rich.live import Live
from rich.padding import Padding
from rich.style import Style
from rich.table import Table
from rich.tree import Tree

import launchflow
from launchflow import exceptions
from launchflow.clients.docker_client import docker_service_available
from launchflow.config import config
from launchflow.flows.create_flows import (
    CreateResourcePlan,
    CreateResourceResult,
    CreateServicePlan,
    CreateServiceResult,
    plan_create,
    plan_create_service,
)
from launchflow.flows.flow_utils import (
    OP_COLOR,
    EnvironmentRef,
    ServiceRef,
    format_configuration_dict,
)
from launchflow.flows.plan import FailedToPlan, Plan, Result, ServicePlan, execute_plans
from launchflow.flows.plan_utils import lock_plans, print_plans, select_plans
from launchflow.gcp.cloud_run import CloudRun
from launchflow.gcp.service import GCPService
from launchflow.locks import Lock, LockOperation, OperationType, ReleaseReason
from launchflow.managers.environment_manager import EnvironmentManager
from launchflow.managers.service_manager import ServiceManager
from launchflow.models.enums import CloudProvider, ServiceStatus
from launchflow.models.flow_state import (
    EnvironmentState,
    GCPEnvironmentConfig,
    ServiceState,
)
from launchflow.node import Node
from launchflow.resource import Resource
from launchflow.service import Service
from launchflow.validation import validate_service_name
from launchflow.workflows.deploy_gcp_service.deploy_gcp_service_utils import (
    build_and_push_gcp_service,
    release_docker_image_to_cloud_run,
)


@dataclasses.dataclass
class BuildServiceResult(Result["BuildServicePlan"]):
    docker_image: Optional[str] = None
    logs_file_or_link: Optional[str] = None


@dataclasses.dataclass
class BuildServicePlan(ServicePlan):
    service_manager: ServiceManager
    gcp_environment_config: GCPEnvironmentConfig
    deployment_id: str
    build_local: bool = False

    @property
    def operation_type(self) -> Literal["build"]:
        return "build"

    async def abandon_plan(self, reason: str):
        result = BuildServiceResult(plan=self, success=False)
        result.error_message = f"Build abandoned: {reason}"
        return result

    async def execute_plan(
        self,
        tree: Tree,
        dependency_results: List[Result],
    ) -> BuildServiceResult:
        try:
            logs_file_or_link = None
            if isinstance(self.service, GCPService):
                docker_image, logs_file_or_link = await build_and_push_gcp_service(
                    self.service,
                    self.service_manager,
                    self.gcp_environment_config,
                    self.deployment_id,
                    self.build_local,
                )
                return BuildServiceResult(self, True, docker_image, logs_file_or_link)
            else:
                # TODO: Add AWS support
                return BuildServiceResult(self, False)
        except Exception as e:
            # TODO: Improve this error handling
            logging.error("Exception occurred: %s", e, exc_info=True)
            result = BuildServiceResult(self, False)
            result.error_message = str(e)
            return result

    def print_plan(
        self,
        console: rich.console.Console = rich.console.Console(),
        left_padding: int = 0,
    ):
        left_padding_str = " " * left_padding
        build_inputs_dict = {
            "dockerfile": self.service.dockerfile,
            "build_directory": self.service.build_directory,
            "build_ignore": self.service.build_ignore,
            "build_local": self.build_local,
        }
        build_inputs_str = format_configuration_dict(build_inputs_dict)
        console.print()
        console.print(
            f"{left_padding_str}1. {ServiceRef(self.service)} will be [{OP_COLOR}]built[/{OP_COLOR}] with the following configuration:"
        )
        console.print(
            left_padding_str
            + "    "
            + f"\n{left_padding_str}    ".join(build_inputs_str.split("\n"))
        )

    async def lock_plan(self) -> None:
        return None

    def pending_message(self):
        return f"Build {ServiceRef(self.service)} waiting for create step to finish..."

    def task_description(self):
        return f"Building {ServiceRef(self.service)}..."

    def success_message(self):
        return f"Successfully built {ServiceRef(self.service)}"

    def failure_message(self):
        return f"Failed to build {ServiceRef(self.service)}"


@dataclasses.dataclass
class ReleaseServiceResult(Result["ReleaseServicePlan"]):
    service_url: Optional[str] = None


@dataclasses.dataclass
class ReleaseServicePlan(ServicePlan):
    environment_ref: EnvironmentRef
    gcp_environment_config: GCPEnvironmentConfig

    @property
    def operation_type(self) -> Literal["release"]:
        return "release"

    async def abandon_plan(self, reason: str):
        result = ReleaseServiceResult(plan=self, success=False)
        result.error_message = f"Release abandoned: {reason}"
        return result

    async def execute_plan(
        self,
        tree: Tree,
        dependency_results: List[Result],
    ) -> ReleaseServiceResult:
        build_result = next(
            (
                result
                for result in dependency_results
                if isinstance(result, BuildServiceResult)
            ),
            None,
        )
        if build_result is None:
            result = ReleaseServiceResult(self, False)
            result.error_message = "Could not find a build result to release"
            return result

        if isinstance(self.service, CloudRun):
            service_url = await release_docker_image_to_cloud_run(
                docker_image=build_result.docker_image,
                gcp_project_id=self.gcp_environment_config.project_id,
                gcp_region=self.gcp_environment_config.default_region,
                cloud_run_service=self.service,
            )
        else:
            # TODO: Add AWS support
            return ReleaseServiceResult(self, False)
        return ReleaseServiceResult(self, True, service_url)

    def print_plan(
        self,
        console: rich.console.Console = rich.console.Console(),
        left_padding: int = 0,
    ):
        left_padding_str = " " * left_padding
        console.print(
            f"{left_padding_str}2. {ServiceRef(self.service)} will be [{OP_COLOR}]released[/{OP_COLOR}] to {self.environment_ref}"
        )
        console.print()

    async def lock_plan(self) -> None:
        return None

    def pending_message(self):
        return f"Release {ServiceRef(self.service)} waiting for build step to finish..."

    def task_description(self):
        return f"Releasing {ServiceRef(self.service)}..."

    def success_message(self):
        return f"Successfully released {ServiceRef(self.service)}"

    def failure_message(self):
        return f"Failed to release {ServiceRef(self.service)}"


@dataclasses.dataclass
class DeployServiceResult(Result["DeployServicePlan"]):
    service_state: Optional[ServiceState]
    build_result: BuildServiceResult
    release_result: ReleaseServiceResult


@dataclasses.dataclass
class DeployServicePlan(ServicePlan):
    service_manager: ServiceManager
    existing_service_state: Optional[ServiceState]
    build_service_plan: BuildServicePlan
    release_service_plan: ReleaseServicePlan
    _lock: Optional[Lock] = None

    def child_plans(self) -> List[Plan]:
        return [
            self.build_service_plan,
            self.release_service_plan,
        ]

    @property
    def operation_type(self) -> Literal["deploy"]:
        return "deploy"

    async def abandon_plan(self, reason: str):
        if self._lock is not None:
            await self._lock.release(ReleaseReason.ABANDONED)

        abandon_tasks = [
            self.build_service_plan.abandon_plan(reason),
            self.release_service_plan.abandon_plan(reason),
        ]
        build_service_result, release_service_result = await asyncio.gather(
            *abandon_tasks
        )

        result = DeployServiceResult(
            self,
            False,
            None,
            build_service_result,
            release_service_result,
        )
        result.error_message = f"Deploy abandoned: {reason}"
        return result

    async def execute_plan(
        self,
        tree: Tree,
        dependency_results: List[Result],
    ) -> DeployServiceResult:
        if self._lock is None:
            return await self.abandon_plan("Plan was not locked before execution.")
        try:
            self.service.outputs()
        except exceptions.ServiceOutputsNotFound:
            return await self.abandon_plan(
                "Service outputs not found. This usually means the service was not created successfully."
            )

        async with self._lock as lock_info:
            updated_time = datetime.datetime.now(datetime.timezone.utc)
            if self.existing_service_state:
                created_time = self.existing_service_state.created_at
                inputs = self.existing_service_state.inputs or {}
            else:
                created_time = updated_time
                # NOTE: We dont save the inputs until the deploy is successful
                inputs = {}

            new_service_state = ServiceState(
                name=self.service.name,
                product=self.service.product,
                cloud_provider=self.service.product.cloud_provider(),
                created_at=created_time,
                updated_at=updated_time,
                status=ServiceStatus.DEPLOYING,
                inputs=inputs,
            )

            # Handle all exceptions to ensure we commit the service state properly
            try:
                # Save intermediate service state to push status to the backend
                await self.service_manager.save_service(
                    new_service_state, lock_info.lock_id
                )

                # NOTE: Plans are returned in the same order as they are passed in
                results = await execute_plans(
                    [
                        self.build_service_plan,
                        self.release_service_plan,
                    ],
                    tree,
                )

                build_service_result, release_service_result = results

                # We do this for type hinting purposes
                build_service_result: BuildServiceResult = build_service_result
                release_service_result: ReleaseServiceResult = release_service_result
                deploy_successful = all(result.success for result in results)

                new_service_state.docker_image = build_service_result.docker_image
                new_service_state.service_url = release_service_result.service_url
                if deploy_successful:
                    new_service_state.status = ServiceStatus.READY
                    # NOTE: We dont save the inputs until the deploy is successful
                    new_service_state.inputs = self.service.inputs()
                else:
                    new_service_state.status = ServiceStatus.DEPLOY_FAILED

                await self.service_manager.save_service(
                    new_service_state, lock_info.lock_id
                )

                return DeployServiceResult(
                    self,
                    deploy_successful,
                    new_service_state,
                    build_service_result,
                    release_service_result,
                )
            except Exception as e:
                logging.error(
                    "Exception occurred while deploying service %s: %s",
                    self.service.name,
                    e,
                    exc_info=True,
                )
                # If an exception occurs we save the service state with a failed status
                new_service_state.status = ServiceStatus.DEPLOY_FAILED
                await self.service_manager.save_service(
                    new_service_state, lock_info.lock_id
                )
                build_service_result = await self.build_service_plan.abandon_plan(
                    "Unknown error occurred while deploying service"
                )
                release_service_result = await self.release_service_plan.abandon_plan(
                    "Unknown error occurred while deploying service"
                )
                result = DeployServiceResult(
                    self,
                    False,
                    new_service_state,
                    build_service_result,
                    release_service_result,
                )
                result.error_message = str(e)
                return result

    def print_plan(
        self,
        console: rich.console.Console = rich.console.Console(),
        left_padding: int = 0,
    ):
        left_padding_str = " " * left_padding
        console.print(
            f"{left_padding_str}{ServiceRef(self.service)} will be [{OP_COLOR}]deployed[/{OP_COLOR}] with the following workflow:"
        )
        self.build_service_plan.print_plan(console, left_padding=left_padding + 4)
        self.release_service_plan.print_plan(console, left_padding=left_padding + 4)

    def task_description(self):
        return f"Deploying {ServiceRef(self.service)}..."

    def success_message(self):
        return f"Successfully deployed {ServiceRef(self.service)}"

    def failure_message(self):
        return f"Failed to deploy {ServiceRef(self.service)}"

    def pending_message(self):
        return f"Deploy {ServiceRef(self.service)} waiting for create operations to finish..."

    async def lock_plan(self) -> Lock:
        if self._lock is not None:
            raise exceptions.PlanAlreadyLocked(self)

        op_type = OperationType.DEPLOY_SERVICE
        plan_output = io.StringIO()
        console = Console(no_color=True, file=plan_output)
        self.print_plan(console)
        plan_output.seek(0)

        lock = await self.service_manager.lock_service(
            operation=LockOperation(
                operation_type=op_type, metadata={"plan": plan_output.read()}
            ),
        )

        try:
            refreshed_service_state = await self.service_manager.load_service()
        except exceptions.ServiceNotFound:
            refreshed_service_state = None

        # NOTE: The refreshed service state will usually be different since create ops
        # will have just executed. We only check if deploy-related fields have changed.
        def _service_state_differs(
            a: Optional[ServiceState], b: Optional[ServiceState]
        ) -> bool:
            # TODO: think through the edge cases here with null states.
            # Maybe we should throw an error if the service state is not Ready?
            if a is None or b is None:
                return False
            return (
                a.product != b.product
                or a.service_url != b.service_url
                or a.docker_image != b.docker_image
            )

        if _service_state_differs(self.existing_service_state, refreshed_service_state):
            # If the service has changed since planning we release the lock and will not
            # attempt to execute the plan
            await lock.release(reason=ReleaseReason.ABANDONED)
            raise exceptions.ServiceStateMismatch(self.service)

        self._lock = lock
        return lock


async def plan_deploy_service(
    service: Service,
    environment: EnvironmentState,
    environment_manager: EnvironmentManager,
    verbose: bool,
    build_local: bool,
) -> Union[DeployServicePlan, FailedToPlan]:
    try:
        validate_service_name(service.name)
    except ValueError as e:
        return FailedToPlan(
            service=service,
            error_message=str(e),
        )

    if service.product.cloud_provider() == CloudProvider.GCP:
        if environment.gcp_config is None:
            return FailedToPlan(
                service=service,
                error_message="CloudProviderMismatch: Cannot use a GCP Service in an AWS Environment.",
            )
    elif service.product.cloud_provider() == CloudProvider.AWS:
        if environment.aws_config is None:
            return FailedToPlan(
                service=service,
                error_message="CloudProviderMismatch: Cannot use an AWS Service in a GCP Environment.",
            )

    service_manager = environment_manager.create_service_manager(service.name)
    try:
        existing_service = await service_manager.load_service()
    except exceptions.ServiceNotFound:
        existing_service = None

    if existing_service is not None and existing_service.product != service.product:
        exception = exceptions.ServiceProductMismatch(
            existing_product=existing_service.product.name,
            new_product=service.product,
        )
        return FailedToPlan(
            service=service,
            error_message=str(exception),
        )

    # TODO: Rethink how we generate deployment ids
    deployment_id = str(int(time.time()))

    # Plan the build for the service
    build_plan = BuildServicePlan(
        resource_or_service=service,
        service_manager=service_manager,
        gcp_environment_config=environment.gcp_config,
        deployment_id=deployment_id,
        depends_on=[],
        verbose=verbose,
        build_local=build_local,
    )

    # Plan the release for the service
    release_plan = ReleaseServicePlan(
        resource_or_service=service,
        depends_on=[build_plan],
        verbose=verbose,
        environment_ref=EnvironmentRef(environment_manager),
        gcp_environment_config=environment.gcp_config,
    )

    return DeployServicePlan(
        resource_or_service=service,
        service_manager=service_manager,
        existing_service_state=existing_service,
        build_service_plan=build_plan,
        release_service_plan=release_plan,
        depends_on=[],
        verbose=verbose,
    )


async def plan_deploy(
    *nodes: Node,
    environment: EnvironmentState,
    environment_manager: EnvironmentManager,
    verbose: bool,
    build_local: bool,
    skip_create: bool,
) -> List[
    Union[CreateResourcePlan, CreateServicePlan, DeployServicePlan, FailedToPlan]
]:
    resource_nodes: List[Resource] = []
    service_nodes: List[Service] = []
    for node in nodes:
        if isinstance(node, Resource):
            resource_nodes.append(node)
        elif isinstance(node, Service):
            service_nodes.append(node)
        else:
            raise ValueError(f"Unknown node type {node}")

    create_plans = []
    if not skip_create:
        create_plans = await plan_create(
            *resource_nodes,
            *service_nodes,
            environment=environment,
            environment_manager=environment_manager,
            verbose=verbose,
        )

    deploy_service_plans = await asyncio.gather(
        *[
            plan_deploy_service(
                service=service,
                environment=environment,
                environment_manager=environment_manager,
                verbose=verbose,
                build_local=build_local,
            )
            for service in service_nodes
        ]
    )
    # We need to check if the skip create flag will cause the deploy to fail.
    # If so, we swap it for a FailedToPlan.
    if skip_create:
        keyed_deploy_service_plans = {
            plan.service.name: plan for plan in deploy_service_plans
        }
        create_service_plans = await asyncio.gather(
            *[
                plan_create_service(
                    service=service,
                    environment=environment,
                    environment_manager=environment_manager,
                    verbose=verbose,
                )
                for service in service_nodes
            ]
        )
        for plan in create_service_plans:
            if isinstance(plan, FailedToPlan) or plan.operation_type != "noop":
                keyed_deploy_service_plans[plan.service.name] = FailedToPlan(
                    service=plan.service,
                    error_message="Cannot deploy service without creating it. Try again without the --skip-create flag.",
                )
        deploy_service_plans = list(keyed_deploy_service_plans.values())

    return create_plans + deploy_service_plans


async def deploy(
    *nodes: Tuple[Node],
    environment_name: Optional[str] = None,
    prompt: bool = True,
    verbose: bool = False,
    build_local: bool = False,
    skip_create: bool = False,
    console: Console = Console(),
):
    """
    Create resources and deploy services in an environment.

    Args:
    - `nodes`: A tuple of Resources and Services to create.
    - `environment_name`: The name of the environment to create resources in. Defaults
        to the env configured in the launchflow.yaml.
    - `prompt`: Whether to prompt the user before creating resources.
    - `verbose`: If true all logs will be written to stdout.
    """
    if not nodes:
        if skip_create:
            console.print("No services to deploy. Exiting.")
        else:
            console.print("No resources to create or services to deploy. Exiting.")
        return True

    if build_local and not docker_service_available():
        console.print(
            "Docker must be installed to use the --build-local flag. Exiting."
        )
        return False

    if launchflow.project is None:
        console.print("Could not determine the project. Exiting.")
        return False

    environment_manager = EnvironmentManager(
        project_name=launchflow.project,
        environment_name=environment_name,
        backend=config.launchflow_yaml.backend,
    )
    environment = await environment_manager.load_environment()

    # Step 1: Build the plans
    plans = await plan_deploy(
        *nodes,
        environment=environment,
        environment_manager=environment_manager,
        verbose=verbose,
        build_local=build_local,
        skip_create=skip_create,
    )

    # NOTE: These lists won't contain the failed plans
    create_plans: List[Union[CreateResourcePlan, CreateServicePlan]] = []
    deploy_service_plans: List[DeployServicePlan] = []
    failed_plans: List[FailedToPlan] = []
    for plan in plans:
        if isinstance(plan, CreateResourcePlan) or isinstance(plan, CreateServicePlan):
            create_plans.append(plan)
        elif isinstance(plan, DeployServicePlan):
            deploy_service_plans.append(plan)
        elif isinstance(plan, FailedToPlan):
            failed_plans.append(plan)

    # TODO: Do a stumble to determine if we should prompt the create + deploy plans
    # together or separately. Separately has less gotchas, but feels a bit clunky.
    # Step 2: Select the plans
    print_plans(
        *plans,
        environment_manager=environment_manager,
        console=console,
    )
    service_names_that_need_create = set(
        [
            plan.service.name
            for plan in create_plans + failed_plans
            if (isinstance(plan, CreateServicePlan) and plan.operation_type != "noop")
            or (isinstance(plan, FailedToPlan) and plan.service is not None)
        ]
    )
    selected_create_plans: Union[
        None, List[Union[CreateResourcePlan, CreateServicePlan]]
    ] = await select_plans(
        *create_plans,
        operation_type="create",
        environment_manager=environment_manager,
        console=console,
        confirm=prompt,
    )
    selected_create_service_names = set(
        [
            plan.service.name
            for plan in selected_create_plans
            if isinstance(plan, CreateServicePlan)
        ]
    )
    serivce_names_that_will_fail_to_deploy = (
        service_names_that_need_create - selected_create_service_names
    )
    if serivce_names_that_will_fail_to_deploy:
        removed_deploy_plans: List[DeployServicePlan] = []
        new_deploy_service_plans: List[DeployServicePlan] = []
        for plan in deploy_service_plans:
            if plan.service.name in serivce_names_that_will_fail_to_deploy:
                removed_deploy_plans.append(plan)
            else:
                new_deploy_service_plans.append(plan)
        deploy_service_plans = new_deploy_service_plans

        console.print(
            "[yellow]The following services need to be created before they can be deployed:[/yellow]"
        )
        for plan in removed_deploy_plans:
            console.print(f"  - {ServiceRef(plan.service)}")
        console.print()

    selected_deploy_plans: Union[None, List[DeployServicePlan]] = await select_plans(
        *deploy_service_plans,
        operation_type="deploy",
        environment_manager=environment_manager,
        console=console,
        confirm=prompt,
    )

    # The None is a special case for no valid plans
    if selected_create_plans is None and selected_deploy_plans is None:
        if skip_create:
            console.print("No services to deploy. Exiting.")
        else:
            console.print("Nothing to create or deploy. Exiting.")
        return False

    # The empty list case means the user did not confirm any plans
    # We only check the deploy plans
    if not selected_deploy_plans:
        console.print("No deploy plans selected. Exiting.")
        return True

    if selected_create_plans is None:
        selected_create_plans = []
    if selected_deploy_plans is None:
        selected_deploy_plans = []

    # Step 3: Lock the plans
    # TODO: Determine if we should check if the Environment state has changed since planning
    if selected_create_plans:
        async with lock_plans(
            *selected_create_plans, environment_manager=environment_manager
        ):
            # Step 4: Execute the plans
            console.rule("[bold purple]create operations")

            tree = Tree(
                "Plans",
                guide_style=Style(dim=True),
                hide_root=True,
            )
            with Live(
                Padding(tree, (1, 0, 1, 0)), console=console, refresh_per_second=8
            ):
                create_results: List[
                    Union[CreateResourceResult, CreateServiceResult]
                ] = await execute_plans(selected_create_plans, tree)
    else:
        create_results = []

    create_has_failures = any(not result.success for result in create_results)
    if create_has_failures:
        console.rule("[bold purple]deploy operations")
        console.print(
            "\n[yellow]Skipping deploy operations due to create failures[/yellow]\n"
        )
        deploy_results = []
    else:
        async with lock_plans(
            *selected_deploy_plans, environment_manager=environment_manager
        ):
            # Step 4: Execute the plans
            console.rule("[bold purple]deploy operations")

            tree = Tree(
                "Plans",
                guide_style=Style(dim=True),
                hide_root=True,
            )
            with Live(
                Padding(tree, (1, 0, 1, 0)), console=console, refresh_per_second=8
            ):
                deploy_results: List[DeployServiceResult] = await execute_plans(
                    selected_deploy_plans, tree
                )

    # Step 5: Print the results

    # Step 5.1: Print the logs
    table = Table(show_header=True, show_edge=False, show_lines=False, box=None)
    table.add_column("Operation", justify="left", no_wrap=True)
    table.add_column("Logs", style="blue")
    # Add the logs for the create resource results
    if create_results:
        for result in create_results:
            if isinstance(result, CreateResourceResult):
                if result.logs_file is None:
                    continue

                if result.success:
                    table.add_row(
                        f"[green]✓[/green] {result.plan.operation_type.title()} {result.plan.reference()}",
                        result.logs_file,
                    )
                else:
                    table.add_row(
                        f"[red]✗[/red] {result.plan.operation_type.title()} {result.plan.reference()}",
                        result.logs_file,
                    )
            elif isinstance(result, CreateServiceResult):
                for resource_result in result.create_resource_results:
                    if resource_result.logs_file is None:
                        continue

                    if resource_result.success:
                        table.add_row(
                            f"[green]✓[/green] {resource_result.plan.operation_type.title()} {resource_result.plan.reference()}",
                            resource_result.logs_file,
                        )
                    else:
                        table.add_row(
                            f"[red]✗[/red] {resource_result.plan.operation_type.title()} {resource_result.plan.reference()}",
                            resource_result.logs_file,
                        )
    # Add the logs for the deploy service results
    if deploy_results:
        for result in deploy_results:
            # Logs for service build step
            if result.build_result is not None:
                if result.build_result.logs_file_or_link is None:
                    continue

                if result.success:
                    table.add_row(
                        f"[green]✓[/green] {result.plan.build_service_plan.operation_type.title()} {result.plan.build_service_plan.reference()}",
                        result.build_result.logs_file_or_link,
                    )
                else:
                    table.add_row(
                        f"[red]✗[/red] {result.plan.build_service_plan.operation_type.title()} {result.plan.build_service_plan.reference()}",
                        result.build_result.logs_file_or_link,
                    )

    # We only print the logs table if there are logs to show
    if table.row_count > 0:
        console.rule("[bold purple]logs")
        console.print()
        console.print(table)
        console.print()

    # Step 5.2: Print the service urls
    table = Table(show_header=True, show_edge=False, show_lines=False, box=None)
    table.add_column("Service", justify="left", no_wrap=True)
    table.add_column("URL", style="blue")
    for result in deploy_results:
        # This is None when the plan was abandoned
        if (
            result.service_state is not None
            and result.service_state.service_url is not None
        ):
            table.add_row(
                str(ServiceRef(result.plan.service)),
                result.service_state.service_url,
            )

    # We only print the service urls table if there are urls to show
    if table.row_count > 0:
        console.rule("[bold purple]service urls")
        console.print()
        console.print(table)
        console.print()

    # Step 5.3: Print the dns settings
    # TODO: add dns settings section

    # Step 5.4: Print the secrets
    # TODO: add secrets section

    # Step 5.5: Print the results summary
    console.rule("[bold purple]summary")
    console.print()

    successful_resource_create_count = 0
    failed_resource_create_count = 0
    successful_resource_update_count = 0
    failed_resource_update_count = 0
    successful_resource_replace_count = 0
    failed_resource_replace_count = 0
    successful_service_create_count = 0
    failed_service_create_count = 0
    successful_service_update_count = 0
    failed_service_update_count = 0
    successful_service_deploy_count = 0
    failed_service_deploy_count = 0

    for result in create_results + deploy_results:
        if isinstance(result, CreateResourceResult):
            if result.success:
                if result.plan.operation_type == "create":
                    successful_resource_create_count += 1
                elif result.plan.operation_type == "update":
                    successful_resource_update_count += 1
                elif result.plan.operation_type == "replace":
                    successful_resource_replace_count += 1
            else:
                if result.plan.operation_type == "create":
                    failed_resource_create_count += 1
                elif result.plan.operation_type == "update":
                    failed_resource_update_count += 1
                elif result.plan.operation_type == "replace":
                    failed_resource_replace_count += 1

        if isinstance(result, CreateServiceResult):
            if result.success:
                successful_service_create_count += 1
            else:
                failed_service_create_count += 1
            for resource_result in result.create_resource_results:
                if resource_result.success:
                    if resource_result.plan.operation_type == "create":
                        successful_resource_create_count += 1
                    elif resource_result.plan.operation_type == "update":
                        successful_resource_update_count += 1
                    elif resource_result.plan.operation_type == "replace":
                        successful_resource_replace_count += 1
                else:
                    if resource_result.plan.operation_type == "create":
                        failed_resource_create_count += 1
                    elif resource_result.plan.operation_type == "update":
                        failed_resource_update_count += 1
                    elif resource_result.plan.operation_type == "replace":
                        failed_resource_replace_count += 1

        elif isinstance(result, DeployServiceResult):
            if result.success:
                successful_service_deploy_count += 1
            else:
                failed_service_deploy_count += 1

    if successful_resource_create_count or successful_service_create_count:
        if successful_service_create_count == 0:
            console.print(
                f"[green]Successfully created {successful_resource_create_count} {'resource' if successful_resource_create_count == 1 else 'resources'}[/green]"
            )
        elif successful_resource_create_count == 0:
            console.print(
                f"[green]Successfully created {successful_service_create_count} {'service' if successful_service_create_count == 1 else 'services'}[/green]"
            )
        else:
            console.print(
                f"[green]Successfully created {successful_resource_create_count} {'resource' if successful_resource_create_count == 1 else 'resources'} and {successful_service_create_count} {'service' if successful_service_create_count == 1 else 'services'}[/green]"
            )
    if failed_resource_create_count or failed_service_create_count:
        if failed_service_create_count == 0:
            console.print(
                f"[red]Failed to create {failed_resource_create_count} {'resource' if failed_resource_create_count == 1 else 'resources'}[/red]"
            )
        elif failed_resource_create_count == 0:
            console.print(
                f"[red]Failed to create {failed_service_create_count} {'service' if failed_service_create_count == 1 else 'services'}[/red]"
            )
        else:
            console.print(
                f"[red]Failed to create {failed_resource_create_count} {'resource' if failed_resource_create_count == 1 else 'resources'} and {failed_service_create_count} {'service' if failed_service_create_count == 1 else 'services'}[/red]"
            )
    if successful_resource_update_count or successful_service_update_count:
        if successful_service_update_count == 0:
            console.print(
                f"[green]Successfully updated {successful_resource_update_count} {'resource' if successful_resource_update_count == 1 else 'resources'}[/green]"
            )
        elif successful_resource_update_count == 0:
            console.print(
                f"[green]Successfully updated {successful_service_update_count} {'service' if successful_service_update_count == 1 else 'services'}[/green]"
            )
        else:
            console.print(
                f"[green]Successfully updated {successful_resource_update_count} {'resource' if successful_resource_update_count == 1 else 'resources'} and {successful_service_update_count} {'service' if successful_service_update_count == 1 else 'services'}[/green]"
            )
    if failed_resource_update_count or failed_service_update_count:
        if failed_service_update_count == 0:
            console.print(
                f"[red]Failed to update {failed_resource_update_count} {'resource' if failed_resource_update_count == 1 else 'resources'}[/red]"
            )
        elif failed_resource_update_count == 0:
            console.print(
                f"[red]Failed to update {failed_service_update_count} {'service' if failed_service_update_count == 1 else 'services'}[/red]"
            )
        else:
            console.print(
                f"[red]Failed to update {failed_resource_update_count} {'resource' if failed_resource_update_count == 1 else 'resources'} and {failed_service_update_count} {'service' if failed_service_update_count == 1 else 'services'}[/red]"
            )
    if successful_resource_replace_count:
        console.print(
            f"[green]Successfully replaced {successful_resource_replace_count} {'resource' if successful_resource_replace_count == 1 else 'resources'}[/green]"
        )
    if failed_resource_replace_count:
        console.print(
            f"[red]Failed to replace {failed_resource_replace_count} {'resource' if failed_resource_replace_count == 1 else 'resources'}[/red]"
        )
    if successful_service_deploy_count:
        console.print(
            f"[green]Successfully deployed {successful_service_deploy_count} {'service' if successful_service_deploy_count == 1 else 'services'}[/green]"
        )
    if failed_service_deploy_count:
        console.print(
            f"[red]Failed to deploy {failed_service_deploy_count} {'service' if failed_service_deploy_count == 1 else 'services'}[/red]"
        )

    if create_has_failures:
        num_deployments_skipped = len(selected_deploy_plans)
        console.print(
            f"[yellow]Skipped {num_deployments_skipped} {'deployment' if num_deployments_skipped == 1 else 'deployments'} due to create failures[/yellow]"
        )

    console.print()
    # Returns true if the command succeeded
    return (
        not failed_resource_create_count
        and not failed_resource_update_count
        and not failed_resource_replace_count
        and not failed_service_create_count
        and not failed_service_update_count
        and not failed_service_deploy_count
        and not create_has_failures
    )
