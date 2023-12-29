import time
import pulumi
import pulumi_gcp as gcp 
from pulumi_gcp import compute
#from pulumi_command import remote
from google.cloud import storage

from infrastructure.pulumi_infra_config import PulumiInfraConfig


class PulumiGCPInterface():
    
    def pulumi_program(self):
        pass 
    
    def get_secrets(self):
        pass

class PulumiGCP(PulumiInfraConfig, PulumiGCPInterface):
    
    def __init__(self, project_id: str, location: str, name: str, region:str , zone: str, instance_name: str) -> None:
        self.project_id = project_id 
        self.location = location
        self.name = name
        self.region = region 
        self.zone = zone
        self.instance_name = instance_name
    
    def upload_to_gcp_bucket(self,file_path: str, bucket_name: str) -> None:
        """Uploads a file to a GCP bucket.
        Args:
            file_path (str): The local path of the file to be uploaded.
            bucket_name (str): The name of the GCP bucket to upload the file to.
        """
        
        
        client = storage.Client()

        bucket = client.get_bucket(bucket_name)

        file_name = file_path.split("/")[-1]
        
        blob = bucket.blob(file_name)

        blob.upload_from_filename(file_path)

        print(f"File {file_name} uploaded to GCP bucket {bucket_name}.")
    
    def pulumi_program(self):

        # Creates a GCP storage bucket with the specified name

        bucket = gcp.storage.Bucket(self.name, name=self.name, location=self.location, project=self.project_id)
        
        temp_bucket_name = "temp-seqera-bucket"
        
        temp_bucket = gcp.storage.Bucket(temp_bucket_name, name=temp_bucket_name, location=self.location, project=self.project_id, force_destroy=True)
                    
                
        service_account = gcp.serviceaccount.Account("my-service-account",
                                             account_id="my-service-account",
                                             display_name="My Service Account", 
                                             project=self.project_id)
        
        # Give the service account permissions to manage objects in the bucket
        bucket_iam_binding = gcp.storage.BucketIAMBinding(f"{self.name}-binding",
                                                        bucket=bucket.name,
                                                        role="roles/storage.admin",
                                                        members=[pulumi.Output.concat("serviceAccount:", service_account.email)])
        
        # Give the service account permissions to manage objects in the bucket
        bucket_iam_binding = gcp.storage.BucketIAMBinding("temp-bucket-binding",
                                                        bucket=temp_bucket.name,
                                                        role="roles/storage.admin",
                                                        members=[pulumi.Output.concat("serviceAccount:", service_account.email)])
        
        # Export the bucket's URL
        pulumi.export('bucket_url', bucket.url)
        pulumi.export('temp_bucket_url', temp_bucket.url)
        
        # Create a VPC network
        network = gcp.compute.Network(f'{self.name}-vpc',
                                      auto_create_subnetworks=False, # We have more control over the network topology when this is False
                                      project = self.project_id)
        
        pulumi.export('network_id', network.id)

        # Create a GCP subnet
        subnet = gcp.compute.Subnetwork(f'{self.name}-subnet',
                                ip_cidr_range="10.2.0.0/16",
                                network=network.id,
                                region=self.region, 
                                project = self.project_id
                                )
        
        pulumi.export('subnetwork_id', subnet.id)
         
        compute_firewall = compute.Firewall(
        "firewall",
        project = self.project_id,
        source_ranges = ["0.0.0.0/0"],
        network=network.self_link,
        allows=[compute.FirewallAllowArgs(
            protocol="tcp",
            ports=["22", "80", "443"],
        )], source_tags = ["seqera-platform"]
            )   
        
        
        time.sleep(10)
        docker_compose = "requirements.txt"
        
        tower_env = ""
        
        tower_yml = ""
        
        groundswell_yml = ""
        
        self.upload_to_gcp_bucket(file_path=docker_compose, bucket_name=temp_bucket_name)

        # A simple bash script that will run when the webserver is initalized
        startup_script = f"""#!/bin/bash
        
        
        BUCKET_NAME="{temp_bucket_name}"
        OBJECT_NAME="{docker_compose}"

        # Set the destination directory on the VM
        DESTINATION_DIR="./"

        # Ensure the destination directory exists
        mkdir -p $DESTINATION_DIR

        # Download the file using gsutil
        gsutil cp gs://$BUCKET_NAME/$OBJECT_NAME $DESTINATION_DIR

        echo "Hello, Seqera!" > index.html
        nohup python -m SimpleHTTPServer 80 &"""

        # instance_addr = compute.address.Address("address")
        
        compute_instance = compute.Instance(
            self.instance_name,
            project = self.project_id,
            machine_type="f1-micro",
            zone = self.zone,
            metadata_startup_script=startup_script,
            tags = ["seqera-platform", "http-server"],
            boot_disk=compute.InstanceBootDiskArgs(
                initialize_params=compute.InstanceBootDiskInitializeParamsArgs(
                    image="debian-cloud/debian-9-stretch-v20181210"
                )
            ),
            network_interfaces=[compute.InstanceNetworkInterfaceArgs(
                    network=network.id,
                    subnetwork = subnet.id,
                    access_configs=[compute.InstanceNetworkInterfaceAccessConfigArgs()]
            )],
            service_account=gcp.compute.InstanceServiceAccountArgs(
                email=service_account.email,
                scopes=["https://www.googleapis.com/auth/cloud-platform"],
            ))
        
        pulumi.export("instanceName", compute_instance.name)
        pulumi.export("tags", compute_instance.labels)
        pulumi.export("instanceIP", compute_instance.network_interfaces)
            
    def get_secrets(self):
        pass