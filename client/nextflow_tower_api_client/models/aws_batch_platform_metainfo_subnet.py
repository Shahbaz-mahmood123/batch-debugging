from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AwsBatchPlatformMetainfoSubnet")


@_attrs_define
class AwsBatchPlatformMetainfoSubnet:
    """
    Attributes:
        id (Union[Unset, str]):
        zone (Union[Unset, str]):
        vpc_id (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    zone: Union[Unset, str] = UNSET
    vpc_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        zone = self.zone
        vpc_id = self.vpc_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if zone is not UNSET:
            field_dict["zone"] = zone
        if vpc_id is not UNSET:
            field_dict["vpcId"] = vpc_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        zone = d.pop("zone", UNSET)

        vpc_id = d.pop("vpcId", UNSET)

        aws_batch_platform_metainfo_subnet = cls(
            id=id,
            zone=zone,
            vpc_id=vpc_id,
        )

        aws_batch_platform_metainfo_subnet.additional_properties = d
        return aws_batch_platform_metainfo_subnet

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
