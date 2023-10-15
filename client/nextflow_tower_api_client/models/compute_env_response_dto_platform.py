from enum import Enum


class ComputeEnvResponseDtoPlatform(str, Enum):
    ALTAIR_PLATFORM = "altair-platform"
    AWS_BATCH = "aws-batch"
    AZURE_BATCH = "azure-batch"
    EKS_PLATFORM = "eks-platform"
    GKE_PLATFORM = "gke-platform"
    GOOGLE_BATCH = "google-batch"
    GOOGLE_LIFESCIENCES = "google-lifesciences"
    K8S_PLATFORM = "k8s-platform"
    LSF_PLATFORM = "lsf-platform"
    SLURM_PLATFORM = "slurm-platform"
    UGE_PLATFORM = "uge-platform"

    def __str__(self) -> str:
        return str(self.value)
