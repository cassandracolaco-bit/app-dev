terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
    }
  }
}

provider "docker" {}

resource "docker_image" "app" {
  name = "myapp:latest"
}

resource "docker_container" "app" {
  name  = "my-container"
  image = docker_image.app.image_id

  ports {
    internal = 8080
    external = 5000
  }
}