from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.member_db_dto import MemberDbDto


T = TypeVar("T", bound="AddMemberResponse")


@_attrs_define
class AddMemberResponse:
    """
    Attributes:
        member (Union[Unset, MemberDbDto]):
    """

    member: Union[Unset, "MemberDbDto"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        member: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.member, Unset):
            member = self.member.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if member is not UNSET:
            field_dict["member"] = member

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.member_db_dto import MemberDbDto

        d = src_dict.copy()
        _member = d.pop("member", UNSET)
        member: Union[Unset, MemberDbDto]
        if isinstance(_member, Unset):
            member = UNSET
        else:
            member = MemberDbDto.from_dict(_member)

        add_member_response = cls(
            member=member,
        )

        add_member_response.additional_properties = d
        return add_member_response

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
