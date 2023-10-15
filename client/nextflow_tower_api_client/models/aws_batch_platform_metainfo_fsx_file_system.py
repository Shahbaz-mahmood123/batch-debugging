from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AwsBatchPlatformMetainfoFsxFileSystem")


@_attrs_define
class AwsBatchPlatformMetainfoFsxFileSystem:
    """
    Attributes:
        id (Union[Unset, str]):
        dns (Union[Unset, str]):
        mount (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    dns: Union[Unset, str] = UNSET
    mount: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        dns = self.dns
        mount = self.mount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if dns is not UNSET:
            field_dict["dns"] = dns
        if mount is not UNSET:
            field_dict["mount"] = mount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        dns = d.pop("dns", UNSET)

        mount = d.pop("mount", UNSET)

        aws_batch_platform_metainfo_fsx_file_system = cls(
            id=id,
            dns=dns,
            mount=mount,
        )

        aws_batch_platform_metainfo_fsx_file_system.additional_properties = d
        return aws_batch_platform_metainfo_fsx_file_system

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
