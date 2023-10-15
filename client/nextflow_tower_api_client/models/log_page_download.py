from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LogPageDownload")


@_attrs_define
class LogPageDownload:
    """
    Attributes:
        file_name (Union[Unset, str]):
        display_text (Union[Unset, str]):
        save_name (Union[Unset, str]):
    """

    file_name: Union[Unset, str] = UNSET
    display_text: Union[Unset, str] = UNSET
    save_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file_name = self.file_name
        display_text = self.display_text
        save_name = self.save_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if display_text is not UNSET:
            field_dict["displayText"] = display_text
        if save_name is not UNSET:
            field_dict["saveName"] = save_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file_name = d.pop("fileName", UNSET)

        display_text = d.pop("displayText", UNSET)

        save_name = d.pop("saveName", UNSET)

        log_page_download = cls(
            file_name=file_name,
            display_text=display_text,
            save_name=save_name,
        )

        log_page_download.additional_properties = d
        return log_page_download

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
