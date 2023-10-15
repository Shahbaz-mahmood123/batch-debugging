from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.org_and_workspace_db_dto import OrgAndWorkspaceDbDto


T = TypeVar("T", bound="ListWorkspacesAndOrgResponse")


@_attrs_define
class ListWorkspacesAndOrgResponse:
    """
    Attributes:
        orgs_and_workspaces (Union[Unset, List['OrgAndWorkspaceDbDto']]):
    """

    orgs_and_workspaces: Union[Unset, List["OrgAndWorkspaceDbDto"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        orgs_and_workspaces: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.orgs_and_workspaces, Unset):
            orgs_and_workspaces = []
            for orgs_and_workspaces_item_data in self.orgs_and_workspaces:
                orgs_and_workspaces_item = orgs_and_workspaces_item_data.to_dict()

                orgs_and_workspaces.append(orgs_and_workspaces_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if orgs_and_workspaces is not UNSET:
            field_dict["orgsAndWorkspaces"] = orgs_and_workspaces

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.org_and_workspace_db_dto import OrgAndWorkspaceDbDto

        d = src_dict.copy()
        orgs_and_workspaces = []
        _orgs_and_workspaces = d.pop("orgsAndWorkspaces", UNSET)
        for orgs_and_workspaces_item_data in _orgs_and_workspaces or []:
            orgs_and_workspaces_item = OrgAndWorkspaceDbDto.from_dict(orgs_and_workspaces_item_data)

            orgs_and_workspaces.append(orgs_and_workspaces_item)

        list_workspaces_and_org_response = cls(
            orgs_and_workspaces=orgs_and_workspaces,
        )

        list_workspaces_and_org_response.additional_properties = d
        return list_workspaces_and_org_response

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
