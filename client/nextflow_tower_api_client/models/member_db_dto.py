from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.org_role import OrgRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="MemberDbDto")


@_attrs_define
class MemberDbDto:
    """
    Attributes:
        avatar (Union[Unset, str]):
        user_name (Union[Unset, str]):
        email (Union[Unset, str]):
        member_id (Union[Unset, int]):
        user_id (Union[Unset, int]):
        role (Union[Unset, OrgRole]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
    """

    avatar: Union[Unset, str] = UNSET
    user_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    member_id: Union[Unset, int] = UNSET
    user_id: Union[Unset, int] = UNSET
    role: Union[Unset, OrgRole] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        avatar = self.avatar
        user_name = self.user_name
        email = self.email
        member_id = self.member_id
        user_id = self.user_id
        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        first_name = self.first_name
        last_name = self.last_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if email is not UNSET:
            field_dict["email"] = email
        if member_id is not UNSET:
            field_dict["memberId"] = member_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if role is not UNSET:
            field_dict["role"] = role
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        avatar = d.pop("avatar", UNSET)

        user_name = d.pop("userName", UNSET)

        email = d.pop("email", UNSET)

        member_id = d.pop("memberId", UNSET)

        user_id = d.pop("userId", UNSET)

        _role = d.pop("role", UNSET)
        role: Union[Unset, OrgRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = OrgRole(_role)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        member_db_dto = cls(
            avatar=avatar,
            user_name=user_name,
            email=email,
            member_id=member_id,
            user_id=user_id,
            role=role,
            first_name=first_name,
            last_name=last_name,
        )

        member_db_dto.additional_properties = d
        return member_db_dto

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
