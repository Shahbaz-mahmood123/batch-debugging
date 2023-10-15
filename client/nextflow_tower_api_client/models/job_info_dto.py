from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobInfoDto")


@_attrs_define
class JobInfoDto:
    """
    Attributes:
        operation_id (Union[Unset, str]):
        id (Union[Unset, int]):
        status (Union[Unset, str]):
        message (Union[Unset, str]):
        exit_code (Union[Unset, int]):
    """

    operation_id: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    status: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    exit_code: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation_id = self.operation_id
        id = self.id
        status = self.status
        message = self.message
        exit_code = self.exit_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operation_id is not UNSET:
            field_dict["operationId"] = operation_id
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message
        if exit_code is not UNSET:
            field_dict["exitCode"] = exit_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        operation_id = d.pop("operationId", UNSET)

        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        message = d.pop("message", UNSET)

        exit_code = d.pop("exitCode", UNSET)

        job_info_dto = cls(
            operation_id=operation_id,
            id=id,
            status=status,
            message=message,
            exit_code=exit_code,
        )

        job_info_dto.additional_properties = d
        return job_info_dto

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
