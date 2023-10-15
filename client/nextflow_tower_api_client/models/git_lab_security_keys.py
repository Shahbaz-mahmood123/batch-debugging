from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitLabSecurityKeys")


@_attrs_define
class GitLabSecurityKeys:
    """
    Attributes:
        username (Union[Unset, str]):
        password (Union[Unset, str]):
        token (Union[Unset, str]):
        discriminator (Union[Unset, str]):
    """

    username: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    discriminator: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        password = self.password
        token = self.token
        discriminator = self.discriminator

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if token is not UNSET:
            field_dict["token"] = token
        if discriminator is not UNSET:
            field_dict["discriminator"] = discriminator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        token = d.pop("token", UNSET)

        discriminator = d.pop("discriminator", UNSET)

        git_lab_security_keys = cls(
            username=username,
            password=password,
            token=token,
            discriminator=discriminator,
        )

        git_lab_security_keys.additional_properties = d
        return git_lab_security_keys

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
