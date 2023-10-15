from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_version_db_dto import DatasetVersionDbDto


T = TypeVar("T", bound="ListDatasetVersionsResponse")


@_attrs_define
class ListDatasetVersionsResponse:
    """
    Attributes:
        versions (Union[Unset, List['DatasetVersionDbDto']]):
    """

    versions: Union[Unset, List["DatasetVersionDbDto"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        versions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.versions, Unset):
            versions = []
            for versions_item_data in self.versions:
                versions_item = versions_item_data.to_dict()

                versions.append(versions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if versions is not UNSET:
            field_dict["versions"] = versions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dataset_version_db_dto import DatasetVersionDbDto

        d = src_dict.copy()
        versions = []
        _versions = d.pop("versions", UNSET)
        for versions_item_data in _versions or []:
            versions_item = DatasetVersionDbDto.from_dict(versions_item_data)

            versions.append(versions_item)

        list_dataset_versions_response = cls(
            versions=versions,
        )

        list_dataset_versions_response.additional_properties = d
        return list_dataset_versions_response

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
