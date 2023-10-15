from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateComputeEnvResponse")


@_attrs_define
class CreateComputeEnvResponse:
    """
    Attributes:
        compute_env_id (Union[Unset, str]):
    """

    compute_env_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compute_env_id = self.compute_env_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compute_env_id is not UNSET:
            field_dict["computeEnvId"] = compute_env_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        compute_env_id = d.pop("computeEnvId", UNSET)

        create_compute_env_response = cls(
            compute_env_id=compute_env_id,
        )

        create_compute_env_response.additional_properties = d
        return create_compute_env_response

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
