from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trace_progress_data import TraceProgressData


T = TypeVar("T", bound="TraceHeartbeatRequest")


@_attrs_define
class TraceHeartbeatRequest:
    """
    Attributes:
        progress (Union[Unset, TraceProgressData]):
    """

    progress: Union[Unset, "TraceProgressData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        progress: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.progress, Unset):
            progress = self.progress.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if progress is not UNSET:
            field_dict["progress"] = progress

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.trace_progress_data import TraceProgressData

        d = src_dict.copy()
        _progress = d.pop("progress", UNSET)
        progress: Union[Unset, TraceProgressData]
        if isinstance(_progress, Unset):
            progress = UNSET
        else:
            progress = TraceProgressData.from_dict(_progress)

        trace_heartbeat_request = cls(
            progress=progress,
        )

        trace_heartbeat_request.additional_properties = d
        return trace_heartbeat_request

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
