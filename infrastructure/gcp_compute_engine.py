import time, os 

import pulumi
import pulumi_gcp as gcp 
from pulumi_gcp import compute
import pulumi_command as command
#from pulumi_command import remote
from google.cloud import storage

from infrastructure.pulumi_infra_config import PulumiInfraConfig
from infrastructure.seqera_platform import SeqeraGCPConfig

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
    
    def upload_to_gcp_bucket(self,file_path: str, bucket_name: str ) -> None:
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
                    
                
        service_account = gcp.serviceaccount.Account("seqera-pulumi-sa",
                                             account_id="seqera-pulumi-sa",
                                             display_name="Seqera Pulumi SA", 
                                             project=self.project_id)
        
        # Give the service account permissions to manage objects in the bucket
        bucket_iam_binding = gcp.storage.BucketIAMBinding(f"{self.name}-binding",
                                                        bucket=bucket.name,
                                                        role="roles/storage.admin",
                                                        members=[pulumi.Output.concat("serviceAccount:", service_account.email)])
        
        # Give the service account permissions to manage objects in the bucket
        temp_bucket_iam_binding = gcp.storage.BucketIAMBinding("temp-bucket-binding",
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
        
        # Create a static IP address.
        static_ip = gcp.compute.Address("static-ip", region="us-central1")


        # TODO: pull in secrets from secret manager and populate files
        local_command = command.local.Command(
            "echo-command",
            create="echo 'Hello, World!'",
        )
        
        # Export the standard output of the command.
        pulumi.export('stdout', local_command.stdout)
        
        current_working_directory = os.getcwd()
        
        docker_compose = f"{current_working_directory}/docker-compose.yml"
        
        tower_env = f"{current_working_directory}/tower.env"
        
        tower_yml = f"{current_working_directory}/tower.yml"
        
        groundswell_yml = f"{current_working_directory}/groundswell.env"
        
        docker_compose_upload = gcp.storage.BucketObject('docker-compose',
                                     bucket=temp_bucket.name,
                                     source=pulumi.FileAsset(docker_compose),
                                     name='docker-compose.yml',
                                     content_type='application/x-yaml')
        
        tower_env_upload = gcp.storage.BucketObject('tower-env',
                                     bucket=temp_bucket.name,
                                     name='tower.env',
                                     source=pulumi.FileAsset(tower_env))

        tower_yml_upload = gcp.storage.BucketObject('tower-yml',
                                     bucket=temp_bucket.name,
                                     source=pulumi.FileAsset(tower_yml),
                                     name='tower.yml',
                                     content_type='application/x-yaml')
        
        groundswell_upload = gcp.storage.BucketObject('groundswell',
                                     bucket=temp_bucket.name,
                                     name='groundswell.env',
                                     source=pulumi.FileAsset(groundswell_yml))
        
        # try:
        #     file_upload = self.upload_to_gcp_bucket(file_path=docker_compose, bucket_name=temp_bucket_name)
        #     file_upload = self.upload_to_gcp_bucket(file_path=tower_env, bucket_name=temp_bucket_name)
        #     file_upload = self.upload_to_gcp_bucket(file_path=tower_yml, bucket_name=temp_bucket_name)
        #     file_upload = self.upload_to_gcp_bucket(file_path=groundswell_yml, bucket_name=temp_bucket_name)
        # except Exception as e:
        #     print(f'Error:{e}')
            
        # A simple bash script that will run when the webserver is initalized
        startup_script = f"""#!/bin/bash
        
        BUCKET_NAME="{temp_bucket_name}"
        DOCKER_COMPOSE="docker-compose.yml"
        TOWER_ENV="tower.env"
        TOWER_YML="tower.yml"
        GROUNDSWELL="groundswell.env"

        # Set the destination directory on the VM
        DESTINATION_DIR="/home/seqera"

        # Ensure the destination directory exists
        mkdir -p $DESTINATION_DIR

        # Download the file using gsutil
        gsutil cp gs://$BUCKET_NAME/$DOCKER_COMPOSE $DESTINATION_DIR
        gsutil cp gs://$BUCKET_NAME/$TOWER_ENV $DESTINATION_DIR
        gsutil cp gs://$BUCKET_NAME/$TOWER_YML $DESTINATION_DIR
        gsutil cp gs://$BUCKET_NAME/$GROUNDSWELL $DESTINATION_DIR

        # Add Docker's official GPG key:
        sudo apt-get -y update
        sudo apt-get -y install ca-certificates curl gnupg
        sudo install -m 0755 -d /etc/apt/keyrings
        curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
        sudo chmod a+r /etc/apt/keyrings/docker.gpg

        # Add the repository to Apt sources:
        echo \
        "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
        $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
        sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
        sudo apt-get update
        # Install Docker
        sudo apt-get -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
        
        #cd /home/seqera 
        #docker compose up -d 
        
        echo "Hello, Seqera!" > index.html
        nohup python -m SimpleHTTPServer 80 &"""

        
        compute_instance = compute.Instance(
            self.instance_name,
            project = self.project_id,
            machine_type="e2-standard-2",
            zone = self.zone,
            metadata_startup_script=startup_script,
            tags = ["seqera-platform", "http-server"],
            boot_disk=compute.InstanceBootDiskArgs(
                initialize_params=compute.InstanceBootDiskInitializeParamsArgs(
                    image="debian-12-bookworm-v20231212"
                )
            ),
            network_interfaces=[compute.InstanceNetworkInterfaceArgs(
                    network=network.id,
                    subnetwork = subnet.id,
                    access_configs=[compute.InstanceNetworkInterfaceAccessConfigArgs(
                        nat_ip=static_ip.address)]
            )],
            service_account=gcp.compute.InstanceServiceAccountArgs(
                email=service_account.email,
                scopes=["https://www.googleapis.com/auth/cloud-platform"],
            ))
        
        pulumi.export("instanceName", compute_instance.name)
        pulumi.export("tags", compute_instance.labels)
        pulumi.export("instanceIP", compute_instance.network_interfaces)
        pulumi.export('static_ip_address', static_ip.address)
            
    def get_secrets(self):
        pass