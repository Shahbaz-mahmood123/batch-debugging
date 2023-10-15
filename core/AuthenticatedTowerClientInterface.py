from client.nextflow_tower_api_client import AuthenticatedClient, client

class AuthenticatedTowerClientInterface():
    """Interface for Nextflow Tower client authenticated with API token."""

    _client: AuthenticatedClient

