import pulumi
import pulumi_gcp as gcp 
from pulumi_infra_config import PulumiInfraConfig

class IPulumiGKE():
    
    def get_secrets(self):
        pass

class PulumiGKE(PulumiInfraConfig, IPulumiGKE):
    
    def __init__(self, project_id: str, location: str, name: str, region:str , zone: str, cluster_name: str, cluster_type: str, nodes: dict) -> None:
        self.project_id = project_id 
        self.name = name
        self.region = region 
        self.zone = zone
        self.cluster_name = cluster_name
        self.cluster_type = cluster_type
        self.nodes = nodes
        
    def pulumi_program(self):
        pass
    
    def get_secrets(self):
        pass