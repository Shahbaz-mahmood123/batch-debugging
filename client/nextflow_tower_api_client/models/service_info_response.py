from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_info import ServiceInfo


T = TypeVar("T", bound="ServiceInfoResponse")


@_attrs_define
class ServiceInfoResponse:
    """
    Attributes:
        service_info (Union[Unset, ServiceInfo]):
    """

    service_info: Union[Unset, "ServiceInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.service_info, Unset):
            service_info = self.service_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_info is not UNSET:
            field_dict["serviceInfo"] = service_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.service_info import ServiceInfo

        d = src_dict.copy()
        _service_info = d.pop("serviceInfo", UNSET)
        service_info: Union[Unset, ServiceInfo]
        if isinstance(_service_info, Unset):
            service_info = UNSET
        else:
            service_info = ServiceInfo.from_dict(_service_info)

        service_info_response = cls(
            service_info=service_info,
        )

        service_info_response.additional_properties = d
        return service_info_response

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
