class AWSQuotasInterface():
    pass

class AWSQuotas(AWSQuotasInterface):
    def __init__(self, quotas_client):
        self.quotas_client = quotas_client
    
    