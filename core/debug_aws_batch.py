import base64
import boto3
import json
from core.client import AuthenticatedTowerClient
from core.ec2 import EC2ClientWrapper
from core.aws_batch import AWSBatchClientWrapper
from core.compute_envs import SeqeraComputeEnvsWrapper
from core.autoscaling import AutoscalingWrapper

class DebugAWSBatchInterface:
    def get_tower_compute_envs_id_list(self, workspace_id: str, status: str) -> list:
        pass

    def get_aws_batch_compute_env_launch_template_id(self, compute_env: list) -> list:
        pass

    def get_launch_template(self, lt_id: dict) -> dict:
        pass

    def extract_and_decode_user_data(self, response: dict) -> str:
        pass

    def get_and_extract_user_data(self, lt_id: dict) -> str:
        pass

    def get_user_data_from_launch_template(self, launch_template_id: list) -> str:
        pass
    
    def get_job_queue_status(self, job_queue_id: str) -> str:
        pass
    
    def get_compute_env_status(self, compute_env_id: str) -> str:
        pass
    
    def get_autoscaling_activity(self, autoscaling_group_id: str) -> str:
        pass

class DebugAWSBatch(DebugAWSBatchInterface):
    def __init__(self, authenticated_tower_client: AuthenticatedTowerClient):
        """
        Initializes the DebugAWSBatch class.

        Args:
            authenticated_tower_client (AuthenticatedTowerClient): An instance of AuthenticatedTowerClient.
        """
        self.authenticated_tower_client = authenticated_tower_client

        batch_client = boto3.client('batch', region_name='us-east-1')
        self.aws_batch_client_wrapper = AWSBatchClientWrapper(batch_client)

        ec2_client = boto3.client('ec2', region_name='us-east-1')
        self.ec2_client_wrapper = EC2ClientWrapper(ec2_client)
        
        autoscaling_client = boto3.client ('autoscaling', region_name='us-east-1')
        self.autoscaling_wrapper = AutoscalingWrapper(autoscaling_client)

        self.seqera_compute_envs_wrapper = SeqeraComputeEnvsWrapper(self.authenticated_tower_client)

    def get_tower_compute_envs_id_list(self, workspace_id: str, status: str) -> list:
        """
        Get a list of Tower compute environment IDs.

        Args:
            workspace_id (str): The Seqera platform workspace ID.
            status (str): The status of compute environments to filter.

        Returns:
            list: A list of compute environment IDs.
        """
        compute_envs = self.seqera_compute_envs_wrapper.list_compute_envs(workspace_id, status)
        compute_envs_id_list = self.seqera_compute_envs_wrapper.get_compute_env_id(compute_envs)
        
        # Add "TowerForge-" prefix and "-head" suffix to each element in the list
        modified_id_list = [f'ShahbazCompute-{env_id}-head' for env_id in compute_envs_id_list]
        return modified_id_list

    def get_aws_batch_compute_env_launch_template_id(self, compute_env: list) -> list:
        """
        Get the launch template ID for an AWS Batch compute environment.

        Args:
            compute_env (list): The name of the compute environment in the seqera platform.

        Returns:
            list: The launch templates ID.
        """
        launch_template_id_list = []
        
        compute_env_list = []
        
        compute_env_list = self.aws_batch_client_wrapper.get_batch_compute_env(compute_env)
        
        launch_template_id_list = []
        for compute_environment in compute_env_list.get("computeEnvironments", []):
            launch_template = compute_environment.get("computeResources", {}).get("launchTemplate", {})
            launch_template_id = launch_template.get("launchTemplateId")
            if launch_template_id:
                launch_template_id_list.append(launch_template_id)
                
        return launch_template_id_list
        
    def get_launch_template(self, lt_id: str) -> dict:
        """
        Get information about an AWS Launch Template.

        Args:
            lt_id (str): The ID of the Launch Template.

        Returns:
            dict: Information about the Launch Template.
        """
        response_iterator = self.ec2_client_wrapper.getLaunchTemplate(lt_id)
        for response in response_iterator:
            return response

    def extract_and_decode_user_data(self, response: dict) -> str:
        """
        Extract and decode user data from an AWS Launch Template response.

        Args:
            response (dict): The AWS Launch Template response.

        Returns:
            str: The decoded user data.
        """
        try:
            launch_template_data = response['LaunchTemplateVersions'][0]['LaunchTemplateData']
            user_data_base64 = launch_template_data.get('UserData', '')
            user_data_decoded = base64.b64decode(user_data_base64).decode('utf-8')
            return user_data_decoded
        except Exception as e:
            return str(e)

    def get_and_extract_user_data(self, lt_id: str) -> str:
        """
        Get and extract user data from an AWS Launch Template.

        Args:
            lt_id (str): The ID of the Launch Template.

        Returns:
            str: The extracted and decoded user data.
        """
        try:
            response = self.get_launch_template(lt_id)
            #print(response)
            #user_data = self.extract_and_decode_user_data(response)
            #print(user_data)
            return response
        except Exception as e:
            return str(e)

    def get_user_data_from_launch_template(self, launch_template_ids: list) -> list:
        """
        Get user data from an AWS Launch Template.

        Args:
            launch_template_id (str): The ID of the Launch Template.

        Returns:
            str: The extracted and decoded user data.
        """
        
        
        user_data = []
        
        if not isinstance(launch_template_ids, list):
            # If launch_template_ids is not a list, wrap it in a list to handle single string inputs.
            launch_template_ids = [launch_template_ids]
            
        for id in launch_template_ids:
            response = self.get_and_extract_user_data(id)
            user_data.append(response)
        return user_data
        
        
    def get_job_queue_status(self, job_queue_id: str) -> str:
        """ 
        returns the current status a job queue in AWS Batch
        Args:
            job_queue_id (str): the ID of the job queue you want to chekc
        Returns:
            str: The current status of the job queue and any tasks running 
            in the job queue
        """
        
        try:
            job_queue_response = self.aws_batch_client_wrapper.get_job_queue(job_queue_id)
            job_queue_info = job_queue_response.get('jobQueues', [])

            if job_queue_info:
                job_queue_info = job_queue_info[0]  
                arn = job_queue_info.get('jobQueueArn', '')
                state = job_queue_info.get('state', '')
                status = job_queue_info.get('status', '')
                status_and_state = (f"Job Queue arn: {arn}, State: {state}, Status: {status}")
                return status_and_state
            else:
                return ('error getting job queue:' + job_queue_response)

        except Exception as e:
            return str(e)
        
        
    def get_compute_env_status(self, compute_env_id: str) -> str:
        """ Get the current status of a compute enviornment

        Args:
            compute_env_id (str): ID of an AWS batch compute env ID

        Returns:
            str: The current status of AWS batch compute env
        """
        
        try: 
            aws_batch_ce_response = self.aws_batch_client_wrapper.get_batch_compute_env(compute_env_id)
          
            ce_info =  aws_batch_ce_response.get('computeEnvironments', [])
            
            if ce_info:
                ce_info = ce_info[0]
                state = ce_info.get('state', '')
                status = ce_info.get('status', '')
                arn = ce_info.get('computeEnvironmentArn', '')
                status_and_state = (f"Job Queue arn: {arn}, State: {state}, Status: {status}")
                return status_and_state
        except Exception as e:
            return str(e)
        
    def get_autoscaling_activity(self, autoscaling_group_id: str) -> str:
        """ Get autoscaling group activity details.

        Args:
            autoscaling_group_id (str): ID of autoscaling group in EC2.

        Returns:
            str: returns acitvity details of an autoscaling group in
        """
        try: 
            response = self.autoscaling_wrapper.get_all_autoscaling_groups(autoscaling_group_id)
            return response
        except Exception as e:
            return(f'An error occured when fetching the autoscaling group ' + str(e))
        
    
    