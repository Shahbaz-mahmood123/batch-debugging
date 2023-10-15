from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteWorkflowsRequest")


@_attrs_define
class DeleteWorkflowsRequest:
    """
    Attributes:
        workflow_ids (Union[Unset, List[str]]):
    """

    workflow_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        workflow_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.workflow_ids, Unset):
            workflow_ids = self.workflow_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workflow_ids is not UNSET:
            field_dict["workflowIds"] = workflow_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        workflow_ids = cast(List[str], d.pop("workflowIds", UNSET))

        delete_workflows_request = cls(
            workflow_ids=workflow_ids,
        )

        delete_workflows_request.additional_properties = d
        return delete_workflows_request

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
