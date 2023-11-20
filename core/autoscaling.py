
class AutoscalingWrapperInterface():

    def get_autoscaling_activity(self):
     pass


class AutoscalingWrapper(AutoscalingWrapperInterface):
    
    def __init__(self, autoscaling_client):
        """Initlizaes autoscaling_client for AWS

        Args:
            autoscaling_client (_type_): Takes an instance of the boto3 autoscaling client
        """
        self.autoscaling_client = autoscaling_client
    
    
    def get_autoscaling_activity(self, autoscaling_group_id: str) -> str:
        try:
            # autoscaling_activity = self.autoscaling_client.describe_scaling_activities(autoscaling_group_id)
            # return autoscaling_activity
            auto_scaling_groups = self.autoscaling_client.describe_auto_scaling_groups(AutoScalingGroupNames=[autoscaling_group_id])
            return auto_scaling_groups
        except Exception as e:
            return(f'An error occured getting the autoscaling group' + str(e))