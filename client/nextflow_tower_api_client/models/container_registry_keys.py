from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContainerRegistryKeys")


@_attrs_define
class ContainerRegistryKeys:
    """
    Attributes:
        user_name (Union[Unset, str]):
        password (Union[Unset, str]):
        registry (Union[Unset, str]):
        discriminator (Union[Unset, str]):
    """

    user_name: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    registry: Union[Unset, str] = UNSET
    discriminator: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_name = self.user_name
        password = self.password
        registry = self.registry
        discriminator = self.discriminator

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if password is not UNSET:
            field_dict["password"] = password
        if registry is not UNSET:
            field_dict["registry"] = registry
        if discriminator is not UNSET:
            field_dict["discriminator"] = discriminator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_name = d.pop("userName", UNSET)

        password = d.pop("password", UNSET)

        registry = d.pop("registry", UNSET)

        discriminator = d.pop("discriminator", UNSET)

        container_registry_keys = cls(
            user_name=user_name,
            password=password,
            registry=registry,
            discriminator=discriminator,
        )

        container_registry_keys.additional_properties = d
        return container_registry_keys

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
