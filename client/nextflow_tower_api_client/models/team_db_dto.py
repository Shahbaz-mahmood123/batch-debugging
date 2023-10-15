from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamDbDto")


@_attrs_define
class TeamDbDto:
    """
    Attributes:
        description (Union[Unset, str]):
        avatar_url (Union[Unset, str]):
        team_id (Union[Unset, int]):
        members_count (Union[Unset, int]):
        name (Union[Unset, str]):
    """

    description: Union[Unset, str] = UNSET
    avatar_url: Union[Unset, str] = UNSET
    team_id: Union[Unset, int] = UNSET
    members_count: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        avatar_url = self.avatar_url
        team_id = self.team_id
        members_count = self.members_count
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if members_count is not UNSET:
            field_dict["membersCount"] = members_count
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        avatar_url = d.pop("avatarUrl", UNSET)

        team_id = d.pop("teamId", UNSET)

        members_count = d.pop("membersCount", UNSET)

        name = d.pop("name", UNSET)

        team_db_dto = cls(
            description=description,
            avatar_url=avatar_url,
            team_id=team_id,
            members_count=members_count,
            name=name,
        )

        team_db_dto.additional_properties = d
        return team_db_dto

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
