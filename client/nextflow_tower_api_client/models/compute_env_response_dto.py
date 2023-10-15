import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.compute_env_response_dto_platform import ComputeEnvResponseDtoPlatform
from ..models.compute_env_status import ComputeEnvStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.altair_pbs_configuration import AltairPBSConfiguration
    from ..models.amazon_eks_cluster_configuration import AmazonEKSClusterConfiguration
    from ..models.aws_batch_configuration import AWSBatchConfiguration
    from ..models.azure_batch_configuration import AzureBatchConfiguration
    from ..models.google_batch_service_configuration import GoogleBatchServiceConfiguration
    from ..models.google_gke_cluster_configuration import GoogleGKEClusterConfiguration
    from ..models.google_life_sciences_configuration import GoogleLifeSciencesConfiguration
    from ..models.ibmlsf_configuration import IBMLSFConfiguration
    from ..models.kubernetes_compute_configuration import KubernetesComputeConfiguration
    from ..models.label_db_dto import LabelDbDto
    from ..models.moab_configuration import MoabConfiguration
    from ..models.slurm_configuration import SlurmConfiguration
    from ..models.univa_grid_engine_configuration import UnivaGridEngineConfiguration


T = TypeVar("T", bound="ComputeEnvResponseDto")


@_attrs_define
class ComputeEnvResponseDto:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        platform (Union[Unset, ComputeEnvResponseDtoPlatform]):
        config (Union['AWSBatchConfiguration', 'AltairPBSConfiguration', 'AmazonEKSClusterConfiguration',
            'AzureBatchConfiguration', 'GoogleBatchServiceConfiguration', 'GoogleGKEClusterConfiguration',
            'GoogleLifeSciencesConfiguration', 'IBMLSFConfiguration', 'KubernetesComputeConfiguration', 'MoabConfiguration',
            'SlurmConfiguration', 'UnivaGridEngineConfiguration', Unset]):
        date_created (Union[Unset, datetime.datetime]):
        last_updated (Union[Unset, datetime.datetime]):
        last_used (Union[Unset, datetime.datetime]):
        deleted (Union[Unset, bool]):
        status (Union[Unset, ComputeEnvStatus]):
        message (Union[Unset, str]):
        primary (Union[Unset, bool]):
        credentials_id (Union[Unset, str]):
        org_id (Union[Unset, int]):
        workspace_id (Union[Unset, int]):
        labels (Union[Unset, List['LabelDbDto']]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    platform: Union[Unset, ComputeEnvResponseDtoPlatform] = UNSET
    config: Union[
        "AWSBatchConfiguration",
        "AltairPBSConfiguration",
        "AmazonEKSClusterConfiguration",
        "AzureBatchConfiguration",
        "GoogleBatchServiceConfiguration",
        "GoogleGKEClusterConfiguration",
        "GoogleLifeSciencesConfiguration",
        "IBMLSFConfiguration",
        "KubernetesComputeConfiguration",
        "MoabConfiguration",
        "SlurmConfiguration",
        "UnivaGridEngineConfiguration",
        Unset,
    ] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    last_used: Union[Unset, datetime.datetime] = UNSET
    deleted: Union[Unset, bool] = UNSET
    status: Union[Unset, ComputeEnvStatus] = UNSET
    message: Union[Unset, str] = UNSET
    primary: Union[Unset, bool] = UNSET
    credentials_id: Union[Unset, str] = UNSET
    org_id: Union[Unset, int] = UNSET
    workspace_id: Union[Unset, int] = UNSET
    labels: Union[Unset, List["LabelDbDto"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.altair_pbs_configuration import AltairPBSConfiguration
        from ..models.amazon_eks_cluster_configuration import AmazonEKSClusterConfiguration
        from ..models.aws_batch_configuration import AWSBatchConfiguration
        from ..models.azure_batch_configuration import AzureBatchConfiguration
        from ..models.google_batch_service_configuration import GoogleBatchServiceConfiguration
        from ..models.google_gke_cluster_configuration import GoogleGKEClusterConfiguration
        from ..models.google_life_sciences_configuration import GoogleLifeSciencesConfiguration
        from ..models.ibmlsf_configuration import IBMLSFConfiguration
        from ..models.kubernetes_compute_configuration import KubernetesComputeConfiguration
        from ..models.slurm_configuration import SlurmConfiguration
        from ..models.univa_grid_engine_configuration import UnivaGridEngineConfiguration

        id = self.id
        name = self.name
        description = self.description
        platform: Union[Unset, str] = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        config: Union[Dict[str, Any], Unset]
        if isinstance(self.config, Unset):
            config = UNSET

        elif isinstance(self.config, AWSBatchConfiguration):
            config = self.config.to_dict()

        elif isinstance(self.config, GoogleLifeSciencesConfiguration):
            config = self.config.to_dict()

        elif isinstance(self.config, GoogleBatchServiceConfiguration):
            config = self.config.to_dict()

        elif isinstance(self.config, AzureBatchConfiguration):
            config = self.config.to_dict()

        elif isinstance(self.config, IBMLSFConfiguration):
            config = self.config.to_dict()

        elif isinstance(self.config, SlurmConfiguration):
            config = self.config.to_dict()

        elif isinstance(self.config, KubernetesComputeConfiguration):
            config = self.config.to_dict()

        elif isinstance(self.config, AmazonEKSClusterConfiguration):
            config = self.config.to_dict()

        elif isinstance(self.config, GoogleGKEClusterConfiguration):
            config = self.config.to_dict()

        elif isinstance(self.config, UnivaGridEngineConfiguration):
            config = self.config.to_dict()

        elif isinstance(self.config, AltairPBSConfiguration):
            config = self.config.to_dict()

        else:
            config = self.config.to_dict()

        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        last_used: Union[Unset, str] = UNSET
        if not isinstance(self.last_used, Unset):
            last_used = self.last_used.isoformat()

        deleted = self.deleted
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        message = self.message
        primary = self.primary
        credentials_id = self.credentials_id
        org_id = self.org_id
        workspace_id = self.workspace_id
        labels: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()

                labels.append(labels_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if platform is not UNSET:
            field_dict["platform"] = platform
        if config is not UNSET:
            field_dict["config"] = config
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if last_used is not UNSET:
            field_dict["lastUsed"] = last_used
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message
        if primary is not UNSET:
            field_dict["primary"] = primary
        if credentials_id is not UNSET:
            field_dict["credentialsId"] = credentials_id
        if org_id is not UNSET:
            field_dict["orgId"] = org_id
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.altair_pbs_configuration import AltairPBSConfiguration
        from ..models.amazon_eks_cluster_configuration import AmazonEKSClusterConfiguration
        from ..models.aws_batch_configuration import AWSBatchConfiguration
        from ..models.azure_batch_configuration import AzureBatchConfiguration
        from ..models.google_batch_service_configuration import GoogleBatchServiceConfiguration
        from ..models.google_gke_cluster_configuration import GoogleGKEClusterConfiguration
        from ..models.google_life_sciences_configuration import GoogleLifeSciencesConfiguration
        from ..models.ibmlsf_configuration import IBMLSFConfiguration
        from ..models.kubernetes_compute_configuration import KubernetesComputeConfiguration
        from ..models.label_db_dto import LabelDbDto
        from ..models.moab_configuration import MoabConfiguration
        from ..models.slurm_configuration import SlurmConfiguration
        from ..models.univa_grid_engine_configuration import UnivaGridEngineConfiguration

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: Union[Unset, ComputeEnvResponseDtoPlatform]
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = ComputeEnvResponseDtoPlatform(_platform)

        def _parse_config(
            data: object,
        ) -> Union[
            "AWSBatchConfiguration",
            "AltairPBSConfiguration",
            "AmazonEKSClusterConfiguration",
            "AzureBatchConfiguration",
            "GoogleBatchServiceConfiguration",
            "GoogleGKEClusterConfiguration",
            "GoogleLifeSciencesConfiguration",
            "IBMLSFConfiguration",
            "KubernetesComputeConfiguration",
            "MoabConfiguration",
            "SlurmConfiguration",
            "UnivaGridEngineConfiguration",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_compute_config_type_0 = AWSBatchConfiguration.from_dict(data)

                return componentsschemas_compute_config_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_compute_config_type_1 = GoogleLifeSciencesConfiguration.from_dict(data)

                return componentsschemas_compute_config_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_compute_config_type_2 = GoogleBatchServiceConfiguration.from_dict(data)

                return componentsschemas_compute_config_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_compute_config_type_3 = AzureBatchConfiguration.from_dict(data)

                return componentsschemas_compute_config_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_compute_config_type_4 = IBMLSFConfiguration.from_dict(data)

                return componentsschemas_compute_config_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_compute_config_type_5 = SlurmConfiguration.from_dict(data)

                return componentsschemas_compute_config_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_compute_config_type_6 = KubernetesComputeConfiguration.from_dict(data)

                return componentsschemas_compute_config_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_compute_config_type_7 = AmazonEKSClusterConfiguration.from_dict(data)

                return componentsschemas_compute_config_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_compute_config_type_8 = GoogleGKEClusterConfiguration.from_dict(data)

                return componentsschemas_compute_config_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_compute_config_type_9 = UnivaGridEngineConfiguration.from_dict(data)

                return componentsschemas_compute_config_type_9
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_compute_config_type_10 = AltairPBSConfiguration.from_dict(data)

                return componentsschemas_compute_config_type_10
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_compute_config_type_11 = MoabConfiguration.from_dict(data)

            return componentsschemas_compute_config_type_11

        config = _parse_config(d.pop("config", UNSET))

        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        _last_used = d.pop("lastUsed", UNSET)
        last_used: Union[Unset, datetime.datetime]
        if isinstance(_last_used, Unset):
            last_used = UNSET
        else:
            last_used = isoparse(_last_used)

        deleted = d.pop("deleted", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ComputeEnvStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ComputeEnvStatus(_status)

        message = d.pop("message", UNSET)

        primary = d.pop("primary", UNSET)

        credentials_id = d.pop("credentialsId", UNSET)

        org_id = d.pop("orgId", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in _labels or []:
            labels_item = LabelDbDto.from_dict(labels_item_data)

            labels.append(labels_item)

        compute_env_response_dto = cls(
            id=id,
            name=name,
            description=description,
            platform=platform,
            config=config,
            date_created=date_created,
            last_updated=last_updated,
            last_used=last_used,
            deleted=deleted,
            status=status,
            message=message,
            primary=primary,
            credentials_id=credentials_id,
            org_id=org_id,
            workspace_id=workspace_id,
            labels=labels,
        )

        compute_env_response_dto.additional_properties = d
        return compute_env_response_dto

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
