from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pipeline_secret import PipelineSecret


T = TypeVar("T", bound="DescribePipelineSecretResponse")


@_attrs_define
class DescribePipelineSecretResponse:
    """
    Attributes:
        pipeline_secret (Union[Unset, PipelineSecret]):
    """

    pipeline_secret: Union[Unset, "PipelineSecret"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pipeline_secret: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pipeline_secret, Unset):
            pipeline_secret = self.pipeline_secret.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pipeline_secret is not UNSET:
            field_dict["pipelineSecret"] = pipeline_secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pipeline_secret import PipelineSecret

        d = src_dict.copy()
        _pipeline_secret = d.pop("pipelineSecret", UNSET)
        pipeline_secret: Union[Unset, PipelineSecret]
        if isinstance(_pipeline_secret, Unset):
            pipeline_secret = UNSET
        else:
            pipeline_secret = PipelineSecret.from_dict(_pipeline_secret)

        describe_pipeline_secret_response = cls(
            pipeline_secret=pipeline_secret,
        )

        describe_pipeline_secret_response.additional_properties = d
        return describe_pipeline_secret_response

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
