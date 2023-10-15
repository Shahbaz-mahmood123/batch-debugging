from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_launch_request import WorkflowLaunchRequest


T = TypeVar("T", bound="SubmitWorkflowLaunchRequest")


@_attrs_define
class SubmitWorkflowLaunchRequest:
    """
    Attributes:
        launch (Union[Unset, WorkflowLaunchRequest]):
    """

    launch: Union[Unset, "WorkflowLaunchRequest"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        launch: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.launch, Unset):
            launch = self.launch.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if launch is not UNSET:
            field_dict["launch"] = launch

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.workflow_launch_request import WorkflowLaunchRequest

        d = src_dict.copy()
        _launch = d.pop("launch", UNSET)
        launch: Union[Unset, WorkflowLaunchRequest]
        if isinstance(_launch, Unset):
            launch = UNSET
        else:
            launch = WorkflowLaunchRequest.from_dict(_launch)

        submit_workflow_launch_request = cls(
            launch=launch,
        )

        submit_workflow_launch_request.additional_properties = d
        return submit_workflow_launch_request

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
