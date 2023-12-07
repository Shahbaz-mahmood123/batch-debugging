class CloudWatchInterface():
    def get_cloudwatch_logs(log_prefix: str) -> dict:
        pass

class CloudWatch(CloudWatchInterface):
    def __init__(self, cloudwatch_client):
        self.cloudwatch_client = cloudwatch_client
    
    def get_cloudwatch_logs(log_prefix: str) -> dict:
        pass
    