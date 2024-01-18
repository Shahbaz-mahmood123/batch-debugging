import pulumi
import pulumi_gcp as gcp 
from pulumi_infra_config import PulumiInfraConfig

class PulumiGKEInterface():
    
    def get_secrets(self):
        pass

class PulumiGKE(PulumiInfraConfig, PulumiGKEInterface):
    
    def __init__(self, project_id: str, name: str, region:str , zone: str, cluster_name: str, cluster_type: str, nodes: dict,
                 min_node_count: int, max_node_count: int) -> None:
        self.project_id = project_id 
        self.name = name
        self.region = region 
        self.zone = zone
        self.cluster_name = cluster_name
        self.cluster_type = cluster_type
        self.min_node_count = min_node_count
        self.min_node_count = max_node_count
        self.nodes = nodes 
        
    def pulumi_program(self):        
        
        # Create a VPC 
        network = gcp.compute.Network(f'{self.name}-vpc',
                                      auto_create_subnetworks=False, # We have more control over the network topology when this is False
                                      project = self.project_id)
        
        pulumi.export('network_id', network.id)

        # Create a GCP subnet
        subnet = gcp.compute.Subnetwork(f'{self.name}-subnet',
                                ip_cidr_range="10.2.0.0/16",
                                network=network.id,
                                region=self.region, 
                                project = self.project_id
                                )
        
        gke_cluster = gcp.container.Cluster(
            self.cluster_name,
            network=network.id,
            subnetwork=subnet.id,
            # Define the node config for the cluster
            node_config=gcp.container.ClusterNodeConfigArgs(
                machine_type="n1-standard-1",  # Standard machine type
                oauth_scopes=[
                    "https://www.googleapis.com/auth/compute",
                    "https://www.googleapis.com/auth/devstorage.read_only",
                    "https://www.googleapis.com/auth/logging.write",
                    "https://www.googleapis.com/auth/monitoring"
                ],
            ),
            remove_default_node_pool=True,
            # Define the location for the cluster
            location=self.region
        )

        # Create a custom node pool attached to the GKE cluster created above.
        custom_node_pool = gcp.container.NodePool("my-custom-node-pool",
            location=gke_cluster.location,
            cluster=gke_cluster.name,
            initial_node_count=1,
            network = network.id,
            subnetwork=subnet.id,
            node_config=gcp.container.NodePoolNodeConfigArgs(
                machine_type="n1-standard-1", # Specify the machine type for the nodes.
            ),
            autoscaling=gcp.container.NodePoolAutoscalingArgs(
                min_node_count=self.min_node_count,
                max_node_count=self.max_node_count,
            ),
            management=gcp.container.NodePoolManagementArgs(
                auto_repair=True,
                auto_upgrade=True
            ))
        # Export the Cluster Name
        pulumi.export("cluster_name", gke_cluster.name)
        # Export the Cluster Endpoint
        pulumi.export("cluster_endpoint", gke_cluster.endpoint)
        # Export the Cluster Master Version
        pulumi.export("cluster_master_version", gke_cluster.master_version)
            
    def get_secrets(self):
        pass