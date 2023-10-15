from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trace_progress_data import TraceProgressData
    from ..models.workflow import Workflow
    from ..models.workflow_metrics import WorkflowMetrics


T = TypeVar("T", bound="TraceCompleteRequest")


@_attrs_define
class TraceCompleteRequest:
    """
    Attributes:
        workflow (Union[Unset, Workflow]):
        metrics (Union[Unset, List['WorkflowMetrics']]):
        progress (Union[Unset, TraceProgressData]):
    """

    workflow: Union[Unset, "Workflow"] = UNSET
    metrics: Union[Unset, List["WorkflowMetrics"]] = UNSET
    progress: Union[Unset, "TraceProgressData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        workflow: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        metrics: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = []
            for metrics_item_data in self.metrics:
                metrics_item = metrics_item_data.to_dict()

                metrics.append(metrics_item)

        progress: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.progress, Unset):
            progress = self.progress.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if progress is not UNSET:
            field_dict["progress"] = progress

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.trace_progress_data import TraceProgressData
        from ..models.workflow import Workflow
        from ..models.workflow_metrics import WorkflowMetrics

        d = src_dict.copy()
        _workflow = d.pop("workflow", UNSET)
        workflow: Union[Unset, Workflow]
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = Workflow.from_dict(_workflow)

        metrics = []
        _metrics = d.pop("metrics", UNSET)
        for metrics_item_data in _metrics or []:
            metrics_item = WorkflowMetrics.from_dict(metrics_item_data)

            metrics.append(metrics_item)

        _progress = d.pop("progress", UNSET)
        progress: Union[Unset, TraceProgressData]
        if isinstance(_progress, Unset):
            progress = UNSET
        else:
            progress = TraceProgressData.from_dict(_progress)

        trace_complete_request = cls(
            workflow=workflow,
            metrics=metrics,
            progress=progress,
        )

        trace_complete_request.additional_properties = d
        return trace_complete_request

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
