from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aws_batch_platform_metainfo_bucket import AwsBatchPlatformMetainfoBucket
    from ..models.aws_batch_platform_metainfo_efs_file_system import AwsBatchPlatformMetainfoEfsFileSystem
    from ..models.aws_batch_platform_metainfo_fsx_file_system import AwsBatchPlatformMetainfoFsxFileSystem
    from ..models.aws_batch_platform_metainfo_image import AwsBatchPlatformMetainfoImage
    from ..models.aws_batch_platform_metainfo_job_queue import AwsBatchPlatformMetainfoJobQueue
    from ..models.aws_batch_platform_metainfo_security_group import AwsBatchPlatformMetainfoSecurityGroup
    from ..models.aws_batch_platform_metainfo_subnet import AwsBatchPlatformMetainfoSubnet
    from ..models.aws_batch_platform_metainfo_vpc import AwsBatchPlatformMetainfoVpc


T = TypeVar("T", bound="AwsBatchPlatformMetainfo")


@_attrs_define
class AwsBatchPlatformMetainfo:
    """
    Attributes:
        warnings (Union[Unset, List[str]]):
        job_queues (Union[Unset, List['AwsBatchPlatformMetainfoJobQueue']]):
        buckets (Union[Unset, List['AwsBatchPlatformMetainfoBucket']]):
        file_systems (Union[Unset, List['AwsBatchPlatformMetainfoFsxFileSystem']]):
        efs_file_systems (Union[Unset, List['AwsBatchPlatformMetainfoEfsFileSystem']]):
        key_pairs (Union[Unset, List[str]]):
        vpcs (Union[Unset, List['AwsBatchPlatformMetainfoVpc']]):
        images (Union[Unset, List['AwsBatchPlatformMetainfoImage']]):
        security_groups (Union[Unset, List['AwsBatchPlatformMetainfoSecurityGroup']]):
        subnets (Union[Unset, List['AwsBatchPlatformMetainfoSubnet']]):
        instance_families (Union[Unset, List[str]]):
        alloc_strategy (Union[Unset, List[str]]):
    """

    warnings: Union[Unset, List[str]] = UNSET
    job_queues: Union[Unset, List["AwsBatchPlatformMetainfoJobQueue"]] = UNSET
    buckets: Union[Unset, List["AwsBatchPlatformMetainfoBucket"]] = UNSET
    file_systems: Union[Unset, List["AwsBatchPlatformMetainfoFsxFileSystem"]] = UNSET
    efs_file_systems: Union[Unset, List["AwsBatchPlatformMetainfoEfsFileSystem"]] = UNSET
    key_pairs: Union[Unset, List[str]] = UNSET
    vpcs: Union[Unset, List["AwsBatchPlatformMetainfoVpc"]] = UNSET
    images: Union[Unset, List["AwsBatchPlatformMetainfoImage"]] = UNSET
    security_groups: Union[Unset, List["AwsBatchPlatformMetainfoSecurityGroup"]] = UNSET
    subnets: Union[Unset, List["AwsBatchPlatformMetainfoSubnet"]] = UNSET
    instance_families: Union[Unset, List[str]] = UNSET
    alloc_strategy: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        warnings: Union[Unset, List[str]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        job_queues: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.job_queues, Unset):
            job_queues = []
            for job_queues_item_data in self.job_queues:
                job_queues_item = job_queues_item_data.to_dict()

                job_queues.append(job_queues_item)

        buckets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.buckets, Unset):
            buckets = []
            for buckets_item_data in self.buckets:
                buckets_item = buckets_item_data.to_dict()

                buckets.append(buckets_item)

        file_systems: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.file_systems, Unset):
            file_systems = []
            for file_systems_item_data in self.file_systems:
                file_systems_item = file_systems_item_data.to_dict()

                file_systems.append(file_systems_item)

        efs_file_systems: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.efs_file_systems, Unset):
            efs_file_systems = []
            for efs_file_systems_item_data in self.efs_file_systems:
                efs_file_systems_item = efs_file_systems_item_data.to_dict()

                efs_file_systems.append(efs_file_systems_item)

        key_pairs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.key_pairs, Unset):
            key_pairs = self.key_pairs

        vpcs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.vpcs, Unset):
            vpcs = []
            for vpcs_item_data in self.vpcs:
                vpcs_item = vpcs_item_data.to_dict()

                vpcs.append(vpcs_item)

        images: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()

                images.append(images_item)

        security_groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.security_groups, Unset):
            security_groups = []
            for security_groups_item_data in self.security_groups:
                security_groups_item = security_groups_item_data.to_dict()

                security_groups.append(security_groups_item)

        subnets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subnets, Unset):
            subnets = []
            for subnets_item_data in self.subnets:
                subnets_item = subnets_item_data.to_dict()

                subnets.append(subnets_item)

        instance_families: Union[Unset, List[str]] = UNSET
        if not isinstance(self.instance_families, Unset):
            instance_families = self.instance_families

        alloc_strategy: Union[Unset, List[str]] = UNSET
        if not isinstance(self.alloc_strategy, Unset):
            alloc_strategy = self.alloc_strategy

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if job_queues is not UNSET:
            field_dict["jobQueues"] = job_queues
        if buckets is not UNSET:
            field_dict["buckets"] = buckets
        if file_systems is not UNSET:
            field_dict["fileSystems"] = file_systems
        if efs_file_systems is not UNSET:
            field_dict["efsFileSystems"] = efs_file_systems
        if key_pairs is not UNSET:
            field_dict["keyPairs"] = key_pairs
        if vpcs is not UNSET:
            field_dict["vpcs"] = vpcs
        if images is not UNSET:
            field_dict["images"] = images
        if security_groups is not UNSET:
            field_dict["securityGroups"] = security_groups
        if subnets is not UNSET:
            field_dict["subnets"] = subnets
        if instance_families is not UNSET:
            field_dict["instanceFamilies"] = instance_families
        if alloc_strategy is not UNSET:
            field_dict["allocStrategy"] = alloc_strategy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aws_batch_platform_metainfo_bucket import AwsBatchPlatformMetainfoBucket
        from ..models.aws_batch_platform_metainfo_efs_file_system import AwsBatchPlatformMetainfoEfsFileSystem
        from ..models.aws_batch_platform_metainfo_fsx_file_system import AwsBatchPlatformMetainfoFsxFileSystem
        from ..models.aws_batch_platform_metainfo_image import AwsBatchPlatformMetainfoImage
        from ..models.aws_batch_platform_metainfo_job_queue import AwsBatchPlatformMetainfoJobQueue
        from ..models.aws_batch_platform_metainfo_security_group import AwsBatchPlatformMetainfoSecurityGroup
        from ..models.aws_batch_platform_metainfo_subnet import AwsBatchPlatformMetainfoSubnet
        from ..models.aws_batch_platform_metainfo_vpc import AwsBatchPlatformMetainfoVpc

        d = src_dict.copy()
        warnings = cast(List[str], d.pop("warnings", UNSET))

        job_queues = []
        _job_queues = d.pop("jobQueues", UNSET)
        for job_queues_item_data in _job_queues or []:
            job_queues_item = AwsBatchPlatformMetainfoJobQueue.from_dict(job_queues_item_data)

            job_queues.append(job_queues_item)

        buckets = []
        _buckets = d.pop("buckets", UNSET)
        for buckets_item_data in _buckets or []:
            buckets_item = AwsBatchPlatformMetainfoBucket.from_dict(buckets_item_data)

            buckets.append(buckets_item)

        file_systems = []
        _file_systems = d.pop("fileSystems", UNSET)
        for file_systems_item_data in _file_systems or []:
            file_systems_item = AwsBatchPlatformMetainfoFsxFileSystem.from_dict(file_systems_item_data)

            file_systems.append(file_systems_item)

        efs_file_systems = []
        _efs_file_systems = d.pop("efsFileSystems", UNSET)
        for efs_file_systems_item_data in _efs_file_systems or []:
            efs_file_systems_item = AwsBatchPlatformMetainfoEfsFileSystem.from_dict(efs_file_systems_item_data)

            efs_file_systems.append(efs_file_systems_item)

        key_pairs = cast(List[str], d.pop("keyPairs", UNSET))

        vpcs = []
        _vpcs = d.pop("vpcs", UNSET)
        for vpcs_item_data in _vpcs or []:
            vpcs_item = AwsBatchPlatformMetainfoVpc.from_dict(vpcs_item_data)

            vpcs.append(vpcs_item)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = AwsBatchPlatformMetainfoImage.from_dict(images_item_data)

            images.append(images_item)

        security_groups = []
        _security_groups = d.pop("securityGroups", UNSET)
        for security_groups_item_data in _security_groups or []:
            security_groups_item = AwsBatchPlatformMetainfoSecurityGroup.from_dict(security_groups_item_data)

            security_groups.append(security_groups_item)

        subnets = []
        _subnets = d.pop("subnets", UNSET)
        for subnets_item_data in _subnets or []:
            subnets_item = AwsBatchPlatformMetainfoSubnet.from_dict(subnets_item_data)

            subnets.append(subnets_item)

        instance_families = cast(List[str], d.pop("instanceFamilies", UNSET))

        alloc_strategy = cast(List[str], d.pop("allocStrategy", UNSET))

        aws_batch_platform_metainfo = cls(
            warnings=warnings,
            job_queues=job_queues,
            buckets=buckets,
            file_systems=file_systems,
            efs_file_systems=efs_file_systems,
            key_pairs=key_pairs,
            vpcs=vpcs,
            images=images,
            security_groups=security_groups,
            subnets=subnets,
            instance_families=instance_families,
            alloc_strategy=alloc_strategy,
        )

        aws_batch_platform_metainfo.additional_properties = d
        return aws_batch_platform_metainfo

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
