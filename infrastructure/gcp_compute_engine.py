import pulumi
import pulumi_gcp as gcp 
from pulumi_gcp import compute

class PulumiInfraConfig(): 
    
    def pulumi_program(self):
        pass
        
class PulumiGCPInterface():
    pass 

        
class PulumiGCP(PulumiInfraConfig, PulumiGCPInterface):
    
    def __init__(self, project_id: str, location: str, name: str, region:str , zone: str, instance_name: str) -> None:
        self.project_id = project_id 
        self.location = location
        self.name = name
        self.region = region 
        self.zone = zone
        self.instance_name = instance_name
        
    def pulumi_program(self):

        # Creates a GCP storage bucket with the specified name
        bucket = gcp.storage.Bucket(self.name,
                                    name=self.name, location=self.location, project=self.project_id)

        # Export the bucket's URL
        pulumi.export('bucket_url', bucket.url)
        
        # Create a VPC network
        network = gcp.compute.Network("seqera-platform",
                                      auto_create_subnetworks=False # We have more control over the network topology when this is False
                                      )
        
        pulumi.export('network_id', network.id)

        # Create a GCP subnet
        subnet = gcp.compute.Subnetwork("seqera-platform-subnetwork",
                                ip_cidr_range="10.2.0.0/16",
                                network=network.id,
                                region="us-central1"
                                )
        
        pulumi.export('subnetwork_id', subnet.id)
         
        compute_firewall = compute.Firewall(
        "firewall",
        network=network.self_link,
        allows=[compute.FirewallAllowArgs(
            protocol="tcp",
            ports=["22", "80"],
        )], source_tags = ["seqera-platform"]
            )   

        # A simple bash script that will run when the webserver is initalized
        startup_script = """#!/bin/bash
        echo "Hello, World!" > index.html
        nohup python -m SimpleHTTPServer 80 &"""

        instance_addr = compute.address.Address("address")
        compute_instance = compute.Instance(
            self.instance_name,
            machine_type="f1-micro",
            metadata_startup_script=startup_script,
            boot_disk=compute.InstanceBootDiskArgs(
                initialize_params=compute.InstanceBootDiskInitializeParamsArgs(
                    image="debian-cloud/debian-9-stretch-v20181210"
                )
            ),
            network_interfaces=[compute.InstanceNetworkInterfaceArgs(
                    network=network.id,
                    access_configs=[compute.InstanceNetworkInterfaceAccessConfigArgs(
                        nat_ip=instance_addr.address
                    )],
            )],
            service_account=compute.InstanceServiceAccountArgs(
                scopes=["https://www.googleapis.com/auth/cloud-platform"],
            ),
            #opts=ResourceOptions(depends_on=[compute_firewall]),
        )

        pulumi.export("instanceName", compute_instance.name)
        pulumi.export("instanceIP", instance_addr.address)
            
    def get_secrets(self):
        pass