from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compute_platform import ComputePlatform


T = TypeVar("T", bound="ListPlatformsResponse")


@_attrs_define
class ListPlatformsResponse:
    """
    Attributes:
        platforms (Union[Unset, List['ComputePlatform']]):
    """

    platforms: Union[Unset, List["ComputePlatform"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        platforms: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.platforms, Unset):
            platforms = []
            for platforms_item_data in self.platforms:
                platforms_item = platforms_item_data.to_dict()

                platforms.append(platforms_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if platforms is not UNSET:
            field_dict["platforms"] = platforms

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.compute_platform import ComputePlatform

        d = src_dict.copy()
        platforms = []
        _platforms = d.pop("platforms", UNSET)
        for platforms_item_data in _platforms or []:
            platforms_item = ComputePlatform.from_dict(platforms_item_data)

            platforms.append(platforms_item)

        list_platforms_response = cls(
            platforms=platforms,
        )

        list_platforms_response.additional_properties = d
        return list_platforms_response

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
