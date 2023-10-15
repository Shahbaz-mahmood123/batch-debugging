from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pod_cleanup_policy import PodCleanupPolicy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_env_variable import ConfigEnvVariable


T = TypeVar("T", bound="KubernetesComputeConfiguration")


@_attrs_define
class KubernetesComputeConfiguration:
    """
    Attributes:
        work_dir (Union[Unset, str]):
        pre_run_script (Union[Unset, str]):
        post_run_script (Union[Unset, str]):
        server (Union[Unset, str]):
        ssl_cert (Union[Unset, str]):
        namespace (Union[Unset, str]):
        compute_service_account (Union[Unset, str]):
        head_service_account (Union[Unset, str]):
        storage_claim_name (Union[Unset, str]):
        storage_mount_path (Union[Unset, str]):
        pod_cleanup (Union[Unset, PodCleanupPolicy]):
        head_pod_spec (Union[Unset, str]):
        service_pod_spec (Union[Unset, str]):
        environment (Union[Unset, List['ConfigEnvVariable']]):
        head_job_cpus (Union[Unset, int]):
        head_job_memory_mb (Union[Unset, int]):
        discriminator (Union[Unset, str]): property to select the compute config platform
    """

    work_dir: Union[Unset, str] = UNSET
    pre_run_script: Union[Unset, str] = UNSET
    post_run_script: Union[Unset, str] = UNSET
    server: Union[Unset, str] = UNSET
    ssl_cert: Union[Unset, str] = UNSET
    namespace: Union[Unset, str] = UNSET
    compute_service_account: Union[Unset, str] = UNSET
    head_service_account: Union[Unset, str] = UNSET
    storage_claim_name: Union[Unset, str] = UNSET
    storage_mount_path: Union[Unset, str] = UNSET
    pod_cleanup: Union[Unset, PodCleanupPolicy] = UNSET
    head_pod_spec: Union[Unset, str] = UNSET
    service_pod_spec: Union[Unset, str] = UNSET
    environment: Union[Unset, List["ConfigEnvVariable"]] = UNSET
    head_job_cpus: Union[Unset, int] = UNSET
    head_job_memory_mb: Union[Unset, int] = UNSET
    discriminator: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        work_dir = self.work_dir
        pre_run_script = self.pre_run_script
        post_run_script = self.post_run_script
        server = self.server
        ssl_cert = self.ssl_cert
        namespace = self.namespace
        compute_service_account = self.compute_service_account
        head_service_account = self.head_service_account
        storage_claim_name = self.storage_claim_name
        storage_mount_path = self.storage_mount_path
        pod_cleanup: Union[Unset, str] = UNSET
        if not isinstance(self.pod_cleanup, Unset):
            pod_cleanup = self.pod_cleanup.value

        head_pod_spec = self.head_pod_spec
        service_pod_spec = self.service_pod_spec
        environment: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.environment, Unset):
            environment = []
            for environment_item_data in self.environment:
                environment_item = environment_item_data.to_dict()

                environment.append(environment_item)

        head_job_cpus = self.head_job_cpus
        head_job_memory_mb = self.head_job_memory_mb
        discriminator = self.discriminator

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if work_dir is not UNSET:
            field_dict["workDir"] = work_dir
        if pre_run_script is not UNSET:
            field_dict["preRunScript"] = pre_run_script
        if post_run_script is not UNSET:
            field_dict["postRunScript"] = post_run_script
        if server is not UNSET:
            field_dict["server"] = server
        if ssl_cert is not UNSET:
            field_dict["sslCert"] = ssl_cert
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if compute_service_account is not UNSET:
            field_dict["computeServiceAccount"] = compute_service_account
        if head_service_account is not UNSET:
            field_dict["headServiceAccount"] = head_service_account
        if storage_claim_name is not UNSET:
            field_dict["storageClaimName"] = storage_claim_name
        if storage_mount_path is not UNSET:
            field_dict["storageMountPath"] = storage_mount_path
        if pod_cleanup is not UNSET:
            field_dict["podCleanup"] = pod_cleanup
        if head_pod_spec is not UNSET:
            field_dict["headPodSpec"] = head_pod_spec
        if service_pod_spec is not UNSET:
            field_dict["servicePodSpec"] = service_pod_spec
        if environment is not UNSET:
            field_dict["environment"] = environment
        if head_job_cpus is not UNSET:
            field_dict["headJobCpus"] = head_job_cpus
        if head_job_memory_mb is not UNSET:
            field_dict["headJobMemoryMb"] = head_job_memory_mb
        if discriminator is not UNSET:
            field_dict["discriminator"] = discriminator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.config_env_variable import ConfigEnvVariable

        d = src_dict.copy()
        work_dir = d.pop("workDir", UNSET)

        pre_run_script = d.pop("preRunScript", UNSET)

        post_run_script = d.pop("postRunScript", UNSET)

        server = d.pop("server", UNSET)

        ssl_cert = d.pop("sslCert", UNSET)

        namespace = d.pop("namespace", UNSET)

        compute_service_account = d.pop("computeServiceAccount", UNSET)

        head_service_account = d.pop("headServiceAccount", UNSET)

        storage_claim_name = d.pop("storageClaimName", UNSET)

        storage_mount_path = d.pop("storageMountPath", UNSET)

        _pod_cleanup = d.pop("podCleanup", UNSET)
        pod_cleanup: Union[Unset, PodCleanupPolicy]
        if isinstance(_pod_cleanup, Unset):
            pod_cleanup = UNSET
        else:
            pod_cleanup = PodCleanupPolicy(_pod_cleanup)

        head_pod_spec = d.pop("headPodSpec", UNSET)

        service_pod_spec = d.pop("servicePodSpec", UNSET)

        environment = []
        _environment = d.pop("environment", UNSET)
        for environment_item_data in _environment or []:
            environment_item = ConfigEnvVariable.from_dict(environment_item_data)

            environment.append(environment_item)

        head_job_cpus = d.pop("headJobCpus", UNSET)

        head_job_memory_mb = d.pop("headJobMemoryMb", UNSET)

        discriminator = d.pop("discriminator", UNSET)

        kubernetes_compute_configuration = cls(
            work_dir=work_dir,
            pre_run_script=pre_run_script,
            post_run_script=post_run_script,
            server=server,
            ssl_cert=ssl_cert,
            namespace=namespace,
            compute_service_account=compute_service_account,
            head_service_account=head_service_account,
            storage_claim_name=storage_claim_name,
            storage_mount_path=storage_mount_path,
            pod_cleanup=pod_cleanup,
            head_pod_spec=head_pod_spec,
            service_pod_spec=service_pod_spec,
            environment=environment,
            head_job_cpus=head_job_cpus,
            head_job_memory_mb=head_job_memory_mb,
            discriminator=discriminator,
        )

        kubernetes_compute_configuration.additional_properties = d
        return kubernetes_compute_configuration

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
