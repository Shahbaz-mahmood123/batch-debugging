from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_env_variable import ConfigEnvVariable
    from ..models.google_batch_service_configuration_labels import GoogleBatchServiceConfigurationLabels


T = TypeVar("T", bound="GoogleBatchServiceConfiguration")


@_attrs_define
class GoogleBatchServiceConfiguration:
    """
    Attributes:
        location (Union[Unset, str]):
        work_dir (Union[Unset, str]):
        spot (Union[Unset, bool]):
        boot_disk_size_gb (Union[Unset, int]):
        cpu_platform (Union[Unset, str]):
        machine_type (Union[Unset, str]):
        project_id (Union[Unset, str]):
        ssh_daemon (Union[Unset, bool]):
        ssh_image (Union[Unset, str]):
        debug_mode (Union[Unset, int]):
        copy_image (Union[Unset, str]):
        use_private_address (Union[Unset, bool]):
        labels (Union[Unset, GoogleBatchServiceConfigurationLabels]):
        pre_run_script (Union[Unset, str]):
        post_run_script (Union[Unset, str]):
        head_job_cpus (Union[Unset, int]):
        head_job_memory_mb (Union[Unset, int]):
        nfs_target (Union[Unset, str]):
        nfs_mount (Union[Unset, str]):
        environment (Union[Unset, List['ConfigEnvVariable']]):
        wave_enabled (Union[Unset, bool]):
        fusion_2_enabled (Union[Unset, bool]):
        service_account (Union[Unset, str]):
        network (Union[Unset, str]):
        subnetwork (Union[Unset, str]):
        discriminator (Union[Unset, str]): property to select the compute config platform
    """

    location: Union[Unset, str] = UNSET
    work_dir: Union[Unset, str] = UNSET
    spot: Union[Unset, bool] = UNSET
    boot_disk_size_gb: Union[Unset, int] = UNSET
    cpu_platform: Union[Unset, str] = UNSET
    machine_type: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    ssh_daemon: Union[Unset, bool] = UNSET
    ssh_image: Union[Unset, str] = UNSET
    debug_mode: Union[Unset, int] = UNSET
    copy_image: Union[Unset, str] = UNSET
    use_private_address: Union[Unset, bool] = UNSET
    labels: Union[Unset, "GoogleBatchServiceConfigurationLabels"] = UNSET
    pre_run_script: Union[Unset, str] = UNSET
    post_run_script: Union[Unset, str] = UNSET
    head_job_cpus: Union[Unset, int] = UNSET
    head_job_memory_mb: Union[Unset, int] = UNSET
    nfs_target: Union[Unset, str] = UNSET
    nfs_mount: Union[Unset, str] = UNSET
    environment: Union[Unset, List["ConfigEnvVariable"]] = UNSET
    wave_enabled: Union[Unset, bool] = UNSET
    fusion_2_enabled: Union[Unset, bool] = UNSET
    service_account: Union[Unset, str] = UNSET
    network: Union[Unset, str] = UNSET
    subnetwork: Union[Unset, str] = UNSET
    discriminator: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        location = self.location
        work_dir = self.work_dir
        spot = self.spot
        boot_disk_size_gb = self.boot_disk_size_gb
        cpu_platform = self.cpu_platform
        machine_type = self.machine_type
        project_id = self.project_id
        ssh_daemon = self.ssh_daemon
        ssh_image = self.ssh_image
        debug_mode = self.debug_mode
        copy_image = self.copy_image
        use_private_address = self.use_private_address
        labels: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        pre_run_script = self.pre_run_script
        post_run_script = self.post_run_script
        head_job_cpus = self.head_job_cpus
        head_job_memory_mb = self.head_job_memory_mb
        nfs_target = self.nfs_target
        nfs_mount = self.nfs_mount
        environment: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.environment, Unset):
            environment = []
            for environment_item_data in self.environment:
                environment_item = environment_item_data.to_dict()

                environment.append(environment_item)

        wave_enabled = self.wave_enabled
        fusion_2_enabled = self.fusion_2_enabled
        service_account = self.service_account
        network = self.network
        subnetwork = self.subnetwork
        discriminator = self.discriminator

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location is not UNSET:
            field_dict["location"] = location
        if work_dir is not UNSET:
            field_dict["workDir"] = work_dir
        if spot is not UNSET:
            field_dict["spot"] = spot
        if boot_disk_size_gb is not UNSET:
            field_dict["bootDiskSizeGb"] = boot_disk_size_gb
        if cpu_platform is not UNSET:
            field_dict["cpuPlatform"] = cpu_platform
        if machine_type is not UNSET:
            field_dict["machineType"] = machine_type
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if ssh_daemon is not UNSET:
            field_dict["sshDaemon"] = ssh_daemon
        if ssh_image is not UNSET:
            field_dict["sshImage"] = ssh_image
        if debug_mode is not UNSET:
            field_dict["debugMode"] = debug_mode
        if copy_image is not UNSET:
            field_dict["copyImage"] = copy_image
        if use_private_address is not UNSET:
            field_dict["usePrivateAddress"] = use_private_address
        if labels is not UNSET:
            field_dict["labels"] = labels
        if pre_run_script is not UNSET:
            field_dict["preRunScript"] = pre_run_script
        if post_run_script is not UNSET:
            field_dict["postRunScript"] = post_run_script
        if head_job_cpus is not UNSET:
            field_dict["headJobCpus"] = head_job_cpus
        if head_job_memory_mb is not UNSET:
            field_dict["headJobMemoryMb"] = head_job_memory_mb
        if nfs_target is not UNSET:
            field_dict["nfsTarget"] = nfs_target
        if nfs_mount is not UNSET:
            field_dict["nfsMount"] = nfs_mount
        if environment is not UNSET:
            field_dict["environment"] = environment
        if wave_enabled is not UNSET:
            field_dict["waveEnabled"] = wave_enabled
        if fusion_2_enabled is not UNSET:
            field_dict["fusion2Enabled"] = fusion_2_enabled
        if service_account is not UNSET:
            field_dict["serviceAccount"] = service_account
        if network is not UNSET:
            field_dict["network"] = network
        if subnetwork is not UNSET:
            field_dict["subnetwork"] = subnetwork
        if discriminator is not UNSET:
            field_dict["discriminator"] = discriminator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.config_env_variable import ConfigEnvVariable
        from ..models.google_batch_service_configuration_labels import GoogleBatchServiceConfigurationLabels

        d = src_dict.copy()
        location = d.pop("location", UNSET)

        work_dir = d.pop("workDir", UNSET)

        spot = d.pop("spot", UNSET)

        boot_disk_size_gb = d.pop("bootDiskSizeGb", UNSET)

        cpu_platform = d.pop("cpuPlatform", UNSET)

        machine_type = d.pop("machineType", UNSET)

        project_id = d.pop("projectId", UNSET)

        ssh_daemon = d.pop("sshDaemon", UNSET)

        ssh_image = d.pop("sshImage", UNSET)

        debug_mode = d.pop("debugMode", UNSET)

        copy_image = d.pop("copyImage", UNSET)

        use_private_address = d.pop("usePrivateAddress", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: Union[Unset, GoogleBatchServiceConfigurationLabels]
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = GoogleBatchServiceConfigurationLabels.from_dict(_labels)

        pre_run_script = d.pop("preRunScript", UNSET)

        post_run_script = d.pop("postRunScript", UNSET)

        head_job_cpus = d.pop("headJobCpus", UNSET)

        head_job_memory_mb = d.pop("headJobMemoryMb", UNSET)

        nfs_target = d.pop("nfsTarget", UNSET)

        nfs_mount = d.pop("nfsMount", UNSET)

        environment = []
        _environment = d.pop("environment", UNSET)
        for environment_item_data in _environment or []:
            environment_item = ConfigEnvVariable.from_dict(environment_item_data)

            environment.append(environment_item)

        wave_enabled = d.pop("waveEnabled", UNSET)

        fusion_2_enabled = d.pop("fusion2Enabled", UNSET)

        service_account = d.pop("serviceAccount", UNSET)

        network = d.pop("network", UNSET)

        subnetwork = d.pop("subnetwork", UNSET)

        discriminator = d.pop("discriminator", UNSET)

        google_batch_service_configuration = cls(
            location=location,
            work_dir=work_dir,
            spot=spot,
            boot_disk_size_gb=boot_disk_size_gb,
            cpu_platform=cpu_platform,
            machine_type=machine_type,
            project_id=project_id,
            ssh_daemon=ssh_daemon,
            ssh_image=ssh_image,
            debug_mode=debug_mode,
            copy_image=copy_image,
            use_private_address=use_private_address,
            labels=labels,
            pre_run_script=pre_run_script,
            post_run_script=post_run_script,
            head_job_cpus=head_job_cpus,
            head_job_memory_mb=head_job_memory_mb,
            nfs_target=nfs_target,
            nfs_mount=nfs_mount,
            environment=environment,
            wave_enabled=wave_enabled,
            fusion_2_enabled=fusion_2_enabled,
            service_account=service_account,
            network=network,
            subnetwork=subnetwork,
            discriminator=discriminator,
        )

        google_batch_service_configuration.additional_properties = d
        return google_batch_service_configuration

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
