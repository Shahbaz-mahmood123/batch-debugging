from client.nextflow_tower_api_client import AuthenticatedClient
from client.nextflow_tower_api_client.api.default import list_compute_envs
from client.nextflow_tower_api_client.models.list_compute_envs_response import ListComputeEnvsResponse

from core.client  import AuthenticatedTowerClient

import json 

class ComputeEnvs():
    
    def __init__(self, client: AuthenticatedTowerClient):
        self.client = client

    def listComputeEnvs(self, workspace_id: int, status: str):
    
        computeEnvJsonList: [ListComputeEnvsResponse] = list_compute_envs.sync(client=self.client, workspace_id=workspace_id, status= status)

        return computeEnvJsonList
    
    
    def getComputeEnvId(self, computeEnvList: [ListComputeEnvsResponse]):
    
        id_list = [compute_env.id for compute_env in computeEnvList.compute_envs]
    
        return id_list
    