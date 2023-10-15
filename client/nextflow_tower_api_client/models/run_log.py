from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.state import State
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.log import Log
    from ..models.run_log_outputs import RunLogOutputs
    from ..models.run_request import RunRequest


T = TypeVar("T", bound="RunLog")


@_attrs_define
class RunLog:
    """
    Attributes:
        run_id (Union[Unset, str]):
        request (Union[Unset, RunRequest]):
        state (Union[Unset, State]):
        run_log (Union[Unset, Log]):
        task_logs (Union[Unset, List['Log']]):
        outputs (Union[Unset, RunLogOutputs]):
    """

    run_id: Union[Unset, str] = UNSET
    request: Union[Unset, "RunRequest"] = UNSET
    state: Union[Unset, State] = UNSET
    run_log: Union[Unset, "Log"] = UNSET
    task_logs: Union[Unset, List["Log"]] = UNSET
    outputs: Union[Unset, "RunLogOutputs"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        run_id = self.run_id
        request: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.request, Unset):
            request = self.request.to_dict()

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        run_log: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.run_log, Unset):
            run_log = self.run_log.to_dict()

        task_logs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.task_logs, Unset):
            task_logs = []
            for task_logs_item_data in self.task_logs:
                task_logs_item = task_logs_item_data.to_dict()

                task_logs.append(task_logs_item)

        outputs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.outputs, Unset):
            outputs = self.outputs.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if run_id is not UNSET:
            field_dict["run_id"] = run_id
        if request is not UNSET:
            field_dict["request"] = request
        if state is not UNSET:
            field_dict["state"] = state
        if run_log is not UNSET:
            field_dict["run_log"] = run_log
        if task_logs is not UNSET:
            field_dict["task_logs"] = task_logs
        if outputs is not UNSET:
            field_dict["outputs"] = outputs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.log import Log
        from ..models.run_log_outputs import RunLogOutputs
        from ..models.run_request import RunRequest

        d = src_dict.copy()
        run_id = d.pop("run_id", UNSET)

        _request = d.pop("request", UNSET)
        request: Union[Unset, RunRequest]
        if isinstance(_request, Unset):
            request = UNSET
        else:
            request = RunRequest.from_dict(_request)

        _state = d.pop("state", UNSET)
        state: Union[Unset, State]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = State(_state)

        _run_log = d.pop("run_log", UNSET)
        run_log: Union[Unset, Log]
        if isinstance(_run_log, Unset):
            run_log = UNSET
        else:
            run_log = Log.from_dict(_run_log)

        task_logs = []
        _task_logs = d.pop("task_logs", UNSET)
        for task_logs_item_data in _task_logs or []:
            task_logs_item = Log.from_dict(task_logs_item_data)

            task_logs.append(task_logs_item)

        _outputs = d.pop("outputs", UNSET)
        outputs: Union[Unset, RunLogOutputs]
        if isinstance(_outputs, Unset):
            outputs = UNSET
        else:
            outputs = RunLogOutputs.from_dict(_outputs)

        run_log = cls(
            run_id=run_id,
            request=request,
            state=state,
            run_log=run_log,
            task_logs=task_logs,
            outputs=outputs,
        )

        run_log.additional_properties = d
        return run_log

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
