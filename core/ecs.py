class ECSWrapperInterface():
    def get_ecs_cluster(self, compute_env_id: str) -> str:
        pass

class ECSWrapper(ECSWrapperInterface):
    def __init__(self, ecs_client):
        self.ecs_client = ecs_client
    
    def get_ecs_cluster(self, compute_env_id: str) -> str:
        if compute_env_id:
            all_clusters = self.ecs_client.list_clusters()
            cluster_arns = all_clusters.get('clusterArns', [])
            if cluster_arns:
                for cluster in cluster_arns:
                    if compute_env_id in cluster :
                        result = self.ecs_client.describe_clusters(clusters=[cluster])
                        return result
                    # else: 
                    #     print ("No ECS clusters found matching ID")
            else:
                raise "No ECS clusters found"
            
        
        
                        
            
            