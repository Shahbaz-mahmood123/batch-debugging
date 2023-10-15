import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.cloud_price_model import CloudPriceModel
from ..models.task_status import TaskStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Task")


@_attrs_define
class Task:
    """
    Attributes:
        task_id (int):
        status (TaskStatus):
        hash_ (Union[Unset, str]):
        name (Union[Unset, str]):
        process (Union[Unset, str]):
        tag (Union[Unset, str]):
        submit (Union[Unset, datetime.datetime]):
        start (Union[Unset, datetime.datetime]):
        complete (Union[Unset, datetime.datetime]):
        module (Union[Unset, List[str]]):
        container (Union[Unset, str]):
        attempt (Union[Unset, int]):
        script (Union[Unset, str]):
        scratch (Union[Unset, str]):
        workdir (Union[Unset, str]):
        queue (Union[Unset, str]):
        cpus (Union[Unset, int]):
        memory (Union[Unset, int]):
        disk (Union[Unset, int]):
        time (Union[Unset, int]):
        env (Union[Unset, str]):
        executor (Union[Unset, str]):
        machine_type (Union[Unset, str]):
        cloud_zone (Union[Unset, str]):
        price_model (Union[Unset, CloudPriceModel]):
        cost (Union[Unset, float]):
        error_action (Union[Unset, str]):
        exit_status (Union[Unset, int]):
        duration (Union[Unset, int]):
        realtime (Union[Unset, int]):
        native_id (Union[Unset, str]):
        pcpu (Union[Unset, float]):
        pmem (Union[Unset, float]):
        rss (Union[Unset, int]):
        vmem (Union[Unset, int]):
        peak_rss (Union[Unset, int]):
        peak_vmem (Union[Unset, int]):
        rchar (Union[Unset, int]):
        wchar (Union[Unset, int]):
        syscr (Union[Unset, int]):
        syscw (Union[Unset, int]):
        read_bytes (Union[Unset, int]):
        write_bytes (Union[Unset, int]):
        vol_ctxt (Union[Unset, int]):
        inv_ctxt (Union[Unset, int]):
        exit_ (Union[Unset, str]):
        id (Union[Unset, None, int]):
        date_created (Union[Unset, None, datetime.datetime]):
        last_updated (Union[Unset, None, datetime.datetime]):
    """

    task_id: int
    status: TaskStatus
    hash_: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    process: Union[Unset, str] = UNSET
    tag: Union[Unset, str] = UNSET
    submit: Union[Unset, datetime.datetime] = UNSET
    start: Union[Unset, datetime.datetime] = UNSET
    complete: Union[Unset, datetime.datetime] = UNSET
    module: Union[Unset, List[str]] = UNSET
    container: Union[Unset, str] = UNSET
    attempt: Union[Unset, int] = UNSET
    script: Union[Unset, str] = UNSET
    scratch: Union[Unset, str] = UNSET
    workdir: Union[Unset, str] = UNSET
    queue: Union[Unset, str] = UNSET
    cpus: Union[Unset, int] = UNSET
    memory: Union[Unset, int] = UNSET
    disk: Union[Unset, int] = UNSET
    time: Union[Unset, int] = UNSET
    env: Union[Unset, str] = UNSET
    executor: Union[Unset, str] = UNSET
    machine_type: Union[Unset, str] = UNSET
    cloud_zone: Union[Unset, str] = UNSET
    price_model: Union[Unset, CloudPriceModel] = UNSET
    cost: Union[Unset, float] = UNSET
    error_action: Union[Unset, str] = UNSET
    exit_status: Union[Unset, int] = UNSET
    duration: Union[Unset, int] = UNSET
    realtime: Union[Unset, int] = UNSET
    native_id: Union[Unset, str] = UNSET
    pcpu: Union[Unset, float] = UNSET
    pmem: Union[Unset, float] = UNSET
    rss: Union[Unset, int] = UNSET
    vmem: Union[Unset, int] = UNSET
    peak_rss: Union[Unset, int] = UNSET
    peak_vmem: Union[Unset, int] = UNSET
    rchar: Union[Unset, int] = UNSET
    wchar: Union[Unset, int] = UNSET
    syscr: Union[Unset, int] = UNSET
    syscw: Union[Unset, int] = UNSET
    read_bytes: Union[Unset, int] = UNSET
    write_bytes: Union[Unset, int] = UNSET
    vol_ctxt: Union[Unset, int] = UNSET
    inv_ctxt: Union[Unset, int] = UNSET
    exit_: Union[Unset, str] = UNSET
    id: Union[Unset, None, int] = UNSET
    date_created: Union[Unset, None, datetime.datetime] = UNSET
    last_updated: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        task_id = self.task_id
        status = self.status.value

        hash_ = self.hash_
        name = self.name
        process = self.process
        tag = self.tag
        submit: Union[Unset, str] = UNSET
        if not isinstance(self.submit, Unset):
            submit = self.submit.isoformat()

        start: Union[Unset, str] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        complete: Union[Unset, str] = UNSET
        if not isinstance(self.complete, Unset):
            complete = self.complete.isoformat()

        module: Union[Unset, List[str]] = UNSET
        if not isinstance(self.module, Unset):
            module = self.module

        container = self.container
        attempt = self.attempt
        script = self.script
        scratch = self.scratch
        workdir = self.workdir
        queue = self.queue
        cpus = self.cpus
        memory = self.memory
        disk = self.disk
        time = self.time
        env = self.env
        executor = self.executor
        machine_type = self.machine_type
        cloud_zone = self.cloud_zone
        price_model: Union[Unset, str] = UNSET
        if not isinstance(self.price_model, Unset):
            price_model = self.price_model.value

        cost = self.cost
        error_action = self.error_action
        exit_status = self.exit_status
        duration = self.duration
        realtime = self.realtime
        native_id = self.native_id
        pcpu = self.pcpu
        pmem = self.pmem
        rss = self.rss
        vmem = self.vmem
        peak_rss = self.peak_rss
        peak_vmem = self.peak_vmem
        rchar = self.rchar
        wchar = self.wchar
        syscr = self.syscr
        syscw = self.syscw
        read_bytes = self.read_bytes
        write_bytes = self.write_bytes
        vol_ctxt = self.vol_ctxt
        inv_ctxt = self.inv_ctxt
        exit_ = self.exit_
        id = self.id
        date_created: Union[Unset, None, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat() if self.date_created else None

        last_updated: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat() if self.last_updated else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "taskId": task_id,
                "status": status,
            }
        )
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if name is not UNSET:
            field_dict["name"] = name
        if process is not UNSET:
            field_dict["process"] = process
        if tag is not UNSET:
            field_dict["tag"] = tag
        if submit is not UNSET:
            field_dict["submit"] = submit
        if start is not UNSET:
            field_dict["start"] = start
        if complete is not UNSET:
            field_dict["complete"] = complete
        if module is not UNSET:
            field_dict["module"] = module
        if container is not UNSET:
            field_dict["container"] = container
        if attempt is not UNSET:
            field_dict["attempt"] = attempt
        if script is not UNSET:
            field_dict["script"] = script
        if scratch is not UNSET:
            field_dict["scratch"] = scratch
        if workdir is not UNSET:
            field_dict["workdir"] = workdir
        if queue is not UNSET:
            field_dict["queue"] = queue
        if cpus is not UNSET:
            field_dict["cpus"] = cpus
        if memory is not UNSET:
            field_dict["memory"] = memory
        if disk is not UNSET:
            field_dict["disk"] = disk
        if time is not UNSET:
            field_dict["time"] = time
        if env is not UNSET:
            field_dict["env"] = env
        if executor is not UNSET:
            field_dict["executor"] = executor
        if machine_type is not UNSET:
            field_dict["machineType"] = machine_type
        if cloud_zone is not UNSET:
            field_dict["cloudZone"] = cloud_zone
        if price_model is not UNSET:
            field_dict["priceModel"] = price_model
        if cost is not UNSET:
            field_dict["cost"] = cost
        if error_action is not UNSET:
            field_dict["errorAction"] = error_action
        if exit_status is not UNSET:
            field_dict["exitStatus"] = exit_status
        if duration is not UNSET:
            field_dict["duration"] = duration
        if realtime is not UNSET:
            field_dict["realtime"] = realtime
        if native_id is not UNSET:
            field_dict["nativeId"] = native_id
        if pcpu is not UNSET:
            field_dict["pcpu"] = pcpu
        if pmem is not UNSET:
            field_dict["pmem"] = pmem
        if rss is not UNSET:
            field_dict["rss"] = rss
        if vmem is not UNSET:
            field_dict["vmem"] = vmem
        if peak_rss is not UNSET:
            field_dict["peakRss"] = peak_rss
        if peak_vmem is not UNSET:
            field_dict["peakVmem"] = peak_vmem
        if rchar is not UNSET:
            field_dict["rchar"] = rchar
        if wchar is not UNSET:
            field_dict["wchar"] = wchar
        if syscr is not UNSET:
            field_dict["syscr"] = syscr
        if syscw is not UNSET:
            field_dict["syscw"] = syscw
        if read_bytes is not UNSET:
            field_dict["readBytes"] = read_bytes
        if write_bytes is not UNSET:
            field_dict["writeBytes"] = write_bytes
        if vol_ctxt is not UNSET:
            field_dict["volCtxt"] = vol_ctxt
        if inv_ctxt is not UNSET:
            field_dict["invCtxt"] = inv_ctxt
        if exit_ is not UNSET:
            field_dict["exit"] = exit_
        if id is not UNSET:
            field_dict["id"] = id
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        task_id = d.pop("taskId")

        status = TaskStatus(d.pop("status"))

        hash_ = d.pop("hash", UNSET)

        name = d.pop("name", UNSET)

        process = d.pop("process", UNSET)

        tag = d.pop("tag", UNSET)

        _submit = d.pop("submit", UNSET)
        submit: Union[Unset, datetime.datetime]
        if isinstance(_submit, Unset):
            submit = UNSET
        else:
            submit = isoparse(_submit)

        _start = d.pop("start", UNSET)
        start: Union[Unset, datetime.datetime]
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = isoparse(_start)

        _complete = d.pop("complete", UNSET)
        complete: Union[Unset, datetime.datetime]
        if isinstance(_complete, Unset):
            complete = UNSET
        else:
            complete = isoparse(_complete)

        module = cast(List[str], d.pop("module", UNSET))

        container = d.pop("container", UNSET)

        attempt = d.pop("attempt", UNSET)

        script = d.pop("script", UNSET)

        scratch = d.pop("scratch", UNSET)

        workdir = d.pop("workdir", UNSET)

        queue = d.pop("queue", UNSET)

        cpus = d.pop("cpus", UNSET)

        memory = d.pop("memory", UNSET)

        disk = d.pop("disk", UNSET)

        time = d.pop("time", UNSET)

        env = d.pop("env", UNSET)

        executor = d.pop("executor", UNSET)

        machine_type = d.pop("machineType", UNSET)

        cloud_zone = d.pop("cloudZone", UNSET)

        _price_model = d.pop("priceModel", UNSET)
        price_model: Union[Unset, CloudPriceModel]
        if isinstance(_price_model, Unset):
            price_model = UNSET
        else:
            price_model = CloudPriceModel(_price_model)

        cost = d.pop("cost", UNSET)

        error_action = d.pop("errorAction", UNSET)

        exit_status = d.pop("exitStatus", UNSET)

        duration = d.pop("duration", UNSET)

        realtime = d.pop("realtime", UNSET)

        native_id = d.pop("nativeId", UNSET)

        pcpu = d.pop("pcpu", UNSET)

        pmem = d.pop("pmem", UNSET)

        rss = d.pop("rss", UNSET)

        vmem = d.pop("vmem", UNSET)

        peak_rss = d.pop("peakRss", UNSET)

        peak_vmem = d.pop("peakVmem", UNSET)

        rchar = d.pop("rchar", UNSET)

        wchar = d.pop("wchar", UNSET)

        syscr = d.pop("syscr", UNSET)

        syscw = d.pop("syscw", UNSET)

        read_bytes = d.pop("readBytes", UNSET)

        write_bytes = d.pop("writeBytes", UNSET)

        vol_ctxt = d.pop("volCtxt", UNSET)

        inv_ctxt = d.pop("invCtxt", UNSET)

        exit_ = d.pop("exit", UNSET)

        id = d.pop("id", UNSET)

        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, None, datetime.datetime]
        if _date_created is None:
            date_created = None
        elif isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, None, datetime.datetime]
        if _last_updated is None:
            last_updated = None
        elif isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        task = cls(
            task_id=task_id,
            status=status,
            hash_=hash_,
            name=name,
            process=process,
            tag=tag,
            submit=submit,
            start=start,
            complete=complete,
            module=module,
            container=container,
            attempt=attempt,
            script=script,
            scratch=scratch,
            workdir=workdir,
            queue=queue,
            cpus=cpus,
            memory=memory,
            disk=disk,
            time=time,
            env=env,
            executor=executor,
            machine_type=machine_type,
            cloud_zone=cloud_zone,
            price_model=price_model,
            cost=cost,
            error_action=error_action,
            exit_status=exit_status,
            duration=duration,
            realtime=realtime,
            native_id=native_id,
            pcpu=pcpu,
            pmem=pmem,
            rss=rss,
            vmem=vmem,
            peak_rss=peak_rss,
            peak_vmem=peak_vmem,
            rchar=rchar,
            wchar=wchar,
            syscr=syscr,
            syscw=syscw,
            read_bytes=read_bytes,
            write_bytes=write_bytes,
            vol_ctxt=vol_ctxt,
            inv_ctxt=inv_ctxt,
            exit_=exit_,
            id=id,
            date_created=date_created,
            last_updated=last_updated,
        )

        task.additional_properties = d
        return task

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
