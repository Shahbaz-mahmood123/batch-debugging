import boto3

class AWSBatchClientWrapperInterface:
    def get_job_queue(self, queue_name: str) -> dict:
        pass

    def get_batch_compute_env(self, compute_env: str) -> dict:
        pass
    
    def get_jobs(self, job_queue_id: str) -> dict:
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
            return {"ERROR": e}
            

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
            return {"ERROR": e}

    def compare_auto_scaling_group(api_response, target_string):
        auto_scaling_groups = api_response.get('AutoScalingGroups', [])
        
        for group in auto_scaling_groups:
            auto_scaling_group_name = group.get('AutoScalingGroupName', '')
            
            # Compare the AutoScalingGroupName up to the point where "work" appears
            if auto_scaling_group_name.startswith(target_string):
                print(f"Match found for {target_string}")
                break
        else:
            return {"No match found for": target_string}
    
    #https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/client/list_jobs.html
    def get_jobs(self, job_queue_id: str, job_status: str) -> dict:
        """ Get the five most recent jobs from a specified job queue. 

        Args:
            job_queue_id (str): The job queue name or fully qualified  AWS arn.
            job_status   (str): The status of the job to retrieve. Accepted values: 
                                'SUBMITTED'|'PENDING'|'RUNNABLE'|'STARTING'|'RUNNING'|'SUCCEEDED'|'FAILED'
        Returns:
            dict: returns 5 most recent jobs.
        """
        try:
            job_response = self.batch_client.list_jobs(jobQueue=job_queue_id, maxResults=5, jobStatus=job_status)
            job_summary_list = job_response.get("jobSummaryList", [])
            if job_summary_list == []:
                return f"No jobs with the status of {job_status} found"
        except Exception as e:
            return ["ERROR", e] 
        return job_response
            
        