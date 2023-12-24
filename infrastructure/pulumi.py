
from typing import Any
import pulumi
import pulumi_gcp as gcp
from pulumi import automation 
    
class PulumiGCPInterface():
    pass 

        
class PulumiGCP(PulumiGCPInterface):
    def pulumi_program():

        # Creates a GCP storage bucket with the specified name
        bucket = gcp.storage.Bucket('shahbaz-pulumi-bucket',
                                    name='shahbaz-pulumi', location='us-east1', project='')

        # Export the bucket's URL
        pulumi.export('bucket_url', bucket.url)


class PulumiExecutionInterface():
    
    def up():
        pass
    
    def destroy():
        pass

class PulumiExecution(PulumiExecutionInterface):
    
    def execute_gcp():
        project_name = ""
        stack_name = "dev"
        
        project_settings = automation.ProjectSettings(
            name=project_name,
            runtime='python',
        )
        stack = automation.create_or_select_stack(stack_name=stack_name,
                                    project_name=project_name,
                                    program=PulumiGCP.pulumi_program)
        stack.workspace.install_plugin("gcp", "v7.3.1")
        up_res = stack.up(on_output=print)
        
    def destroy():
         
        project_name = ''
        stack_name = 'dev'
        
        project_settings = automation.ProjectSettings(
            name=project_name,
            runtime='python',
        )
        stack = automation.create_or_select_stack(stack_name=stack_name,
                                    project_name=project_name,
                                    program=PulumiGCP.pulumi_program)
        
        stack.destroy(on_output=print)



        