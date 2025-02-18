from google.cloud import compute_v1

project_id = "turing-bebop-450119-g5"
zone = "europe-west3-a"
instance_name = "instance-for-hm"

def create_instance():
    instances_client = compute_v1.InstancesClient()

    instance = compute_v1.Instance()
    instance.name = instance_name
    instance.machine_type = f"zones/{zone}/machineTypes/e2-micro"
    
    disk = compute_v1.AttachedDisk()
    disk.initialize_params = compute_v1.AttachedDiskInitializeParams(
        disk_name="my-ssd",
        source_image="projects/debian-cloud/global/images/family/debian-12",
        disk_size_gb=50,
        disk_type=f"zones/{zone}/diskTypes/pd-ssd"
    )
    disk.boot = True
    instance.disks = [disk]

    instance.network_interfaces = [
        compute_v1.NetworkInterface(
            name="global/networks/default"
        )
    ]

    operation = instances_client.insert(
        project=project_id, zone=zone, instance_resource=instance
    )
    operation.result()
    print(f"Instance {instance_name} created.")

create_instance()
