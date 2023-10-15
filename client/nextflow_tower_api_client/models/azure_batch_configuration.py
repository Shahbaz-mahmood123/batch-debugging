from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.job_cleanup_policy import JobCleanupPolicy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.az_batch_forge_config import AzBatchForgeConfig
    from ..models.config_env_variable import ConfigEnvVariable


T = TypeVar("T", bound="AzureBatchConfiguration")


@_attrs_define
class AzureBatchConfiguration:
    """
    Attributes:
        work_dir (Union[Unset, str]):
        pre_run_script (Union[Unset, str]):
        post_run_script (Union[Unset, str]):
        region (Union[Unset, str]):
        head_pool (Union[Unset, str]):
        auto_pool_mode (Union[Unset, bool]):
        forge (Union[Unset, AzBatchForgeConfig]):
        token_duration (Union[Unset, str]):
        delete_jobs_on_completion (Union[Unset, JobCleanupPolicy]):
        delete_pools_on_completion (Union[Unset, bool]):
        environment (Union[Unset, List['ConfigEnvVariable']]):
        wave_enabled (Union[Unset, bool]):
        fusion_2_enabled (Union[Unset, bool]):
        discriminator (Union[Unset, str]): property to select the compute config platform
    """

    work_dir: Union[Unset, str] = UNSET
    pre_run_script: Union[Unset, str] = UNSET
    post_run_script: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    head_pool: Union[Unset, str] = UNSET
    auto_pool_mode: Union[Unset, bool] = UNSET
    forge: Union[Unset, "AzBatchForgeConfig"] = UNSET
    token_duration: Union[Unset, str] = UNSET
    delete_jobs_on_completion: Union[Unset, JobCleanupPolicy] = UNSET
    delete_pools_on_completion: Union[Unset, bool] = UNSET
    environment: Union[Unset, List["ConfigEnvVariable"]] = UNSET
    wave_enabled: Union[Unset, bool] = UNSET
    fusion_2_enabled: Union[Unset, bool] = UNSET
    discriminator: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        work_dir = self.work_dir
        pre_run_script = self.pre_run_script
        post_run_script = self.post_run_script
        region = self.region
        head_pool = self.head_pool
        auto_pool_mode = self.auto_pool_mode
        forge: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.forge, Unset):
            forge = self.forge.to_dict()

        token_duration = self.token_duration
        delete_jobs_on_completion: Union[Unset, str] = UNSET
        if not isinstance(self.delete_jobs_on_completion, Unset):
            delete_jobs_on_completion = self.delete_jobs_on_completion.value

        delete_pools_on_completion = self.delete_pools_on_completion
        environment: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.environment, Unset):
            environment = []
            for environment_item_data in self.environment:
                environment_item = environment_item_data.to_dict()

                environment.append(environment_item)

        wave_enabled = self.wave_enabled
        fusion_2_enabled = self.fusion_2_enabled
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
        if region is not UNSET:
            field_dict["region"] = region
        if head_pool is not UNSET:
            field_dict["headPool"] = head_pool
        if auto_pool_mode is not UNSET:
            field_dict["autoPoolMode"] = auto_pool_mode
        if forge is not UNSET:
            field_dict["forge"] = forge
        if token_duration is not UNSET:
            field_dict["tokenDuration"] = token_duration
        if delete_jobs_on_completion is not UNSET:
            field_dict["deleteJobsOnCompletion"] = delete_jobs_on_completion
        if delete_pools_on_completion is not UNSET:
            field_dict["deletePoolsOnCompletion"] = delete_pools_on_completion
        if environment is not UNSET:
            field_dict["environment"] = environment
        if wave_enabled is not UNSET:
            field_dict["waveEnabled"] = wave_enabled
        if fusion_2_enabled is not UNSET:
            field_dict["fusion2Enabled"] = fusion_2_enabled
        if discriminator is not UNSET:
            field_dict["discriminator"] = discriminator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.az_batch_forge_config import AzBatchForgeConfig
        from ..models.config_env_variable import ConfigEnvVariable

        d = src_dict.copy()
        work_dir = d.pop("workDir", UNSET)

        pre_run_script = d.pop("preRunScript", UNSET)

        post_run_script = d.pop("postRunScript", UNSET)

        region = d.pop("region", UNSET)

        head_pool = d.pop("headPool", UNSET)

        auto_pool_mode = d.pop("autoPoolMode", UNSET)

        _forge = d.pop("forge", UNSET)
        forge: Union[Unset, AzBatchForgeConfig]
        if isinstance(_forge, Unset):
            forge = UNSET
        else:
            forge = AzBatchForgeConfig.from_dict(_forge)

        token_duration = d.pop("tokenDuration", UNSET)

        _delete_jobs_on_completion = d.pop("deleteJobsOnCompletion", UNSET)
        delete_jobs_on_completion: Union[Unset, JobCleanupPolicy]
        if isinstance(_delete_jobs_on_completion, Unset):
            delete_jobs_on_completion = UNSET
        else:
            delete_jobs_on_completion = JobCleanupPolicy(_delete_jobs_on_completion)

        delete_pools_on_completion = d.pop("deletePoolsOnCompletion", UNSET)

        environment = []
        _environment = d.pop("environment", UNSET)
        for environment_item_data in _environment or []:
            environment_item = ConfigEnvVariable.from_dict(environment_item_data)

            environment.append(environment_item)

        wave_enabled = d.pop("waveEnabled", UNSET)

        fusion_2_enabled = d.pop("fusion2Enabled", UNSET)

        discriminator = d.pop("discriminator", UNSET)

        azure_batch_configuration = cls(
            work_dir=work_dir,
            pre_run_script=pre_run_script,
            post_run_script=post_run_script,
            region=region,
            head_pool=head_pool,
            auto_pool_mode=auto_pool_mode,
            forge=forge,
            token_duration=token_duration,
            delete_jobs_on_completion=delete_jobs_on_completion,
            delete_pools_on_completion=delete_pools_on_completion,
            environment=environment,
            wave_enabled=wave_enabled,
            fusion_2_enabled=fusion_2_enabled,
            discriminator=discriminator,
        )

        azure_batch_configuration.additional_properties = d
        return azure_batch_configuration

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
