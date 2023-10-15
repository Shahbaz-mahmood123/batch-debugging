from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.state import State
from ..types import UNSET, Unset

T = TypeVar("T", bound="RunStatus")


@_attrs_define
class RunStatus:
    """
    Attributes:
        run_id (Union[Unset, str]):
        state (Union[Unset, State]):
    """

    run_id: Union[Unset, str] = UNSET
    state: Union[Unset, State] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        run_id = self.run_id
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if run_id is not UNSET:
            field_dict["run_id"] = run_id
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        run_id = d.pop("run_id", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, State]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = State(_state)

        run_status = cls(
            run_id=run_id,
            state=state,
        )

        run_status.additional_properties = d
        return run_status

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
