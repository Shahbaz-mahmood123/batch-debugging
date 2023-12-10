from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compute_platform_dto import ComputePlatformDto
    from ..models.job_info_dto import JobInfoDto
    from ..models.label_db_dto import LabelDbDto
    from ..models.progress_data import ProgressData
    from ..models.workflow import Workflow


T = TypeVar("T", bound="DescribeWorkflowResponse")


@_attrs_define
class DescribeWorkflowResponse:
    """
    Attributes:
        progress (Union[Unset, ProgressData]):
        optimized (Union[Unset, bool]):
        org_id (Union[Unset, int]):
        platform (Union[Unset, ComputePlatformDto]):
        job_info (Union[Unset, JobInfoDto]):
        labels (Union[Unset, List['LabelDbDto']]):
        org_name (Union[Unset, str]):
        workspace_name (Union[Unset, str]):
        workspace_id (Union[Unset, int]):
        workflow (Union[Unset, Workflow]):
    """

    progress: Union[Unset, "ProgressData"] = UNSET
    optimized: Union[Unset, bool] = UNSET
    org_id: Union[Unset, int] = UNSET
    platform: Union[Unset, "ComputePlatformDto"] = UNSET
    job_info: Union[Unset, "JobInfoDto"] = UNSET
    labels: Union[Unset, List["LabelDbDto"]] = UNSET
    org_name: Union[Unset, str] = UNSET
    workspace_name: Union[Unset, str] = UNSET
    workspace_id: Union[Unset, int] = UNSET
    workflow: Union[Unset, "Workflow"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        progress: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.progress, Unset):
            progress = self.progress.to_dict()

        optimized = self.optimized
        org_id = self.org_id
        platform: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.to_dict()

        job_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.job_info, Unset):
            job_info = self.job_info.to_dict()

        labels: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()

                labels.append(labels_item)

        org_name = self.org_name
        workspace_name = self.workspace_name
        workspace_id = self.workspace_id
        workflow: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if progress is not UNSET:
            field_dict["progress"] = progress
        if optimized is not UNSET:
            field_dict["optimized"] = optimized
        if org_id is not UNSET:
            field_dict["orgId"] = org_id
        if platform is not UNSET:
            field_dict["platform"] = platform
        if job_info is not UNSET:
            field_dict["jobInfo"] = job_info
        if labels is not UNSET:
            field_dict["labels"] = labels
        if org_name is not UNSET:
            field_dict["orgName"] = org_name
        if workspace_name is not UNSET:
            field_dict["workspaceName"] = workspace_name
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if workflow is not UNSET:
            field_dict["workflow"] = workflow

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.compute_platform_dto import ComputePlatformDto
        from ..models.job_info_dto import JobInfoDto
        from ..models.label_db_dto import LabelDbDto
        from ..models.progress_data import ProgressData
        from ..models.workflow import Workflow

        d = src_dict.copy()
        _progress = d.pop("progress", UNSET)
        progress: Union[Unset, ProgressData]
        if isinstance(_progress, Unset):
            progress = UNSET
        else:
            progress = ProgressData.from_dict(_progress)

        optimized = d.pop("optimized", UNSET)

        org_id = d.pop("orgId", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: Union[Unset, ComputePlatformDto]
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = ComputePlatformDto.from_dict(_platform)

        _job_info = d.pop("jobInfo", UNSET)
        job_info: Union[Unset, JobInfoDto]
        if isinstance(_job_info, Unset):
            job_info = UNSET
        else:
            job_info = JobInfoDto.from_dict(_job_info)

        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in _labels or []:
            labels_item = LabelDbDto.from_dict(labels_item_data)

            labels.append(labels_item)

        org_name = d.pop("orgName", UNSET)

        workspace_name = d.pop("workspaceName", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        _workflow = d.pop("workflow", UNSET)
        workflow: Union[Unset, Workflow]
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = Workflow.from_dict(_workflow)

        describe_workflow_response = cls(
            progress=progress,
            optimized=optimized,
            org_id=org_id,
            platform=platform,
            job_info=job_info,
            labels=labels,
            org_name=org_name,
            workspace_name=workspace_name,
            workspace_id=workspace_id,
            workflow=workflow,
        )

        describe_workflow_response.additional_properties = d
        return describe_workflow_response

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
