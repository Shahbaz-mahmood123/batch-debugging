import os
import yaml

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
        
class MinimalPulumiGCPConfig(PulumiConfig):
    
    def __init__(self, file_path: str) -> None:
        
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"YAML file not found: {file_path}")

        with open(file_path, 'r') as file:
            self.configs = yaml.safe_load(file) 
        
        self.location = self.configs['location']
        self.resource_name = self.configs['name']
        self.project_id = self.configs['project_id']
        self.zone = self.configs['zone']
        self.region = self.configs['region']
        self.instance_name = self.configs['instance_name']
        self.tower_env_secret = self.configs.get('secrets', {}).get('tower_env_secret', []) 
        self.tower_yaml_secret = self.configs.get('secrets', {}).get('tower_yaml_secret', []) 
        self.harbor_creds = self.configs.get('secrets', {}).get('harbor_creds', [])  
        self.groundswell_secret = self.configs.get('secrets', {}).get('groundswell_secret', []) 
        self.source_ranges = self.configs.get('network', {}).get('source_ranges', [])
        self.tags = self.configs.get('compute-engine', {}).get('tags', [])
        self.source_tags = self.configs.get('network', {}).get('tags', [])

        super().__init__(file_path)
    
    ##TODO: Need to do some validation on the yaml maybe? 
    def validate_yaml(self):
        pass
    
class StandardMinimalPulumiGCPConfig(PulumiConfig):
    
    def __init__(self, file_path: str) -> None:
        
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"YAML file not found: {file_path}")

        with open(file_path, 'r') as file:
            self.configs = yaml.safe_load(file) 
        
        self.location = self.configs['location']
        self.resource_name = self.configs['name']
        self.project_id = self.configs['project_id']
        self.zone = self.configs['zone']
        self.region = self.configs['region']
        self.instance_name = self.configs['instance_name']
        self.tower_env_secret = self.configs.get('secrets', {}).get('tower_env_secret', []) 
        self.tower_yaml_secret = self.configs.get('secrets', {}).get('tower_yaml_secret', []) 
        self.harbor_creds = self.configs.get('secrets', {}).get('harbor_creds', [])  
        self.groundswell_secret = self.configs.get('secrets', {}).get('groundswell_secret', []) 
        self.source_ranges = self.configs.get('network', {}).get('source_ranges', [])
        self.tags = self.configs.get('compute-engine', {}).get('tags', [])
        self.source_tags = self.configs.get('network', {}).get('tags', [])

        super().__init__(file_path)
    
    ##TODO: Need to do some validation on the yaml maybe? 
    def validate_yaml(self):
        pass
    
class PulumiGKEConfig(PulumiConfig):
    
    def __init__(self, file_path: str) -> None:
        self.resource_name = self.configs['name']
        self.project_id = self.configs['project_id']
        self.zone = self.configs['zone']
        self.region = self.configs['region']
        self.cluster_name = self.configs['cluster_name']
        self.cluster_type = self.configs['cluster_type']
        self.min_node_count = self.configs['min_node_count'] 
        self.min_node_count = self.configs['max_node_count']
        self.nodes = self.configs['nodes'] 
        super().__init__(file_path)
        
        ##TODO: Need to do some validation on the yaml maybe? 
        def validate_yaml(self):
            pass