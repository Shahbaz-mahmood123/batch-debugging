from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.avatar import Avatar


T = TypeVar("T", bound="CreateAvatarResponse")


@_attrs_define
class CreateAvatarResponse:
    """
    Attributes:
        avatar (Union[Unset, Avatar]):
        url (Union[Unset, str]):
    """

    avatar: Union[Unset, "Avatar"] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        avatar: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_dict()

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.avatar import Avatar

        d = src_dict.copy()
        _avatar = d.pop("avatar", UNSET)
        avatar: Union[Unset, Avatar]
        if isinstance(_avatar, Unset):
            avatar = UNSET
        else:
            avatar = Avatar.from_dict(_avatar)

        url = d.pop("url", UNSET)

        create_avatar_response = cls(
            avatar=avatar,
            url=url,
        )

        create_avatar_response.additional_properties = d
        return create_avatar_response

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
