provider "google" {
  project = "turing-bebop-450119-g5"
  region  = "europe-west3"
  zone    = "europe-west3-a"
}

resource "google_compute_instance" "vm_instance" {
  name         = var.vm_name 
  machine_type = "e2-micro"
  zone         = "europe-west3-a"

  boot_disk {
    initialize_params {
      image = "debian-12-bookworm-v20250212" 
    }
  }

  network_interface {
    network = "default"
    access_config {
    }
  }

}

output "vm_name" {
  value = google_compute_instance.vm_instance.name
}
