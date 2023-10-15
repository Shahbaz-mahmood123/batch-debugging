from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_source import ActionSource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_launch_request import WorkflowLaunchRequest


T = TypeVar("T", bound="CreateActionRequest")


@_attrs_define
class CreateActionRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        source (Union[Unset, ActionSource]):
        launch (Union[Unset, WorkflowLaunchRequest]):
    """

    name: Union[Unset, str] = UNSET
    source: Union[Unset, ActionSource] = UNSET
    launch: Union[Unset, "WorkflowLaunchRequest"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        launch: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.launch, Unset):
            launch = self.launch.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if source is not UNSET:
            field_dict["source"] = source
        if launch is not UNSET:
            field_dict["launch"] = launch

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.workflow_launch_request import WorkflowLaunchRequest

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, ActionSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ActionSource(_source)

        _launch = d.pop("launch", UNSET)
        launch: Union[Unset, WorkflowLaunchRequest]
        if isinstance(_launch, Unset):
            launch = UNSET
        else:
            launch = WorkflowLaunchRequest.from_dict(_launch)

        create_action_request = cls(
            name=name,
            source=source,
            launch=launch,
        )

        create_action_request.additional_properties = d
        return create_action_request

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
