from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AzureSecurityKeys")


@_attrs_define
class AzureSecurityKeys:
    """
    Attributes:
        batch_name (Union[Unset, str]):
        batch_key (Union[Unset, str]):
        storage_name (Union[Unset, str]):
        storage_key (Union[Unset, str]):
        discriminator (Union[Unset, str]):
    """

    batch_name: Union[Unset, str] = UNSET
    batch_key: Union[Unset, str] = UNSET
    storage_name: Union[Unset, str] = UNSET
    storage_key: Union[Unset, str] = UNSET
    discriminator: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        batch_name = self.batch_name
        batch_key = self.batch_key
        storage_name = self.storage_name
        storage_key = self.storage_key
        discriminator = self.discriminator

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if batch_name is not UNSET:
            field_dict["batchName"] = batch_name
        if batch_key is not UNSET:
            field_dict["batchKey"] = batch_key
        if storage_name is not UNSET:
            field_dict["storageName"] = storage_name
        if storage_key is not UNSET:
            field_dict["storageKey"] = storage_key
        if discriminator is not UNSET:
            field_dict["discriminator"] = discriminator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        batch_name = d.pop("batchName", UNSET)

        batch_key = d.pop("batchKey", UNSET)

        storage_name = d.pop("storageName", UNSET)

        storage_key = d.pop("storageKey", UNSET)

        discriminator = d.pop("discriminator", UNSET)

        azure_security_keys = cls(
            batch_name=batch_name,
            batch_key=batch_key,
            storage_name=storage_name,
            storage_key=storage_key,
            discriminator=discriminator,
        )

        azure_security_keys.additional_properties = d
        return azure_security_keys

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
