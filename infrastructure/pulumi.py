import os

import pulumi
import pulumi_gcp as gcp
from pulumi import automation 

from infrastructure.gcp_compute_engine import PulumiGCP, PulumiInfraConfig


class PulumiExecutionInterface():
    
    def execute(self):
        pass
        
    def destroy(self):
        pass
        
    def preview(self):
        pass
    
    def refresh(self):
        pass
    
class PulumiExecution(PulumiExecutionInterface):
    
    def __init__(self,project_id: str, stack_name: str, pulumi_gcp = PulumiInfraConfig) -> None:
        self.project_id = project_id or os.getenv("GCP_PROJECT_ID")
        self.runtime = 'python'
        self.stack_name = stack_name
        
        self.project_settings =  automation.ProjectSettings(
            name=self.project_id,
            runtime=self.runtime,
        )
        self.pulumi_gcp = pulumi_gcp
        
        self.stack = automation.create_or_select_stack(stack_name=self.stack_name,
                            project_name=self.project_id,
                            program=self.pulumi_gcp.pulumi_program)
        
        self.stack.workspace.install_plugin("gcp", "v7.3.1")
        
    def execute(self):
        self.stack.up(on_output=print)
        
    def destroy(self):
        self.stack.destroy(on_output=print)
        
    def preview(self):
        self.stack.preview(on_output=print)
    
    def refresh(self):
        self.stack.refresh(on_output=print)
    
        