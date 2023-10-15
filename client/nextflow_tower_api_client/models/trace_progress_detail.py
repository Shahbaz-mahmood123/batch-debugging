from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceProgressDetail")


@_attrs_define
class TraceProgressDetail:
    """
    Attributes:
        index (Union[Unset, int]):
        name (Union[Unset, str]):
        pending (Union[Unset, int]):
        submitted (Union[Unset, int]):
        running (Union[Unset, int]):
        succeeded (Union[Unset, int]):
        cached (Union[Unset, int]):
        failed (Union[Unset, int]):
        aborted (Union[Unset, int]):
        stored (Union[Unset, int]):
        ignored (Union[Unset, int]):
        retries (Union[Unset, int]):
        terminated (Union[Unset, bool]):
        load_cpus (Union[Unset, int]):
        load_memory (Union[Unset, int]):
        peak_running (Union[Unset, int]):
        peak_cpus (Union[Unset, int]):
        peak_memory (Union[Unset, int]):
    """

    index: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    pending: Union[Unset, int] = UNSET
    submitted: Union[Unset, int] = UNSET
    running: Union[Unset, int] = UNSET
    succeeded: Union[Unset, int] = UNSET
    cached: Union[Unset, int] = UNSET
    failed: Union[Unset, int] = UNSET
    aborted: Union[Unset, int] = UNSET
    stored: Union[Unset, int] = UNSET
    ignored: Union[Unset, int] = UNSET
    retries: Union[Unset, int] = UNSET
    terminated: Union[Unset, bool] = UNSET
    load_cpus: Union[Unset, int] = UNSET
    load_memory: Union[Unset, int] = UNSET
    peak_running: Union[Unset, int] = UNSET
    peak_cpus: Union[Unset, int] = UNSET
    peak_memory: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        index = self.index
        name = self.name
        pending = self.pending
        submitted = self.submitted
        running = self.running
        succeeded = self.succeeded
        cached = self.cached
        failed = self.failed
        aborted = self.aborted
        stored = self.stored
        ignored = self.ignored
        retries = self.retries
        terminated = self.terminated
        load_cpus = self.load_cpus
        load_memory = self.load_memory
        peak_running = self.peak_running
        peak_cpus = self.peak_cpus
        peak_memory = self.peak_memory

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if index is not UNSET:
            field_dict["index"] = index
        if name is not UNSET:
            field_dict["name"] = name
        if pending is not UNSET:
            field_dict["pending"] = pending
        if submitted is not UNSET:
            field_dict["submitted"] = submitted
        if running is not UNSET:
            field_dict["running"] = running
        if succeeded is not UNSET:
            field_dict["succeeded"] = succeeded
        if cached is not UNSET:
            field_dict["cached"] = cached
        if failed is not UNSET:
            field_dict["failed"] = failed
        if aborted is not UNSET:
            field_dict["aborted"] = aborted
        if stored is not UNSET:
            field_dict["stored"] = stored
        if ignored is not UNSET:
            field_dict["ignored"] = ignored
        if retries is not UNSET:
            field_dict["retries"] = retries
        if terminated is not UNSET:
            field_dict["terminated"] = terminated
        if load_cpus is not UNSET:
            field_dict["loadCpus"] = load_cpus
        if load_memory is not UNSET:
            field_dict["loadMemory"] = load_memory
        if peak_running is not UNSET:
            field_dict["peakRunning"] = peak_running
        if peak_cpus is not UNSET:
            field_dict["peakCpus"] = peak_cpus
        if peak_memory is not UNSET:
            field_dict["peakMemory"] = peak_memory

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        index = d.pop("index", UNSET)

        name = d.pop("name", UNSET)

        pending = d.pop("pending", UNSET)

        submitted = d.pop("submitted", UNSET)

        running = d.pop("running", UNSET)

        succeeded = d.pop("succeeded", UNSET)

        cached = d.pop("cached", UNSET)

        failed = d.pop("failed", UNSET)

        aborted = d.pop("aborted", UNSET)

        stored = d.pop("stored", UNSET)

        ignored = d.pop("ignored", UNSET)

        retries = d.pop("retries", UNSET)

        terminated = d.pop("terminated", UNSET)

        load_cpus = d.pop("loadCpus", UNSET)

        load_memory = d.pop("loadMemory", UNSET)

        peak_running = d.pop("peakRunning", UNSET)

        peak_cpus = d.pop("peakCpus", UNSET)

        peak_memory = d.pop("peakMemory", UNSET)

        trace_progress_detail = cls(
            index=index,
            name=name,
            pending=pending,
            submitted=submitted,
            running=running,
            succeeded=succeeded,
            cached=cached,
            failed=failed,
            aborted=aborted,
            stored=stored,
            ignored=ignored,
            retries=retries,
            terminated=terminated,
            load_cpus=load_cpus,
            load_memory=load_memory,
            peak_running=peak_running,
            peak_cpus=peak_cpus,
            peak_memory=peak_memory,
        )

        trace_progress_detail.additional_properties = d
        return trace_progress_detail

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
