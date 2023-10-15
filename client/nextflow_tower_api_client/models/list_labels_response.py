from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.label_db_dto import LabelDbDto


T = TypeVar("T", bound="ListLabelsResponse")


@_attrs_define
class ListLabelsResponse:
    """
    Attributes:
        labels (Union[Unset, List['LabelDbDto']]):
        total_size (Union[Unset, int]):
    """

    labels: Union[Unset, List["LabelDbDto"]] = UNSET
    total_size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        labels: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()

                labels.append(labels_item)

        total_size = self.total_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if labels is not UNSET:
            field_dict["labels"] = labels
        if total_size is not UNSET:
            field_dict["totalSize"] = total_size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.label_db_dto import LabelDbDto

        d = src_dict.copy()
        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in _labels or []:
            labels_item = LabelDbDto.from_dict(labels_item_data)

            labels.append(labels_item)

        total_size = d.pop("totalSize", UNSET)

        list_labels_response = cls(
            labels=labels,
            total_size=total_size,
        )

        list_labels_response.additional_properties = d
        return list_labels_response

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
