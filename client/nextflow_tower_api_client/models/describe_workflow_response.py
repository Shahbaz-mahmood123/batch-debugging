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
        workflow (Workflow):
        progress (Union[Unset, ProgressData]):
        optimized (Union[Unset, bool]):
        platform (Union[Unset, ComputePlatformDto]):
        org_name (Union[Unset, str]):
        workspace_name (Union[Unset, str]):
        labels (Union[Unset, List['LabelDbDto']]):
        job_info (Union[Unset, JobInfoDto]):
        org_id (Union[Unset, int]):
        workspace_id (Union[Unset, int]):
    """

    workflow: "Workflow"
    progress: Union[Unset, "ProgressData"] = UNSET
    optimized: Union[Unset, bool] = UNSET
    platform: Union[Unset, "ComputePlatformDto"] = UNSET
    org_name: Union[Unset, str] = UNSET
    workspace_name: Union[Unset, str] = UNSET
    labels: Union[Unset, List["LabelDbDto"]] = UNSET
    job_info: Union[Unset, "JobInfoDto"] = UNSET
    org_id: Union[Unset, int] = UNSET
    workspace_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        workflow = self.workflow.to_dict()

        progress: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.progress, Unset):
            progress = self.progress.to_dict()

        optimized = self.optimized
        platform: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.to_dict()

        org_name = self.org_name
        workspace_name = self.workspace_name
        labels: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()

                labels.append(labels_item)

        job_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.job_info, Unset):
            job_info = self.job_info.to_dict()

        org_id = self.org_id
        workspace_id = self.workspace_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workflow": workflow,
            }
        )
        if progress is not UNSET:
            field_dict["progress"] = progress
        if optimized is not UNSET:
            field_dict["optimized"] = optimized
        if platform is not UNSET:
            field_dict["platform"] = platform
        if org_name is not UNSET:
            field_dict["orgName"] = org_name
        if workspace_name is not UNSET:
            field_dict["workspaceName"] = workspace_name
        if labels is not UNSET:
            field_dict["labels"] = labels
        if job_info is not UNSET:
            field_dict["jobInfo"] = job_info
        if org_id is not UNSET:
            field_dict["orgId"] = org_id
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.compute_platform_dto import ComputePlatformDto
        from ..models.job_info_dto import JobInfoDto
        from ..models.label_db_dto import LabelDbDto
        from ..models.progress_data import ProgressData
        from ..models.workflow import Workflow

        d = src_dict.copy()
        workflow = Workflow.from_dict(d.pop("workflow"))

        _progress = d.pop("progress", UNSET)
        progress: Union[Unset, ProgressData]
        if isinstance(_progress, Unset):
            progress = UNSET
        else:
            progress = ProgressData.from_dict(_progress)

        optimized = d.pop("optimized", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: Union[Unset, ComputePlatformDto]
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = ComputePlatformDto.from_dict(_platform)

        org_name = d.pop("orgName", UNSET)

        workspace_name = d.pop("workspaceName", UNSET)

        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in _labels or []:
            labels_item = LabelDbDto.from_dict(labels_item_data)

            labels.append(labels_item)

        _job_info = d.pop("jobInfo", UNSET)
        job_info: Union[Unset, JobInfoDto]
        if isinstance(_job_info, Unset):
            job_info = UNSET
        else:
            job_info = JobInfoDto.from_dict(_job_info)

        org_id = d.pop("orgId", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        describe_workflow_response = cls(
            workflow=workflow,
            progress=progress,
            optimized=optimized,
            platform=platform,
            org_name=org_name,
            workspace_name=workspace_name,
            labels=labels,
            job_info=job_info,
            org_id=org_id,
            workspace_id=workspace_id,
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
