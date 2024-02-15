from typing import List, Optional
from pydantic import BaseModel

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
    