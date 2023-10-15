from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AzBatchForgeConfig")


@_attrs_define
class AzBatchForgeConfig:
    """
    Attributes:
        vm_type (Union[Unset, str]):
        vm_count (Union[Unset, int]):
        auto_scale (Union[Unset, bool]):
        dispose_on_deletion (Union[Unset, bool]):
        container_reg_ids (Union[Unset, List[str]]):
    """

    vm_type: Union[Unset, str] = UNSET
    vm_count: Union[Unset, int] = UNSET
    auto_scale: Union[Unset, bool] = UNSET
    dispose_on_deletion: Union[Unset, bool] = UNSET
    container_reg_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vm_type = self.vm_type
        vm_count = self.vm_count
        auto_scale = self.auto_scale
        dispose_on_deletion = self.dispose_on_deletion
        container_reg_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.container_reg_ids, Unset):
            container_reg_ids = self.container_reg_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vm_type is not UNSET:
            field_dict["vmType"] = vm_type
        if vm_count is not UNSET:
            field_dict["vmCount"] = vm_count
        if auto_scale is not UNSET:
            field_dict["autoScale"] = auto_scale
        if dispose_on_deletion is not UNSET:
            field_dict["disposeOnDeletion"] = dispose_on_deletion
        if container_reg_ids is not UNSET:
            field_dict["containerRegIds"] = container_reg_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vm_type = d.pop("vmType", UNSET)

        vm_count = d.pop("vmCount", UNSET)

        auto_scale = d.pop("autoScale", UNSET)

        dispose_on_deletion = d.pop("disposeOnDeletion", UNSET)

        container_reg_ids = cast(List[str], d.pop("containerRegIds", UNSET))

        az_batch_forge_config = cls(
            vm_type=vm_type,
            vm_count=vm_count,
            auto_scale=auto_scale,
            dispose_on_deletion=dispose_on_deletion,
            container_reg_ids=container_reg_ids,
        )

        az_batch_forge_config.additional_properties = d
        return az_batch_forge_config

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
