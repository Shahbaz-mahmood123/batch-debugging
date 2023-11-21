import boto3

class AWSBatchClientWrapperInterface:
    def get_job_queue(self, queue_name: str) -> dict:
        pass

    def get_batch_compute_env(self, compute_env: str) -> dict:
        pass

class AWSBatchClientWrapper(AWSBatchClientWrapperInterface):
    def __init__(self, batch_client):
        """
        Initializes the AWSBatchClientWrapper class.

        Args:
            batch_client: An instance of the AWS Batch client.
        """
        self.batch_client = batch_client

    def get_job_queue(self, queue_name: str) -> dict:
        """
        Get information about an AWS Batch job queue.

        Args:
            queue_name (str): The name of the job queue.

        Returns:
            dict or None: Information about the job queue or None in case of an error.
        """
        try:
            response = self.batch_client.describe_job_queues(jobQueues=[queue_name])
            return response
        except Exception as e:
            print(f"An error occurred while retrieving job queue: {str(e)}")
            return None

    def get_batch_compute_env(self, compute_env: list) -> dict:
        """
        Get information about an AWS Batch compute environment.

        Args:
            compute_env (str): The name of the compute environment.

        Returns:
            dict or None: Information about the compute environment or None in case of an error.
        """
        try:
            response = self.batch_client.describe_compute_environments(computeEnvironments=[compute_env])
            return response
        except Exception as e:
            print(f"An error occurred while retrieving compute environment: {str(e)}")
            return None

    def compare_auto_scaling_group(api_response, target_string):
        auto_scaling_groups = api_response.get('AutoScalingGroups', [])
        
        for group in auto_scaling_groups:
            auto_scaling_group_name = group.get('AutoScalingGroupName', '')
            
            # Compare the AutoScalingGroupName up to the point where "work" appears
            if auto_scaling_group_name.startswith(target_string):
                print(f"Match found for {target_string}")
                # You can perform additional actions here if needed
                break
        else:
            print(f"No match found for {target_string}")