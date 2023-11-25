from client.nextflow_tower_api_client import AuthenticatedClient
import os


class AuthenticatedPlatformClient():
    def __init__(self, platform_token=None, platform_url=None):
        self.platform_token = platform_token or os.getenv('PLATFORM_TOKEN')
        self.platform_url = platform_url or os.getenv('PLATFORM_URL')

        # Check if both platform_token and platform_url are provided or available through environment variables
        if not self.platform_token or not self.platform_url:
            raise ValueError("Both platform_token and platform_url are required.")

        self.client = AuthenticatedClient(token=self.platform_token, base_url=self.platform_url)
