from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.forge_config_alloc_strategy import ForgeConfigAllocStrategy
from ..models.forge_config_type import ForgeConfigType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ForgeConfig")


@_attrs_define
class ForgeConfig:
    """
    Attributes:
        type (Union[Unset, ForgeConfigType]):
        min_cpus (Union[Unset, int]):
        max_cpus (Union[Unset, int]):
        gpu_enabled (Union[Unset, bool]):
        ebs_auto_scale (Union[Unset, bool]):
        instance_types (Union[Unset, List[str]]):
        alloc_strategy (Union[Unset, ForgeConfigAllocStrategy]):
        image_id (Union[Unset, str]):
        vpc_id (Union[Unset, str]):
        subnets (Union[Unset, List[str]]):
        security_groups (Union[Unset, List[str]]):
        fsx_mount (Union[Unset, str]):
        fsx_name (Union[Unset, str]):
        fsx_size (Union[Unset, int]):
        dispose_on_deletion (Union[Unset, bool]):
        ec_2_key_pair (Union[Unset, str]):
        allow_buckets (Union[Unset, List[str]]):
        ebs_block_size (Union[Unset, int]):
        fusion_enabled (Union[Unset, bool]):
        bid_percentage (Union[Unset, int]):
        efs_create (Union[Unset, bool]):
        efs_id (Union[Unset, str]):
        efs_mount (Union[Unset, str]):
        dragen_enabled (Union[Unset, bool]):
        dragen_ami_id (Union[Unset, str]):
        ebs_boot_size (Union[Unset, int]):
        ecs_config (Union[Unset, str]):
        fargate_head_enabled (Union[Unset, bool]):
        arm_64_enabled (Union[Unset, bool]):
    """

    type: Union[Unset, ForgeConfigType] = UNSET
    min_cpus: Union[Unset, int] = UNSET
    max_cpus: Union[Unset, int] = UNSET
    gpu_enabled: Union[Unset, bool] = UNSET
    ebs_auto_scale: Union[Unset, bool] = UNSET
    instance_types: Union[Unset, List[str]] = UNSET
    alloc_strategy: Union[Unset, ForgeConfigAllocStrategy] = UNSET
    image_id: Union[Unset, str] = UNSET
    vpc_id: Union[Unset, str] = UNSET
    subnets: Union[Unset, List[str]] = UNSET
    security_groups: Union[Unset, List[str]] = UNSET
    fsx_mount: Union[Unset, str] = UNSET
    fsx_name: Union[Unset, str] = UNSET
    fsx_size: Union[Unset, int] = UNSET
    dispose_on_deletion: Union[Unset, bool] = UNSET
    ec_2_key_pair: Union[Unset, str] = UNSET
    allow_buckets: Union[Unset, List[str]] = UNSET
    ebs_block_size: Union[Unset, int] = UNSET
    fusion_enabled: Union[Unset, bool] = UNSET
    bid_percentage: Union[Unset, int] = UNSET
    efs_create: Union[Unset, bool] = UNSET
    efs_id: Union[Unset, str] = UNSET
    efs_mount: Union[Unset, str] = UNSET
    dragen_enabled: Union[Unset, bool] = UNSET
    dragen_ami_id: Union[Unset, str] = UNSET
    ebs_boot_size: Union[Unset, int] = UNSET
    ecs_config: Union[Unset, str] = UNSET
    fargate_head_enabled: Union[Unset, bool] = UNSET
    arm_64_enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        min_cpus = self.min_cpus
        max_cpus = self.max_cpus
        gpu_enabled = self.gpu_enabled
        ebs_auto_scale = self.ebs_auto_scale
        instance_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.instance_types, Unset):
            instance_types = self.instance_types

        alloc_strategy: Union[Unset, str] = UNSET
        if not isinstance(self.alloc_strategy, Unset):
            alloc_strategy = self.alloc_strategy.value

        image_id = self.image_id
        vpc_id = self.vpc_id
        subnets: Union[Unset, List[str]] = UNSET
        if not isinstance(self.subnets, Unset):
            subnets = self.subnets

        security_groups: Union[Unset, List[str]] = UNSET
        if not isinstance(self.security_groups, Unset):
            security_groups = self.security_groups

        fsx_mount = self.fsx_mount
        fsx_name = self.fsx_name
        fsx_size = self.fsx_size
        dispose_on_deletion = self.dispose_on_deletion
        ec_2_key_pair = self.ec_2_key_pair
        allow_buckets: Union[Unset, List[str]] = UNSET
        if not isinstance(self.allow_buckets, Unset):
            allow_buckets = self.allow_buckets

        ebs_block_size = self.ebs_block_size
        fusion_enabled = self.fusion_enabled
        bid_percentage = self.bid_percentage
        efs_create = self.efs_create
        efs_id = self.efs_id
        efs_mount = self.efs_mount
        dragen_enabled = self.dragen_enabled
        dragen_ami_id = self.dragen_ami_id
        ebs_boot_size = self.ebs_boot_size
        ecs_config = self.ecs_config
        fargate_head_enabled = self.fargate_head_enabled
        arm_64_enabled = self.arm_64_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if min_cpus is not UNSET:
            field_dict["minCpus"] = min_cpus
        if max_cpus is not UNSET:
            field_dict["maxCpus"] = max_cpus
        if gpu_enabled is not UNSET:
            field_dict["gpuEnabled"] = gpu_enabled
        if ebs_auto_scale is not UNSET:
            field_dict["ebsAutoScale"] = ebs_auto_scale
        if instance_types is not UNSET:
            field_dict["instanceTypes"] = instance_types
        if alloc_strategy is not UNSET:
            field_dict["allocStrategy"] = alloc_strategy
        if image_id is not UNSET:
            field_dict["imageId"] = image_id
        if vpc_id is not UNSET:
            field_dict["vpcId"] = vpc_id
        if subnets is not UNSET:
            field_dict["subnets"] = subnets
        if security_groups is not UNSET:
            field_dict["securityGroups"] = security_groups
        if fsx_mount is not UNSET:
            field_dict["fsxMount"] = fsx_mount
        if fsx_name is not UNSET:
            field_dict["fsxName"] = fsx_name
        if fsx_size is not UNSET:
            field_dict["fsxSize"] = fsx_size
        if dispose_on_deletion is not UNSET:
            field_dict["disposeOnDeletion"] = dispose_on_deletion
        if ec_2_key_pair is not UNSET:
            field_dict["ec2KeyPair"] = ec_2_key_pair
        if allow_buckets is not UNSET:
            field_dict["allowBuckets"] = allow_buckets
        if ebs_block_size is not UNSET:
            field_dict["ebsBlockSize"] = ebs_block_size
        if fusion_enabled is not UNSET:
            field_dict["fusionEnabled"] = fusion_enabled
        if bid_percentage is not UNSET:
            field_dict["bidPercentage"] = bid_percentage
        if efs_create is not UNSET:
            field_dict["efsCreate"] = efs_create
        if efs_id is not UNSET:
            field_dict["efsId"] = efs_id
        if efs_mount is not UNSET:
            field_dict["efsMount"] = efs_mount
        if dragen_enabled is not UNSET:
            field_dict["dragenEnabled"] = dragen_enabled
        if dragen_ami_id is not UNSET:
            field_dict["dragenAmiId"] = dragen_ami_id
        if ebs_boot_size is not UNSET:
            field_dict["ebsBootSize"] = ebs_boot_size
        if ecs_config is not UNSET:
            field_dict["ecsConfig"] = ecs_config
        if fargate_head_enabled is not UNSET:
            field_dict["fargateHeadEnabled"] = fargate_head_enabled
        if arm_64_enabled is not UNSET:
            field_dict["arm64Enabled"] = arm_64_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, ForgeConfigType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ForgeConfigType(_type)

        min_cpus = d.pop("minCpus", UNSET)

        max_cpus = d.pop("maxCpus", UNSET)

        gpu_enabled = d.pop("gpuEnabled", UNSET)

        ebs_auto_scale = d.pop("ebsAutoScale", UNSET)

        instance_types = cast(List[str], d.pop("instanceTypes", UNSET))

        _alloc_strategy = d.pop("allocStrategy", UNSET)
        alloc_strategy: Union[Unset, ForgeConfigAllocStrategy]
        if isinstance(_alloc_strategy, Unset):
            alloc_strategy = UNSET
        else:
            alloc_strategy = ForgeConfigAllocStrategy(_alloc_strategy)

        image_id = d.pop("imageId", UNSET)

        vpc_id = d.pop("vpcId", UNSET)

        subnets = cast(List[str], d.pop("subnets", UNSET))

        security_groups = cast(List[str], d.pop("securityGroups", UNSET))

        fsx_mount = d.pop("fsxMount", UNSET)

        fsx_name = d.pop("fsxName", UNSET)

        fsx_size = d.pop("fsxSize", UNSET)

        dispose_on_deletion = d.pop("disposeOnDeletion", UNSET)

        ec_2_key_pair = d.pop("ec2KeyPair", UNSET)

        allow_buckets = cast(List[str], d.pop("allowBuckets", UNSET))

        ebs_block_size = d.pop("ebsBlockSize", UNSET)

        fusion_enabled = d.pop("fusionEnabled", UNSET)

        bid_percentage = d.pop("bidPercentage", UNSET)

        efs_create = d.pop("efsCreate", UNSET)

        efs_id = d.pop("efsId", UNSET)

        efs_mount = d.pop("efsMount", UNSET)

        dragen_enabled = d.pop("dragenEnabled", UNSET)

        dragen_ami_id = d.pop("dragenAmiId", UNSET)

        ebs_boot_size = d.pop("ebsBootSize", UNSET)

        ecs_config = d.pop("ecsConfig", UNSET)

        fargate_head_enabled = d.pop("fargateHeadEnabled", UNSET)

        arm_64_enabled = d.pop("arm64Enabled", UNSET)

        forge_config = cls(
            type=type,
            min_cpus=min_cpus,
            max_cpus=max_cpus,
            gpu_enabled=gpu_enabled,
            ebs_auto_scale=ebs_auto_scale,
            instance_types=instance_types,
            alloc_strategy=alloc_strategy,
            image_id=image_id,
            vpc_id=vpc_id,
            subnets=subnets,
            security_groups=security_groups,
            fsx_mount=fsx_mount,
            fsx_name=fsx_name,
            fsx_size=fsx_size,
            dispose_on_deletion=dispose_on_deletion,
            ec_2_key_pair=ec_2_key_pair,
            allow_buckets=allow_buckets,
            ebs_block_size=ebs_block_size,
            fusion_enabled=fusion_enabled,
            bid_percentage=bid_percentage,
            efs_create=efs_create,
            efs_id=efs_id,
            efs_mount=efs_mount,
            dragen_enabled=dragen_enabled,
            dragen_ami_id=dragen_ami_id,
            ebs_boot_size=ebs_boot_size,
            ecs_config=ecs_config,
            fargate_head_enabled=fargate_head_enabled,
            arm_64_enabled=arm_64_enabled,
        )

        forge_config.additional_properties = d
        return forge_config

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
