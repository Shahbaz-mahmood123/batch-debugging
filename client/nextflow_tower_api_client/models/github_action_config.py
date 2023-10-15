from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubActionConfig")


@_attrs_define
class GithubActionConfig:
    """
    Attributes:
        events (Union[Unset, List[str]]):
        discriminator (Union[Unset, str]):
    """

    events: Union[Unset, List[str]] = UNSET
    discriminator: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        events: Union[Unset, List[str]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        discriminator = self.discriminator

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events
        if discriminator is not UNSET:
            field_dict["discriminator"] = discriminator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        events = cast(List[str], d.pop("events", UNSET))

        discriminator = d.pop("discriminator", UNSET)

        github_action_config = cls(
            events=events,
            discriminator=discriminator,
        )

        github_action_config.additional_properties = d
        return github_action_config

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
