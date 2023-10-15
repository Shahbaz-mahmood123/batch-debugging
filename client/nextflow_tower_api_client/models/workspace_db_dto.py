from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.visibility import Visibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkspaceDbDto")


@_attrs_define
class WorkspaceDbDto:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        full_name (Union[Unset, str]):
        description (Union[Unset, str]):
        visibility (Union[Unset, Visibility]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    visibility: Union[Unset, Visibility] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        full_name = self.full_name
        description = self.description
        visibility: Union[Unset, str] = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if description is not UNSET:
            field_dict["description"] = description
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        full_name = d.pop("fullName", UNSET)

        description = d.pop("description", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: Union[Unset, Visibility]
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = Visibility(_visibility)

        workspace_db_dto = cls(
            id=id,
            name=name,
            full_name=full_name,
            description=description,
            visibility=visibility,
        )

        workspace_db_dto.additional_properties = d
        return workspace_db_dto

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
