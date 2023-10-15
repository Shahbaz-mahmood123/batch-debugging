from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.org_role import OrgRole

T = TypeVar("T", bound="MemberDbDto")


@_attrs_define
class MemberDbDto:
    """
    Attributes:
        user_name (str):
        member_id (int):
        user_id (int):
        avatar (str):
        role (OrgRole):
        email (str):
        first_name (str):
        last_name (str):
    """

    user_name: str
    member_id: int
    user_id: int
    avatar: str
    role: OrgRole
    email: str
    first_name: str
    last_name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_name = self.user_name
        member_id = self.member_id
        user_id = self.user_id
        avatar = self.avatar
        role = self.role.value

        email = self.email
        first_name = self.first_name
        last_name = self.last_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userName": user_name,
                "memberId": member_id,
                "userId": user_id,
                "avatar": avatar,
                "role": role,
                "email": email,
                "firstName": first_name,
                "lastName": last_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_name = d.pop("userName")

        member_id = d.pop("memberId")

        user_id = d.pop("userId")

        avatar = d.pop("avatar")

        role = OrgRole(d.pop("role"))

        email = d.pop("email")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        member_db_dto = cls(
            user_name=user_name,
            member_id=member_id,
            user_id=user_id,
            avatar=avatar,
            role=role,
            email=email,
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
