import asyncio
import os
import time
from typing import List, Tuple

from docker.errors import BuildError

from launchflow import exceptions
from launchflow.config import config
from launchflow.flows.flow_logger import WorkflowProgress
from launchflow.gcp.cloud_run import CloudRun
from launchflow.gcp.service import GCPService
from launchflow.managers.service_manager import ServiceManager
from launchflow.models.flow_state import GCPEnvironmentConfig
from launchflow.workflows.utils import tar_source_in_memory


async def _upload_source_tarball_to_gcs(
    source_tarball_gcs_path: str,
    artifact_bucket: str,
    local_source_dir: str,
    build_ignore: List[str],
):
    try:
        from google.cloud import storage
    except ImportError:
        raise exceptions.MissingGCPDependency()

    def upload_async():
        source_tarball = tar_source_in_memory(local_source_dir, build_ignore)

        try:
            bucket = storage.Client().get_bucket(artifact_bucket)
            blob = bucket.blob(source_tarball_gcs_path)
            blob.upload_from_file(source_tarball)
        except Exception:
            raise exceptions.UploadSrcTarballFailed()

    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, upload_async)


# TODO: builds are not going to the correct gcp project
async def _run_docker_gcp_cloud_build(
    docker_repository: str,
    docker_image_name: str,
    docker_image_tag: str,
    gcs_source_bucket: str,
    gcs_source_object: str,
    gcp_project_id: str,
    dockerfile_path: str,
    artifact_bucket: str,
):
    try:
        from google.cloud.devtools import cloudbuild_v1
    except ImportError:
        raise exceptions.MissingGCPDependency()

    latest_image_name = f"{docker_repository}/{docker_image_name}:latest"
    tagged_image_name = f"{docker_repository}/{docker_image_name}:{docker_image_tag}"

    # Create the Cloud Build build plan
    build = cloudbuild_v1.Build(
        source=cloudbuild_v1.Source(
            storage_source=cloudbuild_v1.StorageSource(
                bucket=gcs_source_bucket, object_=gcs_source_object
            )
        ),
        # TODO: determine if we should set the service account still
        # service_account=f"projects/{gcp_project_id}/serviceAccounts/{env_service_account_email}",
        logs_bucket=f"gs://{artifact_bucket}/logs/cloud-builds",
        steps=[
            # Pull the latest image from the registry to use as a cache
            cloudbuild_v1.BuildStep(
                name="gcr.io/cloud-builders/docker",
                entrypoint="bash",
                args=[
                    "-c",
                    f"docker pull {latest_image_name} || exit 0",
                ],
            ),
            # Build the docker image with the cache from the latest image
            cloudbuild_v1.BuildStep(
                name="gcr.io/cloud-builders/docker",
                args=[
                    "build",
                    "-t",
                    latest_image_name,
                    "-t",
                    tagged_image_name,
                    "--cache-from",
                    latest_image_name,
                    "-f",
                    dockerfile_path,
                    ".",
                ],
            ),
        ],
        # NOTE: This is what pushes the image to the registry
        images=[latest_image_name, tagged_image_name],
    )
    # Submit the build to Cloud Build
    cloud_build_client = cloudbuild_v1.CloudBuildAsyncClient()
    operation = await cloud_build_client.create_build(
        project_id=gcp_project_id, build=build
    )
    build_url = f"https://console.cloud.google.com/cloud-build/builds/{operation.metadata.build.id}?project={gcp_project_id}"
    # Add logs to the table to the table
    await operation.result()

    # Return the docker image name
    return tagged_image_name, build_url


def _write_build_logs(file_path: str, log_stream):
    with open(file_path, "w") as f:
        for chunk in log_stream:
            if "stream" in chunk:
                f.write(chunk["stream"])


# TODO: Look into cleaning up old images. I noticed my docker images were taking up a lot of space
# after running this workflow multiple times
async def _build_docker_image_local(
    docker_repository: str,
    docker_image_name: str,
    docker_image_tag: str,
    local_source_dir: str,
    dockerfile_path: str,
    build_logs_file: str,
):
    try:
        from docker import errors, from_env
    except ImportError:
        raise exceptions.MissingDockerDependency()
    try:
        import google.auth
        import google.auth.transport.requests

    except ImportError:
        raise exceptions.MissingGCPDependency()

    docker_client = from_env()
    latest_image_name = f"{docker_repository}/{docker_image_name}:latest"
    tagged_image_name = f"{docker_repository}/{docker_image_name}:{docker_image_tag}"
    # Authenticate with the docker registry
    creds, _ = google.auth.default(
        scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )
    creds.refresh(google.auth.transport.requests.Request())
    docker_client.login(
        username="oauth2accesstoken",
        password=creds.token,
        registry=f"https://{docker_repository.split('/')[0]}",
    )

    # Pull the latest image from the registry to use as a cache
    try:
        # TODO: This is throwing a 500 error saying unauthorized
        docker_client.images.pull(latest_image_name)
        cache_from = [latest_image_name]
    except errors.NotFound:
        # NOTE: this happens on the first build
        cache_from = []

    # Build the docker image with the cache from the latest image
    loop = asyncio.get_event_loop()
    try:
        _, log_stream = await loop.run_in_executor(
            None,
            lambda: docker_client.images.build(
                path=os.path.dirname(local_source_dir),
                dockerfile=dockerfile_path,
                tag=tagged_image_name,
                cache_from=cache_from,
                # NOTE: this is required to build on mac
                platform="linux/amd64",
            ),
        )
        _write_build_logs(build_logs_file, log_stream)
    except BuildError as e:
        _write_build_logs(build_logs_file, e.build_log)
        raise

    # Tag as latest
    docker_client.images.get(tagged_image_name).tag(latest_image_name)

    # Push the images to the registry
    docker_client.images.push(tagged_image_name)
    docker_client.images.push(latest_image_name)

    # Return the docker image name
    return tagged_image_name


async def _promote_docker_image(
    source_env_region: str,
    source_docker_image: str,
    target_docker_repository: str,
    docker_image_name: str,
    docker_image_tag: str,
    target_gcp_project_id: str,
    target_artifact_bucket: str,
    workflow_progress: WorkflowProgress,
):
    try:
        import google.auth
        import google.auth.transport.requests
        from google.cloud.devtools import cloudbuild_v1
    except ImportError:
        raise exceptions.MissingGCPDependency()

    with workflow_progress.step("Promoting Docker image", "Docker image promoted"):
        target_image = f"{target_docker_repository}/{docker_image_name}"
        tagged_target_image = f"{target_image}:{docker_image_tag}"

        # Fetch creds to use for pulling the source image in the target's project
        creds, _ = google.auth.default(
            scopes=["https://www.googleapis.com/auth/cloud-platform"]
        )
        creds.refresh(google.auth.transport.requests.Request())

        build = cloudbuild_v1.Build(
            # TODO: determine if we should set the service account still
            # service_account=f"projects/{target_gcp_project_id}/serviceAccounts/{target_env_service_account_email}",
            logs_bucket=f"gs://{target_artifact_bucket}/logs/cloud-builds",
            steps=[
                # Pull the latest image from the registry to use as a cache
                cloudbuild_v1.BuildStep(
                    name="gcr.io/cloud-builders/docker",
                    entrypoint="bash",
                    args=[
                        "-c",
                        (
                            f"echo {creds.token} | docker login --username=oauth2accesstoken --password-stdin https://{source_env_region}-docker.pkg.dev "
                            f"&& docker pull {source_docker_image} "
                            f"&& docker tag {source_docker_image} {target_image}:{docker_image_tag} "
                        ),
                    ],
                ),
            ],
            # NOTE: This is what pushes the image to the registry
            images=[target_image, tagged_target_image],
        )
        # Submit the build to Cloud Build
        cloud_build_client = cloudbuild_v1.CloudBuildAsyncClient()
        operation = await cloud_build_client.create_build(
            project_id=target_gcp_project_id, build=build
        )
        build_url = f"https://console.cloud.google.com/cloud-build/builds/{operation.metadata.build.id}?project={target_gcp_project_id}"
        # Add logs to the table to the table
        workflow_progress.add_logs_row("build", build_url)
        await operation.result()

    # Return the docker image name
    return tagged_target_image


async def build_and_push_gcp_service(
    gcp_service: GCPService,
    service_manager: ServiceManager,
    gcp_environment_config: GCPEnvironmentConfig,
    deployment_id: str,
    build_local: bool,
) -> Tuple[str, str]:
    if build_local:
        return await build_docker_image_locally(
            gcp_service=gcp_service,
            service_manager=service_manager,
            deployment_id=deployment_id,
        )
    return await build_docker_image_on_cloud_build(
        gcp_service=gcp_service,
        service_manager=service_manager,
        gcp_environment_config=gcp_environment_config,
        deployment_id=deployment_id,
    )


async def build_docker_image_on_cloud_build(
    gcp_service: GCPService,
    service_manager: ServiceManager,
    gcp_environment_config: GCPEnvironmentConfig,
    deployment_id: str,
) -> str:
    full_yaml_path = os.path.dirname(
        os.path.abspath(config.launchflow_yaml.config_path)
    )
    local_source_dir = os.path.join(full_yaml_path, gcp_service.build_directory)
    # Step 1 - Upload the source tarball to GCS
    source_tarball_gcs_path = f"builds/{service_manager.project_name}/{service_manager.environment_name}/services/{service_manager.service_name}/source.tar.gz"
    await _upload_source_tarball_to_gcs(
        source_tarball_gcs_path=source_tarball_gcs_path,
        artifact_bucket=gcp_environment_config.artifact_bucket,
        local_source_dir=local_source_dir,
        build_ignore=gcp_service.build_ignore,
    )

    service_outputs = gcp_service.outputs()

    # Step 2 - Build and push the docker image
    docker_image, build_url = await _run_docker_gcp_cloud_build(
        docker_repository=service_outputs.docker_repository,
        docker_image_name=service_manager.service_name,
        docker_image_tag=deployment_id,
        gcs_source_bucket=gcp_environment_config.artifact_bucket,
        gcs_source_object=source_tarball_gcs_path,
        gcp_project_id=gcp_environment_config.project_id,
        dockerfile_path=gcp_service.dockerfile,
        artifact_bucket=gcp_environment_config.artifact_bucket,
    )

    return docker_image, build_url


async def build_docker_image_locally(
    gcp_service: GCPService,
    service_manager: ServiceManager,
    deployment_id: str,
) -> str:
    full_yaml_path = os.path.dirname(
        os.path.abspath(config.launchflow_yaml.config_path)
    )
    local_source_dir = os.path.join(full_yaml_path, gcp_service.build_directory)

    service_outputs = gcp_service.outputs()

    base_logging_dir = "/tmp/launchflow"
    os.makedirs(base_logging_dir, exist_ok=True)
    build_logs_file = (
        f"{base_logging_dir}/{service_manager.service_name}-{int(time.time())}.log"
    )

    # Step 1 - Build and push the docker image
    docker_image = await _build_docker_image_local(
        docker_repository=service_outputs.docker_repository,
        docker_image_name=service_manager.service_name,
        docker_image_tag=deployment_id,
        local_source_dir=local_source_dir,
        dockerfile_path=gcp_service.dockerfile,
        build_logs_file=build_logs_file,
    )

    return docker_image, build_logs_file


# TODO: It looks like there might be a transient error we need to handle and retry
# Revision 'my-service-new-env-00005-zdj' is not ready and cannot serve traffic. Health check
# failed for the deployment with the user-provided VPC network. Got permission denied error.
async def release_docker_image_to_cloud_run(
    docker_image: str,
    gcp_project_id: str,
    gcp_region: str,
    cloud_run_service: CloudRun,
) -> str:
    try:
        from google.cloud import run_v2
    except ImportError:
        raise exceptions.MissingGCPDependency()

    client = run_v2.ServicesAsyncClient()
    service = await client.get_service(
        name=f"projects/{gcp_project_id}/locations/{gcp_region}/services/{cloud_run_service._cloud_run_service_container.resource_id}"
    )
    # Updating the service container will trigger a new revision to be created
    service.template.containers[0].image = docker_image
    operation = await client.update_service(request=None, service=service)
    response = await operation.result()

    # This is the cloud run service url
    return response.uri
