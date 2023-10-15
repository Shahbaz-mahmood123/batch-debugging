from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aws_batch_configuration_forged_resources_item import AWSBatchConfigurationForgedResourcesItem
    from ..models.config_env_variable import ConfigEnvVariable
    from ..models.forge_config import ForgeConfig


T = TypeVar("T", bound="AWSBatchConfiguration")


@_attrs_define
class AWSBatchConfiguration:
    """
    Attributes:
        region (Union[Unset, str]):
        compute_queue (Union[Unset, str]):
        dragen_queue (Union[Unset, str]):
        compute_job_role (Union[Unset, str]):
        execution_role (Union[Unset, str]):
        head_queue (Union[Unset, str]):
        head_job_role (Union[Unset, str]):
        cli_path (Union[Unset, str]):
        volumes (Union[Unset, List[str]]):
        work_dir (Union[Unset, str]):
        pre_run_script (Union[Unset, str]):
        post_run_script (Union[Unset, str]):
        head_job_cpus (Union[Unset, int]):
        head_job_memory_mb (Union[Unset, int]):
        environment (Union[Unset, List['ConfigEnvVariable']]):
        wave_enabled (Union[Unset, bool]):
        fusion_2_enabled (Union[Unset, bool]):
        nvnme_storage_enabled (Union[Unset, bool]):
        log_group (Union[Unset, str]):
        forge (Union[Unset, ForgeConfig]):
        forged_resources (Union[Unset, List['AWSBatchConfigurationForgedResourcesItem']]):
        discriminator (Union[Unset, str]): property to select the compute config platform
    """

    region: Union[Unset, str] = UNSET
    compute_queue: Union[Unset, str] = UNSET
    dragen_queue: Union[Unset, str] = UNSET
    compute_job_role: Union[Unset, str] = UNSET
    execution_role: Union[Unset, str] = UNSET
    head_queue: Union[Unset, str] = UNSET
    head_job_role: Union[Unset, str] = UNSET
    cli_path: Union[Unset, str] = UNSET
    volumes: Union[Unset, List[str]] = UNSET
    work_dir: Union[Unset, str] = UNSET
    pre_run_script: Union[Unset, str] = UNSET
    post_run_script: Union[Unset, str] = UNSET
    head_job_cpus: Union[Unset, int] = UNSET
    head_job_memory_mb: Union[Unset, int] = UNSET
    environment: Union[Unset, List["ConfigEnvVariable"]] = UNSET
    wave_enabled: Union[Unset, bool] = UNSET
    fusion_2_enabled: Union[Unset, bool] = UNSET
    nvnme_storage_enabled: Union[Unset, bool] = UNSET
    log_group: Union[Unset, str] = UNSET
    forge: Union[Unset, "ForgeConfig"] = UNSET
    forged_resources: Union[Unset, List["AWSBatchConfigurationForgedResourcesItem"]] = UNSET
    discriminator: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        region = self.region
        compute_queue = self.compute_queue
        dragen_queue = self.dragen_queue
        compute_job_role = self.compute_job_role
        execution_role = self.execution_role
        head_queue = self.head_queue
        head_job_role = self.head_job_role
        cli_path = self.cli_path
        volumes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.volumes, Unset):
            volumes = self.volumes

        work_dir = self.work_dir
        pre_run_script = self.pre_run_script
        post_run_script = self.post_run_script
        head_job_cpus = self.head_job_cpus
        head_job_memory_mb = self.head_job_memory_mb
        environment: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.environment, Unset):
            environment = []
            for environment_item_data in self.environment:
                environment_item = environment_item_data.to_dict()

                environment.append(environment_item)

        wave_enabled = self.wave_enabled
        fusion_2_enabled = self.fusion_2_enabled
        nvnme_storage_enabled = self.nvnme_storage_enabled
        log_group = self.log_group
        forge: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.forge, Unset):
            forge = self.forge.to_dict()

        forged_resources: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.forged_resources, Unset):
            forged_resources = []
            for forged_resources_item_data in self.forged_resources:
                forged_resources_item = forged_resources_item_data.to_dict()

                forged_resources.append(forged_resources_item)

        discriminator = self.discriminator

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if region is not UNSET:
            field_dict["region"] = region
        if compute_queue is not UNSET:
            field_dict["computeQueue"] = compute_queue
        if dragen_queue is not UNSET:
            field_dict["dragenQueue"] = dragen_queue
        if compute_job_role is not UNSET:
            field_dict["computeJobRole"] = compute_job_role
        if execution_role is not UNSET:
            field_dict["executionRole"] = execution_role
        if head_queue is not UNSET:
            field_dict["headQueue"] = head_queue
        if head_job_role is not UNSET:
            field_dict["headJobRole"] = head_job_role
        if cli_path is not UNSET:
            field_dict["cliPath"] = cli_path
        if volumes is not UNSET:
            field_dict["volumes"] = volumes
        if work_dir is not UNSET:
            field_dict["workDir"] = work_dir
        if pre_run_script is not UNSET:
            field_dict["preRunScript"] = pre_run_script
        if post_run_script is not UNSET:
            field_dict["postRunScript"] = post_run_script
        if head_job_cpus is not UNSET:
            field_dict["headJobCpus"] = head_job_cpus
        if head_job_memory_mb is not UNSET:
            field_dict["headJobMemoryMb"] = head_job_memory_mb
        if environment is not UNSET:
            field_dict["environment"] = environment
        if wave_enabled is not UNSET:
            field_dict["waveEnabled"] = wave_enabled
        if fusion_2_enabled is not UNSET:
            field_dict["fusion2Enabled"] = fusion_2_enabled
        if nvnme_storage_enabled is not UNSET:
            field_dict["nvnmeStorageEnabled"] = nvnme_storage_enabled
        if log_group is not UNSET:
            field_dict["logGroup"] = log_group
        if forge is not UNSET:
            field_dict["forge"] = forge
        if forged_resources is not UNSET:
            field_dict["forgedResources"] = forged_resources
        if discriminator is not UNSET:
            field_dict["discriminator"] = discriminator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aws_batch_configuration_forged_resources_item import AWSBatchConfigurationForgedResourcesItem
        from ..models.config_env_variable import ConfigEnvVariable
        from ..models.forge_config import ForgeConfig

        d = src_dict.copy()
        region = d.pop("region", UNSET)

        compute_queue = d.pop("computeQueue", UNSET)

        dragen_queue = d.pop("dragenQueue", UNSET)

        compute_job_role = d.pop("computeJobRole", UNSET)

        execution_role = d.pop("executionRole", UNSET)

        head_queue = d.pop("headQueue", UNSET)

        head_job_role = d.pop("headJobRole", UNSET)

        cli_path = d.pop("cliPath", UNSET)

        volumes = cast(List[str], d.pop("volumes", UNSET))

        work_dir = d.pop("workDir", UNSET)

        pre_run_script = d.pop("preRunScript", UNSET)

        post_run_script = d.pop("postRunScript", UNSET)

        head_job_cpus = d.pop("headJobCpus", UNSET)

        head_job_memory_mb = d.pop("headJobMemoryMb", UNSET)

        environment = []
        _environment = d.pop("environment", UNSET)
        for environment_item_data in _environment or []:
            environment_item = ConfigEnvVariable.from_dict(environment_item_data)

            environment.append(environment_item)

        wave_enabled = d.pop("waveEnabled", UNSET)

        fusion_2_enabled = d.pop("fusion2Enabled", UNSET)

        nvnme_storage_enabled = d.pop("nvnmeStorageEnabled", UNSET)

        log_group = d.pop("logGroup", UNSET)

        _forge = d.pop("forge", UNSET)
        forge: Union[Unset, ForgeConfig]
        if isinstance(_forge, Unset):
            forge = UNSET
        else:
            forge = ForgeConfig.from_dict(_forge)

        forged_resources = []
        _forged_resources = d.pop("forgedResources", UNSET)
        for forged_resources_item_data in _forged_resources or []:
            forged_resources_item = AWSBatchConfigurationForgedResourcesItem.from_dict(forged_resources_item_data)

            forged_resources.append(forged_resources_item)

        discriminator = d.pop("discriminator", UNSET)

        aws_batch_configuration = cls(
            region=region,
            compute_queue=compute_queue,
            dragen_queue=dragen_queue,
            compute_job_role=compute_job_role,
            execution_role=execution_role,
            head_queue=head_queue,
            head_job_role=head_job_role,
            cli_path=cli_path,
            volumes=volumes,
            work_dir=work_dir,
            pre_run_script=pre_run_script,
            post_run_script=post_run_script,
            head_job_cpus=head_job_cpus,
            head_job_memory_mb=head_job_memory_mb,
            environment=environment,
            wave_enabled=wave_enabled,
            fusion_2_enabled=fusion_2_enabled,
            nvnme_storage_enabled=nvnme_storage_enabled,
            log_group=log_group,
            forge=forge,
            forged_resources=forged_resources,
            discriminator=discriminator,
        )

        aws_batch_configuration.additional_properties = d
        return aws_batch_configuration

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
