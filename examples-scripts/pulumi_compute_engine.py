from infrastructure.pulumi import PulumiExecution
from infrastructure.minimal_gcp_compute_engine import MinimalPulumiGCP
from infrastructure.pulumi_config import PulumiGCPConfig

def create_tower_deployment():
    
    # Intialize the config class and 
    config = PulumiGCPConfig("./random-files/pulumi-dev.yaml")

    #the working directory where pulumi files wi
    work_dir = '/Users/shahbazmahmood/workspace/pulumi-stack/'

    # the class that holds pulumi script for creating the pulumi script
    pulumi_gcp = MinimalPulumiGCP(project_id=config.project_id, location=config.location, 
                           name=config.resource_name, region=config.region, zone=config.zone , instance_name=config.instance_name,
                           tower_env_secret=config.tower_env_secret, tower_yaml_secret=config.tower_yaml_secret, 
                           harbor_creds=config.harbor_creds, groundswell_secret=config.groundswell)
    
    #Main class that is called for executing up, down, refresh, destroy and preview
    pulumi_execution = PulumiExecution(config.project_id, config.stack_name,work_dir, pulumi_gcp)

    #call class i.e call preview to preview the resources created.
    pulumi_execution.preview()
    