class EC2ClientWrapperInterface():
    def getLaunchTemplate(self, launch_template_id: str) -> list:
        pass


class EC2ClientWrapper():
    
    def __init__(self, ec2_client):
        self.ec2_client = ec2_client
    
    def getLaunchTemplate(self, launch_template_id: str) -> list:
        
        response = []
        
        try:
            paginator = self.ec2_client.get_paginator('describe_launch_template_versions')
            response_iterator = paginator.paginate(
                LaunchTemplateId=launch_template_id,
                PaginationConfig={
                    'MaxItems': 123,
                    'PageSize': 123
                }
            )
            response += response_iterator
        except Exception as e:
            print(f"An error occurred while retrieving the launch templates: {str(e)}")
            return None   
        return response
    
