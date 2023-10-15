from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.navbar_config_navbar_menu import NavbarConfigNavbarMenu


T = TypeVar("T", bound="NavbarConfig")


@_attrs_define
class NavbarConfig:
    """
    Attributes:
        menus (Union[Unset, List['NavbarConfigNavbarMenu']]):
    """

    menus: Union[Unset, List["NavbarConfigNavbarMenu"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        menus: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.menus, Unset):
            menus = []
            for menus_item_data in self.menus:
                menus_item = menus_item_data.to_dict()

                menus.append(menus_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if menus is not UNSET:
            field_dict["menus"] = menus

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.navbar_config_navbar_menu import NavbarConfigNavbarMenu

        d = src_dict.copy()
        menus = []
        _menus = d.pop("menus", UNSET)
        for menus_item_data in _menus or []:
            menus_item = NavbarConfigNavbarMenu.from_dict(menus_item_data)

            menus.append(menus_item)

        navbar_config = cls(
            menus=menus,
        )

        navbar_config.additional_properties = d
        return navbar_config

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
