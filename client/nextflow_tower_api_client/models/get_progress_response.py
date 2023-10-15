from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.progress_data import ProgressData


T = TypeVar("T", bound="GetProgressResponse")


@_attrs_define
class GetProgressResponse:
    """
    Attributes:
        progress (Union[Unset, ProgressData]):
    """

    progress: Union[Unset, "ProgressData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        progress: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.progress, Unset):
            progress = self.progress.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if progress is not UNSET:
            field_dict["progress"] = progress

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.progress_data import ProgressData

        d = src_dict.copy()
        _progress = d.pop("progress", UNSET)
        progress: Union[Unset, ProgressData]
        if isinstance(_progress, Unset):
            progress = UNSET
        else:
            progress = ProgressData.from_dict(_progress)

        get_progress_response = cls(
            progress=progress,
        )

        get_progress_response.additional_properties = d
        return get_progress_response

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
