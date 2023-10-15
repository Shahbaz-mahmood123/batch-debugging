from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pipeline_info import PipelineInfo


T = TypeVar("T", bound="DescribePipelineInfoResponse")


@_attrs_define
class DescribePipelineInfoResponse:
    """
    Attributes:
        pipeline_info (Union[Unset, PipelineInfo]):
    """

    pipeline_info: Union[Unset, "PipelineInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pipeline_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pipeline_info, Unset):
            pipeline_info = self.pipeline_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pipeline_info is not UNSET:
            field_dict["pipelineInfo"] = pipeline_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pipeline_info import PipelineInfo

        d = src_dict.copy()
        _pipeline_info = d.pop("pipelineInfo", UNSET)
        pipeline_info: Union[Unset, PipelineInfo]
        if isinstance(_pipeline_info, Unset):
            pipeline_info = UNSET
        else:
            pipeline_info = PipelineInfo.from_dict(_pipeline_info)

        describe_pipeline_info_response = cls(
            pipeline_info=pipeline_info,
        )

        describe_pipeline_info_response.additional_properties = d
        return describe_pipeline_info_response

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
