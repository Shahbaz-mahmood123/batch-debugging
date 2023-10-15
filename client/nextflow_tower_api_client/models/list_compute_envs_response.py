from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_compute_envs_response_entry import ListComputeEnvsResponseEntry


T = TypeVar("T", bound="ListComputeEnvsResponse")


@_attrs_define
class ListComputeEnvsResponse:
    """
    Attributes:
        compute_envs (Union[Unset, List['ListComputeEnvsResponseEntry']]):
    """

    compute_envs: Union[Unset, List["ListComputeEnvsResponseEntry"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compute_envs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.compute_envs, Unset):
            compute_envs = []
            for compute_envs_item_data in self.compute_envs:
                compute_envs_item = compute_envs_item_data.to_dict()

                compute_envs.append(compute_envs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compute_envs is not UNSET:
            field_dict["computeEnvs"] = compute_envs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_compute_envs_response_entry import ListComputeEnvsResponseEntry

        d = src_dict.copy()
        compute_envs = []
        _compute_envs = d.pop("computeEnvs", UNSET)
        for compute_envs_item_data in _compute_envs or []:
            compute_envs_item = ListComputeEnvsResponseEntry.from_dict(compute_envs_item_data)

            compute_envs.append(compute_envs_item)

        list_compute_envs_response = cls(
            compute_envs=compute_envs,
        )

        list_compute_envs_response.additional_properties = d
        return list_compute_envs_response

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
