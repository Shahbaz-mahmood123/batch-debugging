from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trace_processing_status import TraceProcessingStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceBeginResponse")


@_attrs_define
class TraceBeginResponse:
    """
    Attributes:
        status (Union[Unset, TraceProcessingStatus]):
        workflow_id (Union[Unset, str]):
        watch_url (Union[Unset, str]):
    """

    status: Union[Unset, TraceProcessingStatus] = UNSET
    workflow_id: Union[Unset, str] = UNSET
    watch_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        workflow_id = self.workflow_id
        watch_url = self.watch_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if workflow_id is not UNSET:
            field_dict["workflowId"] = workflow_id
        if watch_url is not UNSET:
            field_dict["watchUrl"] = watch_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, TraceProcessingStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TraceProcessingStatus(_status)

        workflow_id = d.pop("workflowId", UNSET)

        watch_url = d.pop("watchUrl", UNSET)

        trace_begin_response = cls(
            status=status,
            workflow_id=workflow_id,
            watch_url=watch_url,
        )

        trace_begin_response.additional_properties = d
        return trace_begin_response

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
