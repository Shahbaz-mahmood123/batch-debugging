from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateLabelResponse")


@_attrs_define
class UpdateLabelResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        value (Union[Unset, str]):
        is_default (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    is_default: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        value = self.value
        is_default = self.is_default

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        value = d.pop("value", UNSET)

        is_default = d.pop("isDefault", UNSET)

        update_label_response = cls(
            id=id,
            name=name,
            value=value,
            is_default=is_default,
        )

        update_label_response.additional_properties = d
        return update_label_response

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
