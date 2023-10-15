from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.run_status import RunStatus


T = TypeVar("T", bound="RunListResponse")


@_attrs_define
class RunListResponse:
    """
    Attributes:
        runs (Union[Unset, List['RunStatus']]):
        next_page_token (Union[Unset, str]):
    """

    runs: Union[Unset, List["RunStatus"]] = UNSET
    next_page_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        runs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.runs, Unset):
            runs = []
            for runs_item_data in self.runs:
                runs_item = runs_item_data.to_dict()

                runs.append(runs_item)

        next_page_token = self.next_page_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if runs is not UNSET:
            field_dict["runs"] = runs
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.run_status import RunStatus

        d = src_dict.copy()
        runs = []
        _runs = d.pop("runs", UNSET)
        for runs_item_data in _runs or []:
            runs_item = RunStatus.from_dict(runs_item_data)

            runs.append(runs_item)

        next_page_token = d.pop("next_page_token", UNSET)

        run_list_response = cls(
            runs=runs,
            next_page_token=next_page_token,
        )

        run_list_response.additional_properties = d
        return run_list_response

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
