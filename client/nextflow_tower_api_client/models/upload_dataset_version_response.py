from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_version_db_dto import DatasetVersionDbDto


T = TypeVar("T", bound="UploadDatasetVersionResponse")


@_attrs_define
class UploadDatasetVersionResponse:
    """
    Attributes:
        version (Union[Unset, DatasetVersionDbDto]):
    """

    version: Union[Unset, "DatasetVersionDbDto"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dataset_version_db_dto import DatasetVersionDbDto

        d = src_dict.copy()
        _version = d.pop("version", UNSET)
        version: Union[Unset, DatasetVersionDbDto]
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = DatasetVersionDbDto.from_dict(_version)

        upload_dataset_version_response = cls(
            version=version,
        )

        upload_dataset_version_response.additional_properties = d
        return upload_dataset_version_response

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
