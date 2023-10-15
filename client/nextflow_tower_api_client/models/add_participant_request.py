from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddParticipantRequest")


@_attrs_define
class AddParticipantRequest:
    """
    Attributes:
        team_id (Union[Unset, int]):
        member_id (Union[Unset, int]):
        user_name_or_email (Union[Unset, str]):
    """

    team_id: Union[Unset, int] = UNSET
    member_id: Union[Unset, int] = UNSET
    user_name_or_email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team_id = self.team_id
        member_id = self.member_id
        user_name_or_email = self.user_name_or_email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if member_id is not UNSET:
            field_dict["memberId"] = member_id
        if user_name_or_email is not UNSET:
            field_dict["userNameOrEmail"] = user_name_or_email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        team_id = d.pop("teamId", UNSET)

        member_id = d.pop("memberId", UNSET)

        user_name_or_email = d.pop("userNameOrEmail", UNSET)

        add_participant_request = cls(
            team_id=team_id,
            member_id=member_id,
            user_name_or_email=user_name_or_email,
        )

        add_participant_request.additional_properties = d
        return add_participant_request

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
