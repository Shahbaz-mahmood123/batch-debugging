import os

import pulumi
import pulumi_gcp as gcp
from pulumi import automation 
from pulumi.automation import LocalWorkspace, LocalWorkspaceOptions, ProjectBackend
from infrastructure.gcp_compute_engine import PulumiInfraConfig


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
    
    def __init__(self,project_id: str, stack_name: str, work_dir: str, pulumi_program: PulumiInfraConfig) -> None:
        self.project_id = project_id or os.getenv("GCP_PROJECT_ID")
        self.runtime = 'python'
        self.stack_name = stack_name
        self.work_dir = work_dir
        #backend_url = ProjectBackend(f'file://{work_dir}')
        
        self.project_settings =  automation.ProjectSettings(
            name=self.project_id,
            runtime=self.runtime,
            #backend=backend_url
        )
        self.pulumi_program = pulumi_program
        
        self.stack = automation.create_or_select_stack(stack_name=self.stack_name,
                            project_name=self.project_id,
                            program=self.pulumi_program.pulumi_program,
                            opts=LocalWorkspaceOptions(
                                        #secrets_provider=SECRET_PROVIDER,
                                        #The PULUMI_CONFIG_PASSPHRASE since pulumi stack is encrypted by default
                                        env_vars = {'PULUMI_CONFIG_PASSPHRASE': self.stack_name},
                                        work_dir=self.work_dir,
                                        project_settings=self.project_settings))
        
        self.stack.workspace.install_plugin("gcp", "v7.3.1")
        
    def execute(self):
        self.stack.up(on_output=print)
        
    def destroy(self):
        self.stack.destroy(on_output=print)
        
    def preview(self):
        self.stack.preview(on_output=print)
    
    def refresh(self):
        self.stack.refresh(on_output=print)
        
    def cancel(self):
        self.stack.cancel()
    
        