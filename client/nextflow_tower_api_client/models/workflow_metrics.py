from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_data import ResourceData


T = TypeVar("T", bound="WorkflowMetrics")


@_attrs_define
class WorkflowMetrics:
    """
    Attributes:
        process (str):
        id (Union[Unset, None, int]):
        cpu (Union[Unset, ResourceData]):
        mem (Union[Unset, ResourceData]):
        vmem (Union[Unset, ResourceData]):
        time (Union[Unset, ResourceData]):
        reads (Union[Unset, ResourceData]):
        writes (Union[Unset, ResourceData]):
        cpu_usage (Union[Unset, ResourceData]):
        mem_usage (Union[Unset, ResourceData]):
        time_usage (Union[Unset, ResourceData]):
    """

    process: str
    id: Union[Unset, None, int] = UNSET
    cpu: Union[Unset, "ResourceData"] = UNSET
    mem: Union[Unset, "ResourceData"] = UNSET
    vmem: Union[Unset, "ResourceData"] = UNSET
    time: Union[Unset, "ResourceData"] = UNSET
    reads: Union[Unset, "ResourceData"] = UNSET
    writes: Union[Unset, "ResourceData"] = UNSET
    cpu_usage: Union[Unset, "ResourceData"] = UNSET
    mem_usage: Union[Unset, "ResourceData"] = UNSET
    time_usage: Union[Unset, "ResourceData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        process = self.process
        id = self.id
        cpu: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cpu, Unset):
            cpu = self.cpu.to_dict()

        mem: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mem, Unset):
            mem = self.mem.to_dict()

        vmem: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vmem, Unset):
            vmem = self.vmem.to_dict()

        time: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.to_dict()

        reads: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reads, Unset):
            reads = self.reads.to_dict()

        writes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.writes, Unset):
            writes = self.writes.to_dict()

        cpu_usage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cpu_usage, Unset):
            cpu_usage = self.cpu_usage.to_dict()

        mem_usage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mem_usage, Unset):
            mem_usage = self.mem_usage.to_dict()

        time_usage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time_usage, Unset):
            time_usage = self.time_usage.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "process": process,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if mem is not UNSET:
            field_dict["mem"] = mem
        if vmem is not UNSET:
            field_dict["vmem"] = vmem
        if time is not UNSET:
            field_dict["time"] = time
        if reads is not UNSET:
            field_dict["reads"] = reads
        if writes is not UNSET:
            field_dict["writes"] = writes
        if cpu_usage is not UNSET:
            field_dict["cpuUsage"] = cpu_usage
        if mem_usage is not UNSET:
            field_dict["memUsage"] = mem_usage
        if time_usage is not UNSET:
            field_dict["timeUsage"] = time_usage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.resource_data import ResourceData

        d = src_dict.copy()
        process = d.pop("process")

        id = d.pop("id", UNSET)

        _cpu = d.pop("cpu", UNSET)
        cpu: Union[Unset, ResourceData]
        if isinstance(_cpu, Unset):
            cpu = UNSET
        else:
            cpu = ResourceData.from_dict(_cpu)

        _mem = d.pop("mem", UNSET)
        mem: Union[Unset, ResourceData]
        if isinstance(_mem, Unset):
            mem = UNSET
        else:
            mem = ResourceData.from_dict(_mem)

        _vmem = d.pop("vmem", UNSET)
        vmem: Union[Unset, ResourceData]
        if isinstance(_vmem, Unset):
            vmem = UNSET
        else:
            vmem = ResourceData.from_dict(_vmem)

        _time = d.pop("time", UNSET)
        time: Union[Unset, ResourceData]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = ResourceData.from_dict(_time)

        _reads = d.pop("reads", UNSET)
        reads: Union[Unset, ResourceData]
        if isinstance(_reads, Unset):
            reads = UNSET
        else:
            reads = ResourceData.from_dict(_reads)

        _writes = d.pop("writes", UNSET)
        writes: Union[Unset, ResourceData]
        if isinstance(_writes, Unset):
            writes = UNSET
        else:
            writes = ResourceData.from_dict(_writes)

        _cpu_usage = d.pop("cpuUsage", UNSET)
        cpu_usage: Union[Unset, ResourceData]
        if isinstance(_cpu_usage, Unset):
            cpu_usage = UNSET
        else:
            cpu_usage = ResourceData.from_dict(_cpu_usage)

        _mem_usage = d.pop("memUsage", UNSET)
        mem_usage: Union[Unset, ResourceData]
        if isinstance(_mem_usage, Unset):
            mem_usage = UNSET
        else:
            mem_usage = ResourceData.from_dict(_mem_usage)

        _time_usage = d.pop("timeUsage", UNSET)
        time_usage: Union[Unset, ResourceData]
        if isinstance(_time_usage, Unset):
            time_usage = UNSET
        else:
            time_usage = ResourceData.from_dict(_time_usage)

        workflow_metrics = cls(
            process=process,
            id=id,
            cpu=cpu,
            mem=mem,
            vmem=vmem,
            time=time,
            reads=reads,
            writes=writes,
            cpu_usage=cpu_usage,
            mem_usage=mem_usage,
            time_usage=time_usage,
        )

        workflow_metrics.additional_properties = d
        return workflow_metrics

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
