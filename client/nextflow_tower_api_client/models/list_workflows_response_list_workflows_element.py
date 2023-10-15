from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.label_db_dto import LabelDbDto
    from ..models.progress_data import ProgressData
    from ..models.workflow_db_dto import WorkflowDbDto


T = TypeVar("T", bound="ListWorkflowsResponseListWorkflowsElement")


@_attrs_define
class ListWorkflowsResponseListWorkflowsElement:
    """
    Attributes:
        progress (Union[Unset, ProgressData]):
        starred (Union[Unset, bool]):
        optimized (Union[Unset, bool]):
        org_name (Union[Unset, str]):
        workspace_name (Union[Unset, str]):
        labels (Union[Unset, List['LabelDbDto']]):
        workflow (Union[Unset, WorkflowDbDto]):
        org_id (Union[Unset, int]):
        workspace_id (Union[Unset, int]):
    """

    progress: Union[Unset, "ProgressData"] = UNSET
    starred: Union[Unset, bool] = UNSET
    optimized: Union[Unset, bool] = UNSET
    org_name: Union[Unset, str] = UNSET
    workspace_name: Union[Unset, str] = UNSET
    labels: Union[Unset, List["LabelDbDto"]] = UNSET
    workflow: Union[Unset, "WorkflowDbDto"] = UNSET
    org_id: Union[Unset, int] = UNSET
    workspace_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        progress: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.progress, Unset):
            progress = self.progress.to_dict()

        starred = self.starred
        optimized = self.optimized
        org_name = self.org_name
        workspace_name = self.workspace_name
        labels: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()

                labels.append(labels_item)

        workflow: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        org_id = self.org_id
        workspace_id = self.workspace_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if progress is not UNSET:
            field_dict["progress"] = progress
        if starred is not UNSET:
            field_dict["starred"] = starred
        if optimized is not UNSET:
            field_dict["optimized"] = optimized
        if org_name is not UNSET:
            field_dict["orgName"] = org_name
        if workspace_name is not UNSET:
            field_dict["workspaceName"] = workspace_name
        if labels is not UNSET:
            field_dict["labels"] = labels
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if org_id is not UNSET:
            field_dict["orgId"] = org_id
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.label_db_dto import LabelDbDto
        from ..models.progress_data import ProgressData
        from ..models.workflow_db_dto import WorkflowDbDto

        d = src_dict.copy()
        _progress = d.pop("progress", UNSET)
        progress: Union[Unset, ProgressData]
        if isinstance(_progress, Unset):
            progress = UNSET
        else:
            progress = ProgressData.from_dict(_progress)

        starred = d.pop("starred", UNSET)

        optimized = d.pop("optimized", UNSET)

        org_name = d.pop("orgName", UNSET)

        workspace_name = d.pop("workspaceName", UNSET)

        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in _labels or []:
            labels_item = LabelDbDto.from_dict(labels_item_data)

            labels.append(labels_item)

        _workflow = d.pop("workflow", UNSET)
        workflow: Union[Unset, WorkflowDbDto]
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = WorkflowDbDto.from_dict(_workflow)

        org_id = d.pop("orgId", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        list_workflows_response_list_workflows_element = cls(
            progress=progress,
            starred=starred,
            optimized=optimized,
            org_name=org_name,
            workspace_name=workspace_name,
            labels=labels,
            workflow=workflow,
            org_id=org_id,
            workspace_id=workspace_id,
        )

        list_workflows_response_list_workflows_element.additional_properties = d
        return list_workflows_response_list_workflows_element

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
