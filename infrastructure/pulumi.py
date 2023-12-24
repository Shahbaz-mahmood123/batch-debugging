import os

import pulumi
import pulumi_gcp as gcp
from pulumi import automation 

from infrastructure.gcp_compute_engine import PulumiGCP


class PulumiExecutionInterface():
    
    def up():
        pass
    
    def destroy():
        pass

class PulumiExecution(PulumiExecutionInterface):
    
    def __init__(self,project_id: str, stack_name: str, pulumi_gcp = PulumiGCP) -> None:
        self.project_id = project_id or os.getenv("GCP_PROJECT_ID")
        self.runtime = 'python'
        self.stack_name = stack_name
        
        self.project_settings =  automation.ProjectSettings(
            name=self.project_id,
            runtime=self.runtime,
        )
        self.pulumi_gcp = pulumi_gcp
        
    def execute_gcp(self):
        stack = automation.create_or_select_stack(stack_name=self.stack_name,
                                    project_name=self.project_id,
                                    program=self.pulumi_gcp.pulumi_program)
        stack.workspace.install_plugin("gcp", "v7.3.1")
        up_res = stack.up(on_output=print)
        
    def destroy(self):
        
        stack = automation.create_or_select_stack(stack_name=self.stack_name,
                                    project_name=self.project_id,
                                    program=self.pulumi_gcp.pulumi_program)
        
        stack.destroy(on_output=print)
        