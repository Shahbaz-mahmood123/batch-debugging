from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.member_db_dto import MemberDbDto


T = TypeVar("T", bound="ListMembersResponse")


@_attrs_define
class ListMembersResponse:
    """
    Attributes:
        total_size (Union[Unset, int]):
        members (Union[Unset, List['MemberDbDto']]):
    """

    total_size: Union[Unset, int] = UNSET
    members: Union[Unset, List["MemberDbDto"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_size = self.total_size
        members: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()

                members.append(members_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_size is not UNSET:
            field_dict["totalSize"] = total_size
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.member_db_dto import MemberDbDto

        d = src_dict.copy()
        total_size = d.pop("totalSize", UNSET)

        members = []
        _members = d.pop("members", UNSET)
        for members_item_data in _members or []:
            members_item = MemberDbDto.from_dict(members_item_data)

            members.append(members_item)

        list_members_response = cls(
            total_size=total_size,
            members=members,
        )

        list_members_response.additional_properties = d
        return list_members_response

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
