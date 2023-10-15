from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventType")


@_attrs_define
class EventType:
    """
    Attributes:
        source (Union[Unset, str]):
        display (Union[Unset, str]):
        description (Union[Unset, str]):
        enabled (Union[Unset, bool]):
    """

    source: Union[Unset, str] = UNSET
    display: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source = self.source
        display = self.display
        description = self.description
        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if display is not UNSET:
            field_dict["display"] = display
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source = d.pop("source", UNSET)

        display = d.pop("display", UNSET)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        event_type = cls(
            source=source,
            display=display,
            description=description,
            enabled=enabled,
        )

        event_type.additional_properties = d
        return event_type

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
