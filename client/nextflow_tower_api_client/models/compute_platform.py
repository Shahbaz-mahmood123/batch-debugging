from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComputePlatform")


@_attrs_define
class ComputePlatform:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        credentials_providers (Union[Unset, List[str]]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    credentials_providers: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        credentials_providers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.credentials_providers, Unset):
            credentials_providers = self.credentials_providers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if credentials_providers is not UNSET:
            field_dict["credentialsProviders"] = credentials_providers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        credentials_providers = cast(List[str], d.pop("credentialsProviders", UNSET))

        compute_platform = cls(
            id=id,
            name=name,
            credentials_providers=credentials_providers,
        )

        compute_platform.additional_properties = d
        return compute_platform

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
