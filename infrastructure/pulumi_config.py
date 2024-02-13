import os
import yaml

from pydantic import BaseModel
from typing import List, Optional


class PulumiConfigInterface():
    def validate_yaml(self):
        pass
    
class PulumiConfig(PulumiConfigInterface):
    
    def __init__(self, file_path: str) -> None:
        
        with open(file_path, 'r') as file:
            configs = yaml.safe_load(file) 
        
        self.stack_name = configs['stack']
        self.provider = configs['provider']
        self.type = configs['type']

    def validate_yaml(self):
        pass
    
class Stack(BaseModel):
    stack: str
    type: str
    provider: str

class SeqeraSecrets(BaseModel):
    tower_env_secret: str
    tower_yaml_secret: str
    harbor_creds: str
    groundswell_secret: str
    
class Network(BaseModel):
    source_ranges: List[str]
    tags: List[str]
    
class ComputeEngine(BaseModel):
    tags: List[str]
    
class MinimalPulumiGCPConfig(BaseModel):
    stack: Stack
    location: str
    name: str
    project_id: str
    zone: str
    region: str
    instance_name: str
    secrets: SeqeraSecrets
    network: Network
    compute_engine: ComputeEngine
    
class MinimalPulumiGCPConfigYAML():
    
    def __init__(self, file_path: str) -> None:
        
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"YAML file not found: {file_path}")

        self.validate_yaml()
        
        with open(file_path, 'r') as file:
            self.configs = yaml.safe_load(file) 
        
        self.config_model = MinimalPulumiGCPConfig(**self.configs)
    
    ##TODO: Need to do some validation on the yaml maybe? 
    def validate_yaml(self):
        pass

class StandardPulumiGCPConfig(BaseModel):
    stack: Stack
    location: str
    name: str
    project_id: str
    zone: str
    region: str
    instance_name: str
    secrets: SeqeraSecrets
    network: Network
    compute_engine: ComputeEngine
    
class StandardMinimalPulumiGCPConfig():
    
    def __init__(self, file_path: str) -> None:
        
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"YAML file not found: {file_path}")
        self.validate_yaml()
        with open(file_path, 'r') as file:
            self.configs = yaml.safe_load(file) 
        
        self.config_model = MinimalPulumiGCPConfig(**self.configs)
        
    
    ##TODO: Need to do some validation on the yaml maybe? 
    def validate_yaml(self):
        pass
    
    
# Pydantic model for a taint applied to a set of nodes
class Taint(BaseModel):
    key: str
    value: str
    effect: str

# Combined Pydantic model for NodePool configuration
class NodePool(BaseModel):
    name: str
    initial_node_count: int
    machine_type: str
    disk_size_gb: int
    preemptible: bool
    oauth_scopes: List[str]
    tags: Optional[List[str]]
    labels: Optional[dict]
    taints: Optional[List[Taint]]
    auto_repair: bool
    auto_upgrade: bool
    enabled_autoscaling: bool
    min_node_count: int
    max_node_count: int
    
class PulumiGKEConfig(BaseModel):
    project_id: str
    stack: str
    provider: str
    type: str
    name: str
    zone: str
    region: str
    cluster_name: str
    cluster_type: str
    nodes: NodePool
    
class PulumiGKEYamlConfig(PulumiConfig):
    
    def __init__(self, file_path: str) -> None:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"YAML file not found: {file_path}")

        with open(file_path, 'r') as file:
            self.configs = yaml.safe_load(file)

        self.config_model = PulumiGKEConfig(**self.configs)
        self.validate_yaml()
        
        super().__init__(file_path)

    def validate_yaml(self):
        # Use self.config_model for validation
        pass


