import boto3


class AWSBatchClient():
    
    def __init__(self, batch_client):
        self.batch_client = batch_client
    
    def getJobQueue(self, queueName: str):
        
        response = self.batch_client.describe_job_queues(jobQueues=[queueName])
        return response
    
    def getComputeEnv(self, computeEnv: str):
        
        response = self.batch_client.describe_compute_environments(computeEnvs=[computeEnv])
        return response
        
    
    
     