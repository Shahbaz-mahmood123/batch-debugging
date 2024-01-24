import os

import pulumi
import pulumi_gcp as gcp
from pulumi import automation 
from pulumi.automation import LocalWorkspace, LocalWorkspaceOptions, ProjectBackend
from infrastructure.pulumi_infra_config import PulumiInfraConfig


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
    
    def __init__(self,project_id: str, stack_name: str, work_dir: str, infra: PulumiInfraConfig) -> None:
        self.project_id = project_id or os.getenv("GCP_PROJECT_ID")
        self.runtime = 'python'
        self.stack_name = stack_name
        self.work_dir = work_dir
        #Not idea why but setting the backendurl like this makes pulumi prompt for the access token...
        #backend_url = self.work_dir
        
        self.project_settings =  automation.ProjectSettings(
            name=self.project_id,
            runtime=self.runtime,
            ##TODO: Use other backend options for example gcp cloud storage, s3 etc.
            #https://www.pulumi.com/docs/cli/commands/pulumi_login/
            backend=ProjectBackend(url=f"file://{self.work_dir}")
        )
        self.pulumi_program = infra.pulumi_program
        self.stack = automation.create_or_select_stack(stack_name=self.stack_name,
                            project_name=self.project_id,
                            program=self.pulumi_program,
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
        
    def destroy_stack(self):
        self.stack.destroy(on_output=print)
    
        