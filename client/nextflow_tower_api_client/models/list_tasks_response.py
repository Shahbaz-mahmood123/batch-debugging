from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.describe_task_response import DescribeTaskResponse


T = TypeVar("T", bound="ListTasksResponse")


@_attrs_define
class ListTasksResponse:
    """
    Attributes:
        tasks (Union[Unset, List['DescribeTaskResponse']]):
        total (Union[Unset, int]):
    """

    tasks: Union[Unset, List["DescribeTaskResponse"]] = UNSET
    total: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tasks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tasks, Unset):
            tasks = []
            for tasks_item_data in self.tasks:
                tasks_item = tasks_item_data.to_dict()

                tasks.append(tasks_item)

        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.describe_task_response import DescribeTaskResponse

        d = src_dict.copy()
        tasks = []
        _tasks = d.pop("tasks", UNSET)
        for tasks_item_data in _tasks or []:
            tasks_item = DescribeTaskResponse.from_dict(tasks_item_data)

            tasks.append(tasks_item)

        total = d.pop("total", UNSET)

        list_tasks_response = cls(
            tasks=tasks,
            total=total,
        )

        list_tasks_response.additional_properties = d
        return list_tasks_response

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
