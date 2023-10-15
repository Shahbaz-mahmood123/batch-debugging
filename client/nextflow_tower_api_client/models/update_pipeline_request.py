from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_launch_request import WorkflowLaunchRequest


T = TypeVar("T", bound="UpdatePipelineRequest")


@_attrs_define
class UpdatePipelineRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        icon (Union[Unset, str]):
        launch (Union[Unset, WorkflowLaunchRequest]):
        label_ids (Union[Unset, List[int]]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    icon: Union[Unset, str] = UNSET
    launch: Union[Unset, "WorkflowLaunchRequest"] = UNSET
    label_ids: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        icon = self.icon
        launch: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.launch, Unset):
            launch = self.launch.to_dict()

        label_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.label_ids, Unset):
            label_ids = self.label_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if icon is not UNSET:
            field_dict["icon"] = icon
        if launch is not UNSET:
            field_dict["launch"] = launch
        if label_ids is not UNSET:
            field_dict["labelIds"] = label_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.workflow_launch_request import WorkflowLaunchRequest

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        icon = d.pop("icon", UNSET)

        _launch = d.pop("launch", UNSET)
        launch: Union[Unset, WorkflowLaunchRequest]
        if isinstance(_launch, Unset):
            launch = UNSET
        else:
            launch = WorkflowLaunchRequest.from_dict(_launch)

        label_ids = cast(List[int], d.pop("labelIds", UNSET))

        update_pipeline_request = cls(
            name=name,
            description=description,
            icon=icon,
            launch=launch,
            label_ids=label_ids,
        )

        update_pipeline_request.additional_properties = d
        return update_pipeline_request

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
