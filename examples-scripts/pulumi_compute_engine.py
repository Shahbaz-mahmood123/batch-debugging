from infrastructure.pulumi import PulumiExecution
from infrastructure.gcp_compute_engine import PulumiGCP
from infrastructure.pulumi_config import PulumiGCPConfig



def create_tower_deployment():
    
    # Intialize the config class and 
    config = PulumiGCPConfig("./random-files/pulumi-dev.yaml")

    #the working directory where pulumi files wi
    work_dir = '/Users/shahbazmahmood/workspace/pulumi-stack/'

    # the class that holds pulumi script for creating the pulumi script
    pulumi_gcp = PulumiGCP(project_id=config.project_id, location=config.location, 
                           name=config.resource_name, region=config.region, zone=config.zone , instance_name=config.instance_name)
    
    #Main class that is called for executing up, down, refresh, destroy and preview
    pulumi_execution = PulumiExecution(config.project_id, config.stack_name,work_dir, pulumi_gcp)

    #call class i.e call preview to preview the resources created.
    pulumi_execution.preview()