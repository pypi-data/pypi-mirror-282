provider "google" {
  project = var.gcp_project_id
  region  = var.gcp_region
}


resource "google_artifact_registry_repository" "repository" {
  repository_id = var.resource_id
  location      = var.location != null ? var.location : var.gcp_region
  format        = var.format
  # TODO: add additional configuration
}

locals {
  docker_repository = var.format == "DOCKER" ? "${google_artifact_registry_repository.repository.location}-docker.pkg.dev/${google_artifact_registry_repository.repository.project}/${google_artifact_registry_repository.repository.repository_id}" : null
}


output "docker_repository" {
  value = local.docker_repository
}

output "gcp_id" {
  value = google_artifact_registry_repository.repository.id
}
