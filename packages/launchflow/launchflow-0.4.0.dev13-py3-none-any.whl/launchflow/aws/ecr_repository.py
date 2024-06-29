from dataclasses import dataclass
from typing import Literal

from launchflow.aws.resource import AWSResource
from launchflow.models.enums import EnvironmentType, ResourceProduct
from launchflow.node import Outputs
from launchflow.resource import TofuInputs


@dataclass
class ECRRepositoryOutputs(Outputs):
    repository_url: str


@dataclass
class ECRRepositoryInputs(TofuInputs):
    force_delete: bool
    image_tag_mutability: Literal["MUTABLE", "IMMUTABLE"]


class ECRRepository(AWSResource[ECRRepositoryOutputs]):
    product = ResourceProduct.AWS_ECR_REPOSITORY

    def __init__(
        self,
        name: str,
        force_delete: bool = True,
        image_tag_mutability: Literal["MUTABLE", "IMMUTABLE"] = "MUTABLE",
    ) -> None:
        super().__init__(
            name=name,
            replacement_arguments={"format", "location"},
        )
        self.force_delete = force_delete
        self.image_tag_mutability = image_tag_mutability

    def inputs(self, environment_type: EnvironmentType) -> ECRRepositoryInputs:
        return ECRRepositoryInputs(
            resource_id=self.resource_id,
            force_delete=self.force_delete,
            image_tag_mutability=self.image_tag_mutability,
        )
