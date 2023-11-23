
class AutoscalingWrapperInterface():

    def get_all_autoscaling_groups(self):
     pass
 
    
    def get_scaling_activities(self, autoscaling_group_name: str) -> dict:
        pass


class AutoscalingWrapper(AutoscalingWrapperInterface):
    
    def __init__(self, autoscaling_client):
        """Initlizaes autoscaling_client for AWS

        Args:
            autoscaling_client (_type_): Takes an instance of the boto3 autoscaling client
        """
        self.autoscaling_client = autoscaling_client
    
    def compare_auto_scaling_group(self, list_of_autoscaling_groups: dict, compute_env_id: str) -> str:
        auto_scaling_groups = list_of_autoscaling_groups.get('AutoScalingGroups', [])
        
        for group in auto_scaling_groups:
            auto_scaling_group = group.get('AutoScalingGroupName', '')
            
            # Compare the AutoScalingGroupName up to the point where "work" appears
            if auto_scaling_group.startswith(compute_env_id):
                print(f"Match found for {compute_env_id}")
                return group
        else:
            print(f"No match found for {compute_env_id}")
    
    def get_all_autoscaling_groups(self, autoscaling_group_id: str) -> str:
        try:
            auto_scaling_groups = self.autoscaling_client.describe_auto_scaling_groups()
            matching_autoscaling_group = self.compare_auto_scaling_group(auto_scaling_groups, autoscaling_group_id)
            return matching_autoscaling_group
        except Exception as e:
            return(f'An error occured getting all the autoscaling groups' + str(e))
        
        
    def get_scaling_activities(self, autoscaling_group_name: str) -> dict:
        try:
            scaling_activity = self.autoscaling_client.describe_scaling_activities(AutoScalingGroupName=autoscaling_group_name)
            return scaling_activity
        except Exception as e:
            return(f'An error occured getting the scaling activities for {autoscaling_group_name}' + str(e))
        
