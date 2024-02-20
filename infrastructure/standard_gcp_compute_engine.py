import time, os 

import pulumi
import pulumi_gcp as gcp 
from pulumi_gcp import compute
import pulumi_command as command
#from pulumi_command import remote
from google.cloud import storage
# from google.cloud import secretmanager
from google.cloud.exceptions import NotFound, Forbidden

from infrastructure.pulumi_infra_config import PulumiInfraConfig
from infrastructure.pulumi_config import StandardPulumiGCPConfig
from infrastructure.seqera_platform import SeqeraGCPConfig

class PulumiGCPInterface():
    
    def pulumi_program(self):
        pass 
    
    def run_sql_commands(self, instance_name: str):
        pass

class MinimalPulumiGCP(PulumiInfraConfig, PulumiGCPInterface):
    
    def __init__(self, config: StandardPulumiGCPConfig) -> None:
        self.project_id = config.project_id 
        self.location = config.location
        self.name = config.name
        self.region = config.region 
        self.zone = config.zone
        self.instance_name = config.instance_name
        self.tower_env_secret = config.secrets.tower_env_secret
        self.tower_yaml_secret = config.secrets.tower_yaml_secret
        self.harbor_creds = config.secrets.harbor_creds
        self.groundswell_secret = config.secrets.groundswell_secret
        self.source_ranges = config.network.source_ranges
        self.tags = config.network.tags
        self.source_tags = config.compute_engine.tags
    
    def pulumi_program(self):

        self.check_resource_exists()
        
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
        # Create a VPC network
        network = gcp.compute.Network(f'{self.name}-vpc',
                                      auto_create_subnetworks=False, # We have more control over the network topology when this is False
                                      project = self.project_id)

        # Create a GCP subnet
        subnet = gcp.compute.Subnetwork(f'{self.name}-subnet',
                                ip_cidr_range="10.2.0.0/16",
                                network=network.id,
                                region=self.region, 
                                project = self.project_id
                                )
        
         
        compute_firewall = compute.Firewall(
        "firewall",
        project = self.project_id,
        source_ranges = self.source_ranges,
        network=network.self_link,
        allows=[compute.FirewallAllowArgs(
            protocol="tcp",
            ports=["22", "8000"],
        )], source_tags = self.source_tags
            )   

                # Create a Cloud SQL instance
        cloud_sql_instance = gcp.sql.DatabaseInstance(f'{self.name}-sql',
                                                    database_version="MYSQL_8_0",
                                                    #region=self.region,
                                                    settings=gcp.sql.DatabaseInstanceSettingsArgs(
                                                        tier="db-f1-micro",
                                                        ip_configuration=gcp.sql.DatabaseInstanceSettingsIpConfigurationArgs(
                                                            private_network=network.id
                                                        )
                                                    ))

        # When the Cloud SQL instance is created, call the function run_sql_commands
        cloud_sql_instance.name.apply(self.run_sql_commands)
        
        # Create a static IP address.
        static_ip = gcp.compute.Address("static-ip", region="us-central1",  project=self.project_id)

        # my_secret = gcp.secretmanager.get_secret_version_output(
        #     secret=self.tower_env_secret,
        #     secret_version="latest"  # using "latest" to fetch the newest version
        # )
        
        # Get secrets from secret manager 
        tower_env_version = gcp.secretmanager.get_secret_version(secret=self.tower_env_secret, project=self.project_id)

        #tower_yml_version = gcp.secretmanager.get_secret_version(secret=self.tower_yaml_secret, project=self.project_id)
        groundswell_version = gcp.secretmanager.get_secret_version(secret=self.groundswell_secret, project=self.project_id)
        docker_creds_version = gcp.secretmanager.get_secret_version(secret=self.harbor_creds, project=self.project_id)

        
        # pulumi.export('tower_env', tower_env_version.secret_data)
        # pulumi.export('tower_yml', tower_yml_version.secret_data)
        # pulumi.export('docker_creds', docker_creds_version.secret_data)
        
        #Replace tower.env files here
        # TODO: sed is using the mac version of sed need to replace that with linux.
        # https://stackoverflow.com/questions/4247068/sed-command-with-i-option-failing-on-mac-but-works-on-linux
        populate_tower_files_script = f"""
        #!/bin/bash
        echo "{tower_env_version.secret_data}" | tee tower.env
        #echo "tower_yml_version.secret_data" | tee tower.yml
        echo "{groundswell_version.secret_data}" | tee groundswell.env
        
        # Check if the file exists        
        config_file="./tower.env" 
        if [ -f "$config_file" ]; then
            # Replace the TOWER_SERVER_URL value
            sed -i '' "s|TOWER_SERVER_URL=.*|TOWER_SERVER_URL=http://$STATIC_IP:8000|" "$config_file"
            echo "TOWER_SERVER_URL replaced with: http://$STATIC_IP"
        else
            echo "Config file not found: $config_file"
        fi
        """

        populate_tower_files = command.local.Command(
            "echo-command",
            create=populate_tower_files_script,
            environment={
                "STATIC_IP": static_ip.address
            },
            # triggers={"alwaysRun": str(True)},
        )
        
        #If user does a preview ignore this and only execute on a pulumi up, not sure if I should require the user 
        # to have the config files present in the working directory or not show these four resources being created.  
        if  pulumi.runtime.is_dry_run() != True:
            current_working_directory = os.getcwd()
            docker_compose = f"{current_working_directory}/docker-compose.yml"
            tower_env = f"{current_working_directory}/tower.env"
            tower_yml = f"{current_working_directory}/tower.yml"
            groundswell_yml = f"{current_working_directory}/groundswell.env"
            
            docker_compose_upload = gcp.storage.BucketObject('docker-compose',
                                        bucket=temp_bucket.name,
                                        source=pulumi.FileAsset(docker_compose),
                                        name='docker-compose.yml',
                                        content_type='application/x-yaml',
                                        opts=pulumi.ResourceOptions(depends_on=[populate_tower_files]))
            
            tower_env_upload = gcp.storage.BucketObject('tower-env',
                                        bucket=temp_bucket.name,
                                        name='tower.env',
                                        source=pulumi.FileAsset(tower_env),
                                        opts=pulumi.ResourceOptions(depends_on=[populate_tower_files]))

            tower_yml_upload = gcp.storage.BucketObject('tower-yml',
                                        bucket=temp_bucket.name,
                                        source=pulumi.FileAsset(tower_yml),
                                        name='tower.yml',
                                        content_type='application/x-yaml',
                                        opts=pulumi.ResourceOptions(depends_on=[populate_tower_files]))
            
            groundswell_upload = gcp.storage.BucketObject('groundswell',
                                        bucket=temp_bucket.name,
                                        name='groundswell.env',
                                        source=pulumi.FileAsset(groundswell_yml),
                                        opts=pulumi.ResourceOptions(depends_on=[populate_tower_files]))
                    
        # A simple bash script that will run when the webserver is initalized
        print(docker_creds_version.secret_data)
        startup_script = f"""#!/bin/bash
       
        sudo apt-get -y update 
        sudo apt-get -y install jq
               
        BUCKET_NAME="{temp_bucket_name}"
        DOCKER_COMPOSE="docker-compose.yml"
        TOWER_ENV="tower.env"
        TOWER_YML="tower.yml"
        GROUNDSWELL="groundswell.env"
        
        # Extract docker credentials
        JSON_DATA='{docker_creds_version.secret_data}'
        ROBOT_NAME=$(echo "$JSON_DATA" | jq -r '.name')
        SECRET_PASSWORD=$(echo "$JSON_DATA" | jq -r '.secret')
        # Display the extracted values
        echo "JSON DATA: $JSON_DATA"
        echo "Robot Name: $ROBOT_NAME"
        echo "Secret Password: $SECRET_PASSWORD"
        
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
        
        service docker start
        
        docker login -u $ROBOT_NAME -p $SECRET_PASSWORD cr.seqera.io
        
        cd /home/seqera 
        docker compose up -d 
        
        # echo "Hello, Seqera!" > index.html
        # nohup python -m SimpleHTTPServer 80 &
        """
                # Create a Compute Engine instance template
        instance_template = gcp.compute.InstanceTemplate(
            self.project_id,
            f"{self.name}instance-template",
            machine_type="e2-standard-2",
            network_interfaces=[compute.InstanceNetworkInterfaceArgs (
                    network=network.id,
                    subnetwork = subnet.id,
                    access_configs=[compute.InstanceNetworkInterfaceAccessConfigArgs(
                        nat_ip=static_ip.address)]
            )],
            tags = self.tags,
            
            disks=[gcp.compute.InstanceTemplateDiskArgs(
                source_image="debian-12-bookworm-v20231212",
                auto_delete=True,
                boot=True,
            )],
            
            metadata={
                "startup-script": startup_script
            },
            service_account=gcp.compute.InstanceServiceAccountArgs (
                email=service_account.email,
                scopes=["https://www.googleapis.com/auth/cloud-platform"],
            )
        )

        # Create a managed instance group using the instance template
        instance_group = gcp.compute.InstanceGroupManager(f"{self.name}instance-group",
            base_instance_name=f"{self.name}-vm",
            instance_template=instance_template.id,
            zone=self.zone,
            target_size=1,
        )
        
        # Create a Compute Engine instance from the instance template
        compute_instance = gcp.compute.InstanceFromTemplate("instance-from-template",
            name=f"{self.name}-vm",
            zone=self.zone, # Specify the zone where to create the instance
            source_instance_template=instance_template.id
        )
        # Create a health check for the load balancer
        health_check = compute.HealthCheck(f'{self.name}-http-health-check',
            check_interval_sec=5,
            timeout_sec=5,
            healthy_threshold=2,
            unhealthy_threshold=2,
            tcp_health_check=compute.HealthCheckTcpHealthCheckArgs(port=80))

        # Create a backend service using the instance group
        backend_service = compute.BackendService(f'{self.name}-backend-service',
            backends=[compute.BackendServiceBackendArgs(
                group=instance_group.name 
            )],
            health_checks=[health_check.self_link],
            port_name='http',
            protocol='HTTP',
            timeout_sec=10)

        # Create a URL map to route incoming requests to the backend service
        url_map = compute.URLMap(f'{self.name} url-map',
            default_service=backend_service.self_link)

        # Create a target HTTP proxy to route requests to your URL map
        target_http_proxy = compute.TargetHttpProxy(f'{self.name}-target-http-proxy',
            url_map=url_map.self_link)

        # Create a global forwarding rule to route incoming requests to the proxy
        global_forwarding_rule = compute.GlobalForwardingRule(f'{self.name}-global-forwarding-rule',
            target=target_http_proxy.self_link,
            port_range='80')

        # Export the external IP address of the Load Balancer
        lb_ip = pulumi.Output.all(global_forwarding_rule.ip_address).apply(lambda args: args[0])
        
        pulumi.export('network_id', network.id)
        pulumi.export('bucket_url', bucket.url)
        pulumi.export('temp_bucket_url', temp_bucket.url)
        pulumi.export("instanceName", compute_instance.name)
        pulumi.export("tags", compute_instance.labels)
        pulumi.export("instanceIP", compute_instance.network_interfaces)
        pulumi.export('static_ip_address', static_ip.address)
        pulumi.export('subnetwork_id', subnet.id)
        pulumi.export('config files populate', populate_tower_files.stdout)
        pulumi.export('load_balancer_ip', lb_ip)
        
    def run_sql_commands(self, instance_name: str):
        pass
    
    def check_resource_exists(resource_type: str, resource_name: str, **kwargs):
        """
        Checks if the specified Pulumi resource exists.

        :param resource_type: The Pulumi resource type (e.g., aws.s3.Bucket).
        :param resource_name: The name of the resource to check.
        :param kwargs: Additional arguments required to identify the resource.
        :return: True if the resource exists, False otherwise.
        """
        try:
            # Try to get the resource with the provided details.
            resource = resource_type.get(resource_name, resource_name, **kwargs)
            return True if resource else False
        except pulumi.ResourceError:
            # If there's an exception, it means the resource does not exist.
            return False

    
