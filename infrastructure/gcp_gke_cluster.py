from pydantic import BaseModel

import pulumi
import pulumi_gcp as gcp 
import pulumi_kubernetes as k8s

from .pulumi_infra_config import PulumiInfraConfig
from .pulumi_config import PulumiGKEConfig

# Pydantic model for Node Pool Management
class Management(BaseModel):
    autoRepair: bool
    autoUpgrade: bool
    
class PulumiGKEInterface():
    
    def get_secrets(self):
        pass

class PulumiGKE(PulumiInfraConfig, PulumiGKEInterface):
    
    def __init__(self, config: PulumiGKEConfig) -> None:
        self.project_id = config.project_id 
        self.name = config.name
        self.region = config.region 
        self.zone = config.zone
        self.cluster_name = config.cluster_name
        self.cluster_type = config.cluster_type
        self.nodes = config.nodes 

        
    def pulumi_program(self):        
        
        # Create a VPC 
        network = gcp.compute.Network(f'{self.name}-vpc',
                                      auto_create_subnetworks=False, # We have more control over the network topology when this is False
                                      project = self.project_id)
        
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
            initial_node_count = 1,
            remove_default_node_pool=True,
            # Define the location for the cluster
            location=self.region,
            project = self.project_id
        )

        # Create a custom node pool attached to the GKE cluster created above.
        custom_node_pool = gcp.container.NodePool(self.nodes.name,
            location=gke_cluster.location,
            cluster=gke_cluster.name,
            initial_node_count=self.nodes.initial_node_count,
            project = self.project_id,
            # network = network.id,
            # subnetwork=subnet.id,
            node_config=gcp.container.NodePoolNodeConfigArgs(
                machine_type=self.nodes.machine_type, # Specify the machine type for the nodes.
            ),
            autoscaling=gcp.container.NodePoolAutoscalingArgs(
                min_node_count=self.nodes.min_node_count,
                max_node_count=self.nodes.max_node_count,
            ),
            management=gcp.container.NodePoolManagementArgs(
                auto_repair=self.nodes.auto_repair,
                auto_upgrade=self.nodes.auto_upgrade
            ))
        
        # A Kubernetes provider to apply resources to the created GKE cluster
        # Create a Kubernetes provider to use the cluster kubeconfig
        k8s_info = pulumi.Output.all(gke_cluster.name, gke_cluster.endpoint, gke_cluster.master_auth)
        k8s_config = k8s_info.apply(
            lambda info: """apiVersion: v1
        clusters:
        - cluster:
            certificate-authority-data: {0}
            server: https://{1}
        name: {2}
        contexts:
        - context:
            cluster: {2}
            user: {2}
        name: {2}
        current-context: {2}
        kind: Config
        preferences: {{}}
        users:
        - name: {2}
        user:
            exec:
            apiVersion: client.authentication.k8s.io/v1beta1
            command: gke-gcloud-auth-plugin
            installHint: Install gke-gcloud-auth-plugin for use with kubectl by following
                https://cloud.google.com/blog/products/containers-kubernetes/kubectl-auth-changes-in-gke
            provideClusterInfo: true
        """.format(info[2]['cluster_ca_certificate'], info[1], '{0}_{1}_{2}'.format(self.project, self.zone, info[0])))

        # Make a Kubernetes provider instance that uses our cluster from above.
        k8s_provider = k8s.Provider('gke_k8s', kubeconfig=k8s_config)
        
        tower_launcher_manifest = k8s.yaml.ConfigFile("k8s-manifest", file="./tower-launcher.yaml")
        
        # Create a new GCP service account
        service_account = gcp.serviceaccount.Account(f"{self.name}-sa]",
                                                     account_id=f"pulumiserviceaccount",
                                                     display_name=f"{self.name} Service Account",
                                                     project = self.project_id)

        # Define the roles you want to assign to the service account
        roles_list = ["roles/container.admin"]

        # Assign the roles to the service account
        for role in roles_list:
            iam_binding = gcp.serviceaccount.IAMBinding(f"service-account-iam-{role}",
                                                        service_account_id=service_account.name,
                                                        role=role,
                                                        members=[f"serviceAccount:{service_account.email}"]
                                                        )

        # Create a service account key
        service_account_key = gcp.serviceaccount.Key(f"{self.name}-key]",
                                                     service_account_id=service_account.name
                                                     )

        # Export the service account email and the path to the generated key file
        pulumi.export("service_account_email", service_account.email)
        
        pulumi.export("service_account_key_path", service_account_key.private_key.apply(lambda key: key.path if key else None))

        pulumi.export('network_id', network.id)
        # Export the Cluster Name
        pulumi.export("cluster_name", gke_cluster.name)
        # Export the Cluster Endpoint
        pulumi.export("cluster_endpoint", gke_cluster.endpoint)
        # Export the Cluster Master Version
        pulumi.export("cluster_master_version", gke_cluster.master_version)
        
        #pulumi.export("resource_names", tower_launcher_manifest.urn)
            
    def get_secrets(self):
        pass