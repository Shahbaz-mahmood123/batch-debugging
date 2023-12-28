import yaml

class PulumiConfigInterface():
    def validate_yaml(self):
        pass

class PulumiConfig(PulumiConfigInterface):
    
    def __init__(self, file_path: str) -> None:
        
        with open(file_path, 'r') as file:
            configs = yaml.safe_load(file) 
        
        self.stack_name = configs['stack']
        
    def validate_yaml(self):
        pass
        
class PulumiGCPConfig(PulumiConfig):
    
    def __init__(self, file_path: str) -> None:
        
        with open(file_path, 'r') as file:
            self.configs = yaml.safe_load(file) 
        
        self.location = self.configs['location']
        self.resource_name = self.configs['name']
        self.project_id = self.configs['project_id']
        self.zone = self.configs['zone']
        self.region = self.configs['region']
        self.instance_name = self.configs['instance_name']
        
        super().__init__(file_path)

class PulumiGKEConfig(PulumiConfig):
    
    def __init__(self, file_path: str) -> None:
        self.resource_name = self.configs['name']
        self.project_id = self.configs['project_id']
        self.zone = self.configs['zone']
        self.region = self.configs['region']
        self.cluster_name = self.configs['cluster_name']
        super().__init__(file_path)