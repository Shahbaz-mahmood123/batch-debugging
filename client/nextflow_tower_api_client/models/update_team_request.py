from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTeamRequest")


@_attrs_define
class UpdateTeamRequest:
    """
    Attributes:
        description (Union[Unset, str]):
        avatar_id (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    description: Union[Unset, str] = UNSET
    avatar_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        avatar_id = self.avatar_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if avatar_id is not UNSET:
            field_dict["avatarId"] = avatar_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        avatar_id = d.pop("avatarId", UNSET)

        name = d.pop("name", UNSET)

        update_team_request = cls(
            description=description,
            avatar_id=avatar_id,
            name=name,
        )

        update_team_request.additional_properties = d
        return update_team_request

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
