provider "google" {
  credentials = file("/mnt/d/git/Artiom_Strelchenko_DOS23/Homework_Lesson35_Clouds_1_HM28/turing-bebop-450119-g5-75a718581401.json")
  project = "turing-bebop-450119-g5"
  region  = "europe-west3-c"
}

resource "google_compute_instance_template" "default" {
  name_prefix  = "my-instance-template-terraform"
  machine_type = "e2-medium"

  disk {
    source_image = "debian-cloud/debian-12"
  }

  network_interface {
    network = "default"
  }

}

resource "google_compute_instance_group_manager" "default" {
  name               = "my-instance-group-terraform"
  base_instance_name = "my-instance"
  zone               = "europe-west3-c"

  version {
    instance_template = google_compute_instance_template.default.self_link
  }

  target_size = 2
}

resource "google_compute_autoscaler" "default" {
  name   = "my-autoscaler"
  zone   = "europe-west3-c"
  target = google_compute_instance_group_manager.default.self_link

  autoscaling_policy {
    max_replicas    = 5
    min_replicas    = 2
    cpu_utilization {
      target = 0.7
    }
  }
}