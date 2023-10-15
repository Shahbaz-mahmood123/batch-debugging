from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trace_progress_detail import TraceProgressDetail


T = TypeVar("T", bound="TraceProgressData")


@_attrs_define
class TraceProgressData:
    """
    Attributes:
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
        load_cpus (Union[Unset, int]):
        load_memory (Union[Unset, int]):
        peak_running (Union[Unset, int]):
        peak_cpus (Union[Unset, int]):
        peak_memory (Union[Unset, int]):
        processes (Union[Unset, List['TraceProgressDetail']]):
    """

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
    load_cpus: Union[Unset, int] = UNSET
    load_memory: Union[Unset, int] = UNSET
    peak_running: Union[Unset, int] = UNSET
    peak_cpus: Union[Unset, int] = UNSET
    peak_memory: Union[Unset, int] = UNSET
    processes: Union[Unset, List["TraceProgressDetail"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        load_cpus = self.load_cpus
        load_memory = self.load_memory
        peak_running = self.peak_running
        peak_cpus = self.peak_cpus
        peak_memory = self.peak_memory
        processes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.processes, Unset):
            processes = []
            for processes_item_data in self.processes:
                processes_item = processes_item_data.to_dict()

                processes.append(processes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if processes is not UNSET:
            field_dict["processes"] = processes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.trace_progress_detail import TraceProgressDetail

        d = src_dict.copy()
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

        load_cpus = d.pop("loadCpus", UNSET)

        load_memory = d.pop("loadMemory", UNSET)

        peak_running = d.pop("peakRunning", UNSET)

        peak_cpus = d.pop("peakCpus", UNSET)

        peak_memory = d.pop("peakMemory", UNSET)

        processes = []
        _processes = d.pop("processes", UNSET)
        for processes_item_data in _processes or []:
            processes_item = TraceProgressDetail.from_dict(processes_item_data)

            processes.append(processes_item)

        trace_progress_data = cls(
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
            load_cpus=load_cpus,
            load_memory=load_memory,
            peak_running=peak_running,
            peak_cpus=peak_cpus,
            peak_memory=peak_memory,
            processes=processes,
        )

        trace_progress_data.additional_properties = d
        return trace_progress_data

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
