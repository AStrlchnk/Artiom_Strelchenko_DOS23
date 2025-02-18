import os
from google.cloud import firestore
from google.cloud import compute_v1

def stop_instances(request):
    project = os.getenv('turing-bebop-450119-g5')
    zone = 'europe-west3-a'

    compute_client = compute_v1.InstancesClient()

    instances = compute_client.aggregated_list(project=project)

    for instance in instances:
        if 'instances' in instance[1]:
            for vm in instance[1]['instances']:
                if vm['status'] == 'RUNNING':  
                    print(f"Stopping VM: {vm['name']}")
                    stop_operation = compute_client.stop(
                        project=project,
                        zone=zone,
                        instance=vm['name']
                    )
                    print(f"Stopping operation: {stop_operation.name}")

    return 'Done'
