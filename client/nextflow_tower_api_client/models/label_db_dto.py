from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LabelDbDto")


@_attrs_define
class LabelDbDto:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        value (Union[Unset, str]):
        resource (Union[Unset, bool]):
        is_default (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    resource: Union[Unset, bool] = UNSET
    is_default: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        value = self.value
        resource = self.resource
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
        if resource is not UNSET:
            field_dict["resource"] = resource
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        value = d.pop("value", UNSET)

        resource = d.pop("resource", UNSET)

        is_default = d.pop("isDefault", UNSET)

        label_db_dto = cls(
            id=id,
            name=name,
            value=value,
            resource=resource,
            is_default=is_default,
        )

        label_db_dto.additional_properties = d
        return label_db_dto

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
