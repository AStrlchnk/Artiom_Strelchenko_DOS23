provider "google" {
  credentials = file("/mnt/d/git/Artiom_Strelchenko_DOS23/Homework_Lesson35_Clouds_1_HM28/turing-bebop-450119-g5-75a718581401.json")
  project = "turing-bebop-450119-g5"
  region  = "europe-west3"
}

resource "google_storage_bucket" "my_bucket" {
  name          = "test-bucket-strel-terraform"
  location      = "europe-west3"
  storage_class = "STANDARD"

  versioning {
    enabled = true
  }
}