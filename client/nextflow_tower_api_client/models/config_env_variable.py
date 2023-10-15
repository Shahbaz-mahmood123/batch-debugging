from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigEnvVariable")


@_attrs_define
class ConfigEnvVariable:
    """
    Attributes:
        name (Union[Unset, str]):
        value (Union[Unset, str]):
        head (Union[Unset, bool]):
        compute (Union[Unset, bool]):
    """

    name: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    head: Union[Unset, bool] = UNSET
    compute: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        value = self.value
        head = self.head
        compute = self.compute

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value
        if head is not UNSET:
            field_dict["head"] = head
        if compute is not UNSET:
            field_dict["compute"] = compute

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        value = d.pop("value", UNSET)

        head = d.pop("head", UNSET)

        compute = d.pop("compute", UNSET)

        config_env_variable = cls(
            name=name,
            value=value,
            head=head,
            compute=compute,
        )

        config_env_variable.additional_properties = d
        return config_env_variable

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
