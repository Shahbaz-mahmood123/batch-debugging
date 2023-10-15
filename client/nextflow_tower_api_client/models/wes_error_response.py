from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WesErrorResponse")


@_attrs_define
class WesErrorResponse:
    """
    Attributes:
        msg (Union[Unset, str]):
        status_code (Union[Unset, int]):
    """

    msg: Union[Unset, str] = UNSET
    status_code: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        msg = self.msg
        status_code = self.status_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if msg is not UNSET:
            field_dict["msg"] = msg
        if status_code is not UNSET:
            field_dict["status_code"] = status_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        msg = d.pop("msg", UNSET)

        status_code = d.pop("status_code", UNSET)

        wes_error_response = cls(
            msg=msg,
            status_code=status_code,
        )

        wes_error_response.additional_properties = d
        return wes_error_response

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
