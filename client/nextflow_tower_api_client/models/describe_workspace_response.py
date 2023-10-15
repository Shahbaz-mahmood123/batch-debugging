from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workspace import Workspace


T = TypeVar("T", bound="DescribeWorkspaceResponse")


@_attrs_define
class DescribeWorkspaceResponse:
    """
    Attributes:
        workspace (Union[Unset, Workspace]):
    """

    workspace: Union[Unset, "Workspace"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        workspace: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workspace, Unset):
            workspace = self.workspace.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workspace is not UNSET:
            field_dict["workspace"] = workspace

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.workspace import Workspace

        d = src_dict.copy()
        _workspace = d.pop("workspace", UNSET)
        workspace: Union[Unset, Workspace]
        if isinstance(_workspace, Unset):
            workspace = UNSET
        else:
            workspace = Workspace.from_dict(_workspace)

        describe_workspace_response = cls(
            workspace=workspace,
        )

        describe_workspace_response.additional_properties = d
        return describe_workspace_response

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
