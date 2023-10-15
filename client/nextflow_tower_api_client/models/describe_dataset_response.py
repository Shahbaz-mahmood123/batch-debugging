from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset import Dataset


T = TypeVar("T", bound="DescribeDatasetResponse")


@_attrs_define
class DescribeDatasetResponse:
    """
    Attributes:
        dataset (Union[Unset, Dataset]):
    """

    dataset: Union[Unset, "Dataset"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dataset: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dataset, Unset):
            dataset = self.dataset.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dataset is not UNSET:
            field_dict["dataset"] = dataset

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dataset import Dataset

        d = src_dict.copy()
        _dataset = d.pop("dataset", UNSET)
        dataset: Union[Unset, Dataset]
        if isinstance(_dataset, Unset):
            dataset = UNSET
        else:
            dataset = Dataset.from_dict(_dataset)

        describe_dataset_response = cls(
            dataset=dataset,
        )

        describe_dataset_response.additional_properties = d
        return describe_dataset_response

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
