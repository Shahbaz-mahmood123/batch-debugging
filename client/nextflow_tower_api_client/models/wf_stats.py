from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfStats")


@_attrs_define
class WfStats:
    """
    Attributes:
        compute_time_fmt (Union[Unset, str]):
        cached_count (Union[Unset, int]):
        failed_count (Union[Unset, int]):
        ignored_count (Union[Unset, int]):
        succeed_count (Union[Unset, int]):
        cached_count_fmt (Union[Unset, str]):
        succeed_count_fmt (Union[Unset, str]):
        failed_count_fmt (Union[Unset, str]):
        ignored_count_fmt (Union[Unset, str]):
        cached_pct (Union[Unset, float]):
        failed_pct (Union[Unset, float]):
        succeed_pct (Union[Unset, float]):
        ignored_pct (Union[Unset, float]):
        cached_duration (Union[Unset, int]):
        failed_duration (Union[Unset, int]):
        succeed_duration (Union[Unset, int]):
    """

    compute_time_fmt: Union[Unset, str] = UNSET
    cached_count: Union[Unset, int] = UNSET
    failed_count: Union[Unset, int] = UNSET
    ignored_count: Union[Unset, int] = UNSET
    succeed_count: Union[Unset, int] = UNSET
    cached_count_fmt: Union[Unset, str] = UNSET
    succeed_count_fmt: Union[Unset, str] = UNSET
    failed_count_fmt: Union[Unset, str] = UNSET
    ignored_count_fmt: Union[Unset, str] = UNSET
    cached_pct: Union[Unset, float] = UNSET
    failed_pct: Union[Unset, float] = UNSET
    succeed_pct: Union[Unset, float] = UNSET
    ignored_pct: Union[Unset, float] = UNSET
    cached_duration: Union[Unset, int] = UNSET
    failed_duration: Union[Unset, int] = UNSET
    succeed_duration: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compute_time_fmt = self.compute_time_fmt
        cached_count = self.cached_count
        failed_count = self.failed_count
        ignored_count = self.ignored_count
        succeed_count = self.succeed_count
        cached_count_fmt = self.cached_count_fmt
        succeed_count_fmt = self.succeed_count_fmt
        failed_count_fmt = self.failed_count_fmt
        ignored_count_fmt = self.ignored_count_fmt
        cached_pct = self.cached_pct
        failed_pct = self.failed_pct
        succeed_pct = self.succeed_pct
        ignored_pct = self.ignored_pct
        cached_duration = self.cached_duration
        failed_duration = self.failed_duration
        succeed_duration = self.succeed_duration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compute_time_fmt is not UNSET:
            field_dict["computeTimeFmt"] = compute_time_fmt
        if cached_count is not UNSET:
            field_dict["cachedCount"] = cached_count
        if failed_count is not UNSET:
            field_dict["failedCount"] = failed_count
        if ignored_count is not UNSET:
            field_dict["ignoredCount"] = ignored_count
        if succeed_count is not UNSET:
            field_dict["succeedCount"] = succeed_count
        if cached_count_fmt is not UNSET:
            field_dict["cachedCountFmt"] = cached_count_fmt
        if succeed_count_fmt is not UNSET:
            field_dict["succeedCountFmt"] = succeed_count_fmt
        if failed_count_fmt is not UNSET:
            field_dict["failedCountFmt"] = failed_count_fmt
        if ignored_count_fmt is not UNSET:
            field_dict["ignoredCountFmt"] = ignored_count_fmt
        if cached_pct is not UNSET:
            field_dict["cachedPct"] = cached_pct
        if failed_pct is not UNSET:
            field_dict["failedPct"] = failed_pct
        if succeed_pct is not UNSET:
            field_dict["succeedPct"] = succeed_pct
        if ignored_pct is not UNSET:
            field_dict["ignoredPct"] = ignored_pct
        if cached_duration is not UNSET:
            field_dict["cachedDuration"] = cached_duration
        if failed_duration is not UNSET:
            field_dict["failedDuration"] = failed_duration
        if succeed_duration is not UNSET:
            field_dict["succeedDuration"] = succeed_duration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        compute_time_fmt = d.pop("computeTimeFmt", UNSET)

        cached_count = d.pop("cachedCount", UNSET)

        failed_count = d.pop("failedCount", UNSET)

        ignored_count = d.pop("ignoredCount", UNSET)

        succeed_count = d.pop("succeedCount", UNSET)

        cached_count_fmt = d.pop("cachedCountFmt", UNSET)

        succeed_count_fmt = d.pop("succeedCountFmt", UNSET)

        failed_count_fmt = d.pop("failedCountFmt", UNSET)

        ignored_count_fmt = d.pop("ignoredCountFmt", UNSET)

        cached_pct = d.pop("cachedPct", UNSET)

        failed_pct = d.pop("failedPct", UNSET)

        succeed_pct = d.pop("succeedPct", UNSET)

        ignored_pct = d.pop("ignoredPct", UNSET)

        cached_duration = d.pop("cachedDuration", UNSET)

        failed_duration = d.pop("failedDuration", UNSET)

        succeed_duration = d.pop("succeedDuration", UNSET)

        wf_stats = cls(
            compute_time_fmt=compute_time_fmt,
            cached_count=cached_count,
            failed_count=failed_count,
            ignored_count=ignored_count,
            succeed_count=succeed_count,
            cached_count_fmt=cached_count_fmt,
            succeed_count_fmt=succeed_count_fmt,
            failed_count_fmt=failed_count_fmt,
            ignored_count_fmt=ignored_count_fmt,
            cached_pct=cached_pct,
            failed_pct=failed_pct,
            succeed_pct=succeed_pct,
            ignored_pct=ignored_pct,
            cached_duration=cached_duration,
            failed_duration=failed_duration,
            succeed_duration=succeed_duration,
        )

        wf_stats.additional_properties = d
        return wf_stats

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
