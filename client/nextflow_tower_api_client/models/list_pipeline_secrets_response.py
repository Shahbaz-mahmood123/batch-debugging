from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pipeline_secret import PipelineSecret


T = TypeVar("T", bound="ListPipelineSecretsResponse")


@_attrs_define
class ListPipelineSecretsResponse:
    """
    Attributes:
        pipeline_secrets (Union[Unset, List['PipelineSecret']]):
        total_size (Union[Unset, int]):
    """

    pipeline_secrets: Union[Unset, List["PipelineSecret"]] = UNSET
    total_size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pipeline_secrets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pipeline_secrets, Unset):
            pipeline_secrets = []
            for pipeline_secrets_item_data in self.pipeline_secrets:
                pipeline_secrets_item = pipeline_secrets_item_data.to_dict()

                pipeline_secrets.append(pipeline_secrets_item)

        total_size = self.total_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pipeline_secrets is not UNSET:
            field_dict["pipelineSecrets"] = pipeline_secrets
        if total_size is not UNSET:
            field_dict["totalSize"] = total_size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pipeline_secret import PipelineSecret

        d = src_dict.copy()
        pipeline_secrets = []
        _pipeline_secrets = d.pop("pipelineSecrets", UNSET)
        for pipeline_secrets_item_data in _pipeline_secrets or []:
            pipeline_secrets_item = PipelineSecret.from_dict(pipeline_secrets_item_data)

            pipeline_secrets.append(pipeline_secrets_item)

        total_size = d.pop("totalSize", UNSET)

        list_pipeline_secrets_response = cls(
            pipeline_secrets=pipeline_secrets,
            total_size=total_size,
        )

        list_pipeline_secrets_response.additional_properties = d
        return list_pipeline_secrets_response

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
