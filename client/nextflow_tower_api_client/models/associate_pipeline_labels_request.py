from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssociatePipelineLabelsRequest")


@_attrs_define
class AssociatePipelineLabelsRequest:
    """
    Attributes:
        pipeline_ids (Union[Unset, List[int]]):
        label_ids (Union[Unset, List[int]]):
    """

    pipeline_ids: Union[Unset, List[int]] = UNSET
    label_ids: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pipeline_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.pipeline_ids, Unset):
            pipeline_ids = self.pipeline_ids

        label_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.label_ids, Unset):
            label_ids = self.label_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pipeline_ids is not UNSET:
            field_dict["pipelineIds"] = pipeline_ids
        if label_ids is not UNSET:
            field_dict["labelIds"] = label_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pipeline_ids = cast(List[int], d.pop("pipelineIds", UNSET))

        label_ids = cast(List[int], d.pop("labelIds", UNSET))

        associate_pipeline_labels_request = cls(
            pipeline_ids=pipeline_ids,
            label_ids=label_ids,
        )

        associate_pipeline_labels_request.additional_properties = d
        return associate_pipeline_labels_request

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
