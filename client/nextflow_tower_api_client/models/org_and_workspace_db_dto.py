from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.visibility import Visibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgAndWorkspaceDbDto")


@_attrs_define
class OrgAndWorkspaceDbDto:
    """
    Attributes:
        org_id (Union[Unset, int]):
        org_name (Union[Unset, str]):
        org_logo_url (Union[Unset, str]):
        workspace_id (Union[Unset, int]):
        workspace_name (Union[Unset, str]):
        workspace_full_name (Union[Unset, str]):
        visibility (Union[Unset, Visibility]):
    """

    org_id: Union[Unset, int] = UNSET
    org_name: Union[Unset, str] = UNSET
    org_logo_url: Union[Unset, str] = UNSET
    workspace_id: Union[Unset, int] = UNSET
    workspace_name: Union[Unset, str] = UNSET
    workspace_full_name: Union[Unset, str] = UNSET
    visibility: Union[Unset, Visibility] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        org_id = self.org_id
        org_name = self.org_name
        org_logo_url = self.org_logo_url
        workspace_id = self.workspace_id
        workspace_name = self.workspace_name
        workspace_full_name = self.workspace_full_name
        visibility: Union[Unset, str] = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if org_id is not UNSET:
            field_dict["orgId"] = org_id
        if org_name is not UNSET:
            field_dict["orgName"] = org_name
        if org_logo_url is not UNSET:
            field_dict["orgLogoUrl"] = org_logo_url
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if workspace_name is not UNSET:
            field_dict["workspaceName"] = workspace_name
        if workspace_full_name is not UNSET:
            field_dict["workspaceFullName"] = workspace_full_name
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        org_id = d.pop("orgId", UNSET)

        org_name = d.pop("orgName", UNSET)

        org_logo_url = d.pop("orgLogoUrl", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        workspace_name = d.pop("workspaceName", UNSET)

        workspace_full_name = d.pop("workspaceFullName", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: Union[Unset, Visibility]
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = Visibility(_visibility)

        org_and_workspace_db_dto = cls(
            org_id=org_id,
            org_name=org_name,
            org_logo_url=org_logo_url,
            workspace_id=workspace_id,
            workspace_name=workspace_name,
            workspace_full_name=workspace_full_name,
            visibility=visibility,
        )

        org_and_workspace_db_dto.additional_properties = d
        return org_and_workspace_db_dto

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
