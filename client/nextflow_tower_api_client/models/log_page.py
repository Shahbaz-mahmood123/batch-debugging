from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iterator_string import IteratorString
    from ..models.log_page_download import LogPageDownload


T = TypeVar("T", bound="LogPage")


@_attrs_define
class LogPage:
    """
    Attributes:
        entries (Union[Unset, IteratorString]):
        rewind_token (Union[Unset, str]):
        forward_token (Union[Unset, str]):
        pending (Union[Unset, bool]):
        message (Union[Unset, str]):
        downloads (Union[Unset, List['LogPageDownload']]):
        truncated (Union[Unset, bool]):
    """

    entries: Union[Unset, "IteratorString"] = UNSET
    rewind_token: Union[Unset, str] = UNSET
    forward_token: Union[Unset, str] = UNSET
    pending: Union[Unset, bool] = UNSET
    message: Union[Unset, str] = UNSET
    downloads: Union[Unset, List["LogPageDownload"]] = UNSET
    truncated: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entries: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entries, Unset):
            entries = self.entries.to_dict()

        rewind_token = self.rewind_token
        forward_token = self.forward_token
        pending = self.pending
        message = self.message
        downloads: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.downloads, Unset):
            downloads = []
            for downloads_item_data in self.downloads:
                downloads_item = downloads_item_data.to_dict()

                downloads.append(downloads_item)

        truncated = self.truncated

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entries is not UNSET:
            field_dict["entries"] = entries
        if rewind_token is not UNSET:
            field_dict["rewindToken"] = rewind_token
        if forward_token is not UNSET:
            field_dict["forwardToken"] = forward_token
        if pending is not UNSET:
            field_dict["pending"] = pending
        if message is not UNSET:
            field_dict["message"] = message
        if downloads is not UNSET:
            field_dict["downloads"] = downloads
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.iterator_string import IteratorString
        from ..models.log_page_download import LogPageDownload

        d = src_dict.copy()
        _entries = d.pop("entries", UNSET)
        entries: Union[Unset, IteratorString]
        if isinstance(_entries, Unset):
            entries = UNSET
        else:
            entries = IteratorString.from_dict(_entries)

        rewind_token = d.pop("rewindToken", UNSET)

        forward_token = d.pop("forwardToken", UNSET)

        pending = d.pop("pending", UNSET)

        message = d.pop("message", UNSET)

        downloads = []
        _downloads = d.pop("downloads", UNSET)
        for downloads_item_data in _downloads or []:
            downloads_item = LogPageDownload.from_dict(downloads_item_data)

            downloads.append(downloads_item)

        truncated = d.pop("truncated", UNSET)

        log_page = cls(
            entries=entries,
            rewind_token=rewind_token,
            forward_token=forward_token,
            pending=pending,
            message=message,
            downloads=downloads,
            truncated=truncated,
        )

        log_page.additional_properties = d
        return log_page

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
