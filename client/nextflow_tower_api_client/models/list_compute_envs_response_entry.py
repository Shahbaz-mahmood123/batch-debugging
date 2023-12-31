import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.compute_env_status import ComputeEnvStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListComputeEnvsResponseEntry")


@_attrs_define
class ListComputeEnvsResponseEntry:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        platform (Union[Unset, str]):
        status (Union[Unset, ComputeEnvStatus]):
        message (Union[Unset, str]):
        last_used (Union[Unset, datetime.datetime]):
        primary (Union[Unset, bool]):
        workspace_name (Union[Unset, str]):
        visibility (Union[Unset, str]):
        work_dir (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    platform: Union[Unset, str] = UNSET
    status: Union[Unset, ComputeEnvStatus] = UNSET
    message: Union[Unset, str] = UNSET
    last_used: Union[Unset, datetime.datetime] = UNSET
    primary: Union[Unset, bool] = UNSET
    workspace_name: Union[Unset, str] = UNSET
    visibility: Union[Unset, str] = UNSET
    work_dir: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        platform = self.platform
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        message = self.message
        last_used: Union[Unset, str] = UNSET
        if not isinstance(self.last_used, Unset):
            last_used = self.last_used.isoformat()

        primary = self.primary
        workspace_name = self.workspace_name
        visibility = self.visibility
        work_dir = self.work_dir

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if platform is not UNSET:
            field_dict["platform"] = platform
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message
        if last_used is not UNSET:
            field_dict["lastUsed"] = last_used
        if primary is not UNSET:
            field_dict["primary"] = primary
        if workspace_name is not UNSET:
            field_dict["workspaceName"] = workspace_name
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if work_dir is not UNSET:
            field_dict["workDir"] = work_dir

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        platform = d.pop("platform", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ComputeEnvStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ComputeEnvStatus(_status)

        message = d.pop("message", UNSET)

        _last_used = d.pop("lastUsed", UNSET)
        last_used: Union[Unset, datetime.datetime]
        if isinstance(_last_used, Unset):
            last_used = UNSET
        else:
            last_used = isoparse(_last_used)

        primary = d.pop("primary", UNSET)

        workspace_name = d.pop("workspaceName", UNSET)

        visibility = d.pop("visibility", UNSET)

        work_dir = d.pop("workDir", UNSET)

        list_compute_envs_response_entry = cls(
            id=id,
            name=name,
            platform=platform,
            status=status,
            message=message,
            last_used=last_used,
            primary=primary,
            workspace_name=workspace_name,
            visibility=visibility,
            work_dir=work_dir,
        )

        list_compute_envs_response_entry.additional_properties = d
        return list_compute_envs_response_entry

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
