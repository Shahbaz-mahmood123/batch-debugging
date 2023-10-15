from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workspace_db_dto import WorkspaceDbDto


T = TypeVar("T", bound="ListWorkspacesResponse")


@_attrs_define
class ListWorkspacesResponse:
    """
    Attributes:
        workspaces (Union[Unset, List['WorkspaceDbDto']]):
    """

    workspaces: Union[Unset, List["WorkspaceDbDto"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        workspaces: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.workspaces, Unset):
            workspaces = []
            for workspaces_item_data in self.workspaces:
                workspaces_item = workspaces_item_data.to_dict()

                workspaces.append(workspaces_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workspaces is not UNSET:
            field_dict["workspaces"] = workspaces

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.workspace_db_dto import WorkspaceDbDto

        d = src_dict.copy()
        workspaces = []
        _workspaces = d.pop("workspaces", UNSET)
        for workspaces_item_data in _workspaces or []:
            workspaces_item = WorkspaceDbDto.from_dict(workspaces_item_data)

            workspaces.append(workspaces_item)

        list_workspaces_response = cls(
            workspaces=workspaces,
        )

        list_workspaces_response.additional_properties = d
        return list_workspaces_response

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
