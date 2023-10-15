import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessLoad")


@_attrs_define
class ProcessLoad:
    """
    Attributes:
        pending (int):
        submitted (int):
        running (int):
        succeeded (int):
        failed (int):
        cached (int):
        process (str):
        cpus (int):
        cpu_time (int):
        cpu_load (int):
        memory_rss (int):
        memory_req (int):
        read_bytes (int):
        write_bytes (int):
        vol_ctx_switch (int):
        inv_ctx_switch (int):
        load_tasks (int):
        load_cpus (int):
        load_memory (int):
        peak_cpus (int):
        peak_tasks (int):
        peak_memory (int):
        memory_efficiency (Union[Unset, float]):
        cpu_efficiency (Union[Unset, float]):
        date_created (Union[Unset, datetime.datetime]):
        last_updated (Union[Unset, datetime.datetime]):
    """

    pending: int
    submitted: int
    running: int
    succeeded: int
    failed: int
    cached: int
    process: str
    cpus: int
    cpu_time: int
    cpu_load: int
    memory_rss: int
    memory_req: int
    read_bytes: int
    write_bytes: int
    vol_ctx_switch: int
    inv_ctx_switch: int
    load_tasks: int
    load_cpus: int
    load_memory: int
    peak_cpus: int
    peak_tasks: int
    peak_memory: int
    memory_efficiency: Union[Unset, float] = UNSET
    cpu_efficiency: Union[Unset, float] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pending = self.pending
        submitted = self.submitted
        running = self.running
        succeeded = self.succeeded
        failed = self.failed
        cached = self.cached
        process = self.process
        cpus = self.cpus
        cpu_time = self.cpu_time
        cpu_load = self.cpu_load
        memory_rss = self.memory_rss
        memory_req = self.memory_req
        read_bytes = self.read_bytes
        write_bytes = self.write_bytes
        vol_ctx_switch = self.vol_ctx_switch
        inv_ctx_switch = self.inv_ctx_switch
        load_tasks = self.load_tasks
        load_cpus = self.load_cpus
        load_memory = self.load_memory
        peak_cpus = self.peak_cpus
        peak_tasks = self.peak_tasks
        peak_memory = self.peak_memory
        memory_efficiency = self.memory_efficiency
        cpu_efficiency = self.cpu_efficiency
        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pending": pending,
                "submitted": submitted,
                "running": running,
                "succeeded": succeeded,
                "failed": failed,
                "cached": cached,
                "process": process,
                "cpus": cpus,
                "cpuTime": cpu_time,
                "cpuLoad": cpu_load,
                "memoryRss": memory_rss,
                "memoryReq": memory_req,
                "readBytes": read_bytes,
                "writeBytes": write_bytes,
                "volCtxSwitch": vol_ctx_switch,
                "invCtxSwitch": inv_ctx_switch,
                "loadTasks": load_tasks,
                "loadCpus": load_cpus,
                "loadMemory": load_memory,
                "peakCpus": peak_cpus,
                "peakTasks": peak_tasks,
                "peakMemory": peak_memory,
            }
        )
        if memory_efficiency is not UNSET:
            field_dict["memoryEfficiency"] = memory_efficiency
        if cpu_efficiency is not UNSET:
            field_dict["cpuEfficiency"] = cpu_efficiency
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pending = d.pop("pending")

        submitted = d.pop("submitted")

        running = d.pop("running")

        succeeded = d.pop("succeeded")

        failed = d.pop("failed")

        cached = d.pop("cached")

        process = d.pop("process")

        cpus = d.pop("cpus")

        cpu_time = d.pop("cpuTime")

        cpu_load = d.pop("cpuLoad")

        memory_rss = d.pop("memoryRss")

        memory_req = d.pop("memoryReq")

        read_bytes = d.pop("readBytes")

        write_bytes = d.pop("writeBytes")

        vol_ctx_switch = d.pop("volCtxSwitch")

        inv_ctx_switch = d.pop("invCtxSwitch")

        load_tasks = d.pop("loadTasks")

        load_cpus = d.pop("loadCpus")

        load_memory = d.pop("loadMemory")

        peak_cpus = d.pop("peakCpus")

        peak_tasks = d.pop("peakTasks")

        peak_memory = d.pop("peakMemory")

        memory_efficiency = d.pop("memoryEfficiency", UNSET)

        cpu_efficiency = d.pop("cpuEfficiency", UNSET)

        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        process_load = cls(
            pending=pending,
            submitted=submitted,
            running=running,
            succeeded=succeeded,
            failed=failed,
            cached=cached,
            process=process,
            cpus=cpus,
            cpu_time=cpu_time,
            cpu_load=cpu_load,
            memory_rss=memory_rss,
            memory_req=memory_req,
            read_bytes=read_bytes,
            write_bytes=write_bytes,
            vol_ctx_switch=vol_ctx_switch,
            inv_ctx_switch=inv_ctx_switch,
            load_tasks=load_tasks,
            load_cpus=load_cpus,
            load_memory=load_memory,
            peak_cpus=peak_cpus,
            peak_tasks=peak_tasks,
            peak_memory=peak_memory,
            memory_efficiency=memory_efficiency,
            cpu_efficiency=cpu_efficiency,
            date_created=date_created,
            last_updated=last_updated,
        )

        process_load.additional_properties = d
        return process_load

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
