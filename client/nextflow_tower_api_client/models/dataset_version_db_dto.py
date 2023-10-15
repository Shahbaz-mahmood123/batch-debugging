import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatasetVersionDbDto")


@_attrs_define
class DatasetVersionDbDto:
    """
    Attributes:
        dataset_id (Union[Unset, str]):
        dataset_name (Union[Unset, str]):
        dataset_description (Union[Unset, str]):
        has_header (Union[Unset, bool]):
        version (Union[Unset, int]):
        last_updated (Union[Unset, datetime.datetime]):
        file_name (Union[Unset, str]):
        media_type (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    dataset_id: Union[Unset, str] = UNSET
    dataset_name: Union[Unset, str] = UNSET
    dataset_description: Union[Unset, str] = UNSET
    has_header: Union[Unset, bool] = UNSET
    version: Union[Unset, int] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    file_name: Union[Unset, str] = UNSET
    media_type: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dataset_id = self.dataset_id
        dataset_name = self.dataset_name
        dataset_description = self.dataset_description
        has_header = self.has_header
        version = self.version
        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        file_name = self.file_name
        media_type = self.media_type
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dataset_id is not UNSET:
            field_dict["datasetId"] = dataset_id
        if dataset_name is not UNSET:
            field_dict["datasetName"] = dataset_name
        if dataset_description is not UNSET:
            field_dict["datasetDescription"] = dataset_description
        if has_header is not UNSET:
            field_dict["hasHeader"] = has_header
        if version is not UNSET:
            field_dict["version"] = version
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if media_type is not UNSET:
            field_dict["mediaType"] = media_type
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dataset_id = d.pop("datasetId", UNSET)

        dataset_name = d.pop("datasetName", UNSET)

        dataset_description = d.pop("datasetDescription", UNSET)

        has_header = d.pop("hasHeader", UNSET)

        version = d.pop("version", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        file_name = d.pop("fileName", UNSET)

        media_type = d.pop("mediaType", UNSET)

        url = d.pop("url", UNSET)

        dataset_version_db_dto = cls(
            dataset_id=dataset_id,
            dataset_name=dataset_name,
            dataset_description=dataset_description,
            has_header=has_header,
            version=version,
            last_updated=last_updated,
            file_name=file_name,
            media_type=media_type,
            url=url,
        )

        dataset_version_db_dto.additional_properties = d
        return dataset_version_db_dto

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
