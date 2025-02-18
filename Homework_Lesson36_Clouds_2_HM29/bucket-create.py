from google.cloud import storage

bucket_name = "bucket-for-hm"

def create_bucket():
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = "STANDARD"
    storage_client.create_bucket(bucket, location="EU")
    print(f"Bucket {bucket_name} created.")

def upload_file(file_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    blob.upload_from_filename(file_name)
    print(f"Uploaded {file_name} to {bucket_name}.")

create_bucket()
upload_file("example.txt")
