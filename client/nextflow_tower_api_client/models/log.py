from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Log")


@_attrs_define
class Log:
    """
    Attributes:
        name (Union[Unset, str]):
        cmd (Union[Unset, List[str]]):
        start_time (Union[Unset, str]):
        end_time (Union[Unset, str]):
        stdout (Union[Unset, str]):
        stderr (Union[Unset, str]):
        exit_code (Union[Unset, int]):
    """

    name: Union[Unset, str] = UNSET
    cmd: Union[Unset, List[str]] = UNSET
    start_time: Union[Unset, str] = UNSET
    end_time: Union[Unset, str] = UNSET
    stdout: Union[Unset, str] = UNSET
    stderr: Union[Unset, str] = UNSET
    exit_code: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        cmd: Union[Unset, List[str]] = UNSET
        if not isinstance(self.cmd, Unset):
            cmd = self.cmd

        start_time = self.start_time
        end_time = self.end_time
        stdout = self.stdout
        stderr = self.stderr
        exit_code = self.exit_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if cmd is not UNSET:
            field_dict["cmd"] = cmd
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if stdout is not UNSET:
            field_dict["stdout"] = stdout
        if stderr is not UNSET:
            field_dict["stderr"] = stderr
        if exit_code is not UNSET:
            field_dict["exit_code"] = exit_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        cmd = cast(List[str], d.pop("cmd", UNSET))

        start_time = d.pop("start_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        stdout = d.pop("stdout", UNSET)

        stderr = d.pop("stderr", UNSET)

        exit_code = d.pop("exit_code", UNSET)

        log = cls(
            name=name,
            cmd=cmd,
            start_time=start_time,
            end_time=end_time,
            stdout=stdout,
            stderr=stderr,
            exit_code=exit_code,
        )

        log.additional_properties = d
        return log

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
