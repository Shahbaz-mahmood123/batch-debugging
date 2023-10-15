from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_load import ProcessLoad
    from ..models.workflow_load import WorkflowLoad


T = TypeVar("T", bound="ProgressData")


@_attrs_define
class ProgressData:
    """
    Attributes:
        workflow_progress (Union[Unset, WorkflowLoad]):
        processes_progress (Union[Unset, List['ProcessLoad']]):
    """

    workflow_progress: Union[Unset, "WorkflowLoad"] = UNSET
    processes_progress: Union[Unset, List["ProcessLoad"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        workflow_progress: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workflow_progress, Unset):
            workflow_progress = self.workflow_progress.to_dict()

        processes_progress: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.processes_progress, Unset):
            processes_progress = []
            for processes_progress_item_data in self.processes_progress:
                processes_progress_item = processes_progress_item_data.to_dict()

                processes_progress.append(processes_progress_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workflow_progress is not UNSET:
            field_dict["workflowProgress"] = workflow_progress
        if processes_progress is not UNSET:
            field_dict["processesProgress"] = processes_progress

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.process_load import ProcessLoad
        from ..models.workflow_load import WorkflowLoad

        d = src_dict.copy()
        _workflow_progress = d.pop("workflowProgress", UNSET)
        workflow_progress: Union[Unset, WorkflowLoad]
        if isinstance(_workflow_progress, Unset):
            workflow_progress = UNSET
        else:
            workflow_progress = WorkflowLoad.from_dict(_workflow_progress)

        processes_progress = []
        _processes_progress = d.pop("processesProgress", UNSET)
        for processes_progress_item_data in _processes_progress or []:
            processes_progress_item = ProcessLoad.from_dict(processes_progress_item_data)

            processes_progress.append(processes_progress_item)

        progress_data = cls(
            workflow_progress=workflow_progress,
            processes_progress=processes_progress,
        )

        progress_data.additional_properties = d
        return progress_data

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
