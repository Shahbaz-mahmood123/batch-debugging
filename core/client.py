from client.nextflow_tower_api_client import AuthenticatedClient
from client.nextflow_tower_api_client import errors
from core import AuthenticatedTowerClientInterface


class AuthenticatedTowerClient():
    def __init__(self, client: AuthenticatedClient):
        self.client = client
