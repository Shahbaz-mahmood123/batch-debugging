from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pipeline_db_dto import PipelineDbDto


T = TypeVar("T", bound="ListPipelinesResponse")


@_attrs_define
class ListPipelinesResponse:
    """
    Attributes:
        pipelines (Union[Unset, List['PipelineDbDto']]):
        total_size (Union[Unset, int]):
    """

    pipelines: Union[Unset, List["PipelineDbDto"]] = UNSET
    total_size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pipelines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pipelines, Unset):
            pipelines = []
            for pipelines_item_data in self.pipelines:
                pipelines_item = pipelines_item_data.to_dict()

                pipelines.append(pipelines_item)

        total_size = self.total_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pipelines is not UNSET:
            field_dict["pipelines"] = pipelines
        if total_size is not UNSET:
            field_dict["totalSize"] = total_size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pipeline_db_dto import PipelineDbDto

        d = src_dict.copy()
        pipelines = []
        _pipelines = d.pop("pipelines", UNSET)
        for pipelines_item_data in _pipelines or []:
            pipelines_item = PipelineDbDto.from_dict(pipelines_item_data)

            pipelines.append(pipelines_item)

        total_size = d.pop("totalSize", UNSET)

        list_pipelines_response = cls(
            pipelines=pipelines,
            total_size=total_size,
        )

        list_pipelines_response.additional_properties = d
        return list_pipelines_response

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
