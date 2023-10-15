from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleSecurityKeys")


@_attrs_define
class GoogleSecurityKeys:
    """
    Attributes:
        data (Union[Unset, str]):
        discriminator (Union[Unset, str]):
    """

    data: Union[Unset, str] = UNSET
    discriminator: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data
        discriminator = self.discriminator

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if discriminator is not UNSET:
            field_dict["discriminator"] = discriminator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data = d.pop("data", UNSET)

        discriminator = d.pop("discriminator", UNSET)

        google_security_keys = cls(
            data=data,
            discriminator=discriminator,
        )

        google_security_keys.additional_properties = d
        return google_security_keys

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
