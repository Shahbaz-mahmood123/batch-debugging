from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compute_env_response_dto import ComputeEnvResponseDto


T = TypeVar("T", bound="DescribeComputeEnvResponse")


@_attrs_define
class DescribeComputeEnvResponse:
    """
    Attributes:
        compute_env (Union[Unset, ComputeEnvResponseDto]):
    """

    compute_env: Union[Unset, "ComputeEnvResponseDto"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compute_env: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.compute_env, Unset):
            compute_env = self.compute_env.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compute_env is not UNSET:
            field_dict["computeEnv"] = compute_env

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.compute_env_response_dto import ComputeEnvResponseDto

        d = src_dict.copy()
        _compute_env = d.pop("computeEnv", UNSET)
        compute_env: Union[Unset, ComputeEnvResponseDto]
        if isinstance(_compute_env, Unset):
            compute_env = UNSET
        else:
            compute_env = ComputeEnvResponseDto.from_dict(_compute_env)

        describe_compute_env_response = cls(
            compute_env=compute_env,
        )

        describe_compute_env_response.additional_properties = d
        return describe_compute_env_response

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
