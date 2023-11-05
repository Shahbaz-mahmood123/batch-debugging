import base64
import boto3
from core.client import AuthenticatedTowerClient
from core.ec2 import EC2ClientWrapper
from core.aws_batch import AWSBatchClientWrapper
from core.compute_envs import SeqeraComputeEnvsWrapper

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
        print(response)
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
        print(lt_id)
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
        
