from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow import Workflow


T = TypeVar("T", bound="TraceBeginRequest")


@_attrs_define
class TraceBeginRequest:
    """
    Attributes:
        workflow (Union[Unset, Workflow]):
        process_names (Union[Unset, List[str]]):
        tower_launch (Union[Unset, bool]):
    """

    workflow: Union[Unset, "Workflow"] = UNSET
    process_names: Union[Unset, List[str]] = UNSET
    tower_launch: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        workflow: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        process_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.process_names, Unset):
            process_names = self.process_names

        tower_launch = self.tower_launch

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if process_names is not UNSET:
            field_dict["processNames"] = process_names
        if tower_launch is not UNSET:
            field_dict["towerLaunch"] = tower_launch

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.workflow import Workflow

        d = src_dict.copy()
        _workflow = d.pop("workflow", UNSET)
        workflow: Union[Unset, Workflow]
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = Workflow.from_dict(_workflow)

        process_names = cast(List[str], d.pop("processNames", UNSET))

        tower_launch = d.pop("towerLaunch", UNSET)

        trace_begin_request = cls(
            workflow=workflow,
            process_names=process_names,
            tower_launch=tower_launch,
        )

        trace_begin_request.additional_properties = d
        return trace_begin_request

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
