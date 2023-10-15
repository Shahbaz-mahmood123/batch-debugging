from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.org_role import OrgRole
from ..models.participant_type import ParticipantType
from ..models.wsp_role import WspRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="ParticipantDbDto")


@_attrs_define
class ParticipantDbDto:
    """
    Attributes:
        user_name (Union[Unset, str]):
        team_id (Union[Unset, int]):
        member_id (Union[Unset, int]):
        participant_id (Union[Unset, int]):
        wsp_role (Union[Unset, WspRole]):
        org_role (Union[Unset, OrgRole]):
        user_avatar_url (Union[Unset, str]):
        team_name (Union[Unset, str]):
        team_avatar_url (Union[Unset, str]):
        email (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        type (Union[Unset, ParticipantType]):
    """

    user_name: Union[Unset, str] = UNSET
    team_id: Union[Unset, int] = UNSET
    member_id: Union[Unset, int] = UNSET
    participant_id: Union[Unset, int] = UNSET
    wsp_role: Union[Unset, WspRole] = UNSET
    org_role: Union[Unset, OrgRole] = UNSET
    user_avatar_url: Union[Unset, str] = UNSET
    team_name: Union[Unset, str] = UNSET
    team_avatar_url: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    type: Union[Unset, ParticipantType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_name = self.user_name
        team_id = self.team_id
        member_id = self.member_id
        participant_id = self.participant_id
        wsp_role: Union[Unset, str] = UNSET
        if not isinstance(self.wsp_role, Unset):
            wsp_role = self.wsp_role.value

        org_role: Union[Unset, str] = UNSET
        if not isinstance(self.org_role, Unset):
            org_role = self.org_role.value

        user_avatar_url = self.user_avatar_url
        team_name = self.team_name
        team_avatar_url = self.team_avatar_url
        email = self.email
        first_name = self.first_name
        last_name = self.last_name
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if member_id is not UNSET:
            field_dict["memberId"] = member_id
        if participant_id is not UNSET:
            field_dict["participantId"] = participant_id
        if wsp_role is not UNSET:
            field_dict["wspRole"] = wsp_role
        if org_role is not UNSET:
            field_dict["orgRole"] = org_role
        if user_avatar_url is not UNSET:
            field_dict["userAvatarUrl"] = user_avatar_url
        if team_name is not UNSET:
            field_dict["teamName"] = team_name
        if team_avatar_url is not UNSET:
            field_dict["teamAvatarUrl"] = team_avatar_url
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_name = d.pop("userName", UNSET)

        team_id = d.pop("teamId", UNSET)

        member_id = d.pop("memberId", UNSET)

        participant_id = d.pop("participantId", UNSET)

        _wsp_role = d.pop("wspRole", UNSET)
        wsp_role: Union[Unset, WspRole]
        if isinstance(_wsp_role, Unset):
            wsp_role = UNSET
        else:
            wsp_role = WspRole(_wsp_role)

        _org_role = d.pop("orgRole", UNSET)
        org_role: Union[Unset, OrgRole]
        if isinstance(_org_role, Unset):
            org_role = UNSET
        else:
            org_role = OrgRole(_org_role)

        user_avatar_url = d.pop("userAvatarUrl", UNSET)

        team_name = d.pop("teamName", UNSET)

        team_avatar_url = d.pop("teamAvatarUrl", UNSET)

        email = d.pop("email", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ParticipantType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ParticipantType(_type)

        participant_db_dto = cls(
            user_name=user_name,
            team_id=team_id,
            member_id=member_id,
            participant_id=participant_id,
            wsp_role=wsp_role,
            org_role=org_role,
            user_avatar_url=user_avatar_url,
            team_name=team_name,
            team_avatar_url=team_avatar_url,
            email=email,
            first_name=first_name,
            last_name=last_name,
            type=type,
        )

        participant_db_dto.additional_properties = d
        return participant_db_dto

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
