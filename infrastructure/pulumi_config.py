import os
import yaml

from .models.config import MinimalPulumiGCPConfig, StandardPulumiGCPConfig, PulumiGKEConfig

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


