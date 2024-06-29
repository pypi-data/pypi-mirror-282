from dataclasses import dataclass
from enum import Enum
from typing import Optional, Union

from google.cloud.compute_v1.services.disks.transports.rest import Dict

from launchflow.gcp.resource import GCPResource
from launchflow.models.enums import EnvironmentType, ResourceProduct
from launchflow.models.flow_state import EnvironmentState
from launchflow.node import Outputs
from launchflow.resource import TofuInputs


@dataclass
class ArtifactRegistryOutputs(Outputs):
    # NOTE: This is only set if the format is DOCKER
    docker_repository: Optional[str] = None


@dataclass
class ArtifactRegistryInputs(TofuInputs):
    format: str
    location: Optional[str] = None


class RegistryFormat(Enum):
    DOCKER = "DOCKER"
    MAVEN = "MAVEN"
    NPM = "NPM"
    PYTHON = "PYTHON"
    APT = "APT"
    YUM = "YUM"
    KUBEFLOW = "KUBEFLOW"
    GENERIC = "GENERIC"


class ArtifactRegistryRepository(GCPResource[ArtifactRegistryOutputs]):
    product = ResourceProduct.GCP_ARTIFACT_REGISTRY_REPOSITORY

    def __init__(
        self,
        name: str,
        format: Union[str, RegistryFormat],
        location: Optional[str] = None,
    ) -> None:
        super().__init__(
            name=name,
            replacement_arguments={"format", "location"},
        )
        if isinstance(format, str):
            format = RegistryFormat(format.upper())
        self.format = format
        self.location = location

    def import_resource(self, environment: EnvironmentState) -> Dict[str, str]:
        location = self.location or environment.gcp_config.default_region
        return {
            "google_artifact_registry_repository.repository": f"projects/{environment.gcp_config.project_id}/locations/{location}/repositories/{self.resource_id}",
        }

    def inputs(self, environment_type: EnvironmentType) -> ArtifactRegistryInputs:
        return ArtifactRegistryInputs(
            resource_id=self.resource_id,
            format=self.format.value,
            location=self.location,
        )
