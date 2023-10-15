from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.log_page import LogPage


T = TypeVar("T", bound="WorkflowLogResponse")


@_attrs_define
class WorkflowLogResponse:
    """
    Attributes:
        log (Union[Unset, LogPage]):
    """

    log: Union[Unset, "LogPage"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        log: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.log, Unset):
            log = self.log.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if log is not UNSET:
            field_dict["log"] = log

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.log_page import LogPage

        d = src_dict.copy()
        _log = d.pop("log", UNSET)
        log: Union[Unset, LogPage]
        if isinstance(_log, Unset):
            log = UNSET
        else:
            log = LogPage.from_dict(_log)

        workflow_log_response = cls(
            log=log,
        )

        workflow_log_response.additional_properties = d
        return workflow_log_response

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
