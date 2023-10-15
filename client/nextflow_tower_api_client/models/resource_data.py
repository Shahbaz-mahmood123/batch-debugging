from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceData")


@_attrs_define
class ResourceData:
    """
    Attributes:
        warnings (Union[Unset, List[str]]):
        mean (Union[Unset, float]):
        min_ (Union[Unset, float]):
        q1 (Union[Unset, float]):
        q2 (Union[Unset, float]):
        q3 (Union[Unset, float]):
        max_ (Union[Unset, float]):
        min_label (Union[Unset, str]):
        max_label (Union[Unset, str]):
        q_1_label (Union[Unset, str]):
        q_2_label (Union[Unset, str]):
        q_3_label (Union[Unset, str]):
    """

    warnings: Union[Unset, List[str]] = UNSET
    mean: Union[Unset, float] = UNSET
    min_: Union[Unset, float] = UNSET
    q1: Union[Unset, float] = UNSET
    q2: Union[Unset, float] = UNSET
    q3: Union[Unset, float] = UNSET
    max_: Union[Unset, float] = UNSET
    min_label: Union[Unset, str] = UNSET
    max_label: Union[Unset, str] = UNSET
    q_1_label: Union[Unset, str] = UNSET
    q_2_label: Union[Unset, str] = UNSET
    q_3_label: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        warnings: Union[Unset, List[str]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        mean = self.mean
        min_ = self.min_
        q1 = self.q1
        q2 = self.q2
        q3 = self.q3
        max_ = self.max_
        min_label = self.min_label
        max_label = self.max_label
        q_1_label = self.q_1_label
        q_2_label = self.q_2_label
        q_3_label = self.q_3_label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if mean is not UNSET:
            field_dict["mean"] = mean
        if min_ is not UNSET:
            field_dict["min"] = min_
        if q1 is not UNSET:
            field_dict["q1"] = q1
        if q2 is not UNSET:
            field_dict["q2"] = q2
        if q3 is not UNSET:
            field_dict["q3"] = q3
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_label is not UNSET:
            field_dict["minLabel"] = min_label
        if max_label is not UNSET:
            field_dict["maxLabel"] = max_label
        if q_1_label is not UNSET:
            field_dict["q1Label"] = q_1_label
        if q_2_label is not UNSET:
            field_dict["q2Label"] = q_2_label
        if q_3_label is not UNSET:
            field_dict["q3Label"] = q_3_label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        warnings = cast(List[str], d.pop("warnings", UNSET))

        mean = d.pop("mean", UNSET)

        min_ = d.pop("min", UNSET)

        q1 = d.pop("q1", UNSET)

        q2 = d.pop("q2", UNSET)

        q3 = d.pop("q3", UNSET)

        max_ = d.pop("max", UNSET)

        min_label = d.pop("minLabel", UNSET)

        max_label = d.pop("maxLabel", UNSET)

        q_1_label = d.pop("q1Label", UNSET)

        q_2_label = d.pop("q2Label", UNSET)

        q_3_label = d.pop("q3Label", UNSET)

        resource_data = cls(
            warnings=warnings,
            mean=mean,
            min_=min_,
            q1=q1,
            q2=q2,
            q3=q3,
            max_=max_,
            min_label=min_label,
            max_label=max_label,
            q_1_label=q_1_label,
            q_2_label=q_2_label,
            q_3_label=q_3_label,
        )

        resource_data.additional_properties = d
        return resource_data

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
