import json
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.run_request_tags import RunRequestTags
    from ..models.run_request_workflow_engine_parameters import RunRequestWorkflowEngineParameters
    from ..models.run_request_workflow_params import RunRequestWorkflowParams


T = TypeVar("T", bound="RunRequest")


@_attrs_define
class RunRequest:
    """
    Attributes:
        workflow_params (Union[Unset, RunRequestWorkflowParams]):
        workflow_type (Union[Unset, str]):
        workflow_type_version (Union[Unset, str]):
        tags (Union[Unset, RunRequestTags]):
        workflow_engine_parameters (Union[Unset, RunRequestWorkflowEngineParameters]):
        workflow_url (Union[Unset, str]):
    """

    workflow_params: Union[Unset, "RunRequestWorkflowParams"] = UNSET
    workflow_type: Union[Unset, str] = UNSET
    workflow_type_version: Union[Unset, str] = UNSET
    tags: Union[Unset, "RunRequestTags"] = UNSET
    workflow_engine_parameters: Union[Unset, "RunRequestWorkflowEngineParameters"] = UNSET
    workflow_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        workflow_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workflow_params, Unset):
            workflow_params = self.workflow_params.to_dict()

        workflow_type = self.workflow_type
        workflow_type_version = self.workflow_type_version
        tags: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        workflow_engine_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workflow_engine_parameters, Unset):
            workflow_engine_parameters = self.workflow_engine_parameters.to_dict()

        workflow_url = self.workflow_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workflow_params is not UNSET:
            field_dict["workflow_params"] = workflow_params
        if workflow_type is not UNSET:
            field_dict["workflow_type"] = workflow_type
        if workflow_type_version is not UNSET:
            field_dict["workflow_type_version"] = workflow_type_version
        if tags is not UNSET:
            field_dict["tags"] = tags
        if workflow_engine_parameters is not UNSET:
            field_dict["workflow_engine_parameters"] = workflow_engine_parameters
        if workflow_url is not UNSET:
            field_dict["workflow_url"] = workflow_url

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        workflow_params: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.workflow_params, Unset):
            workflow_params = (None, json.dumps(self.workflow_params.to_dict()).encode(), "application/json")

        workflow_type = (
            self.workflow_type
            if isinstance(self.workflow_type, Unset)
            else (None, str(self.workflow_type).encode(), "text/plain")
        )
        workflow_type_version = (
            self.workflow_type_version
            if isinstance(self.workflow_type_version, Unset)
            else (None, str(self.workflow_type_version).encode(), "text/plain")
        )
        tags: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = (None, json.dumps(self.tags.to_dict()).encode(), "application/json")

        workflow_engine_parameters: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.workflow_engine_parameters, Unset):
            workflow_engine_parameters = (
                None,
                json.dumps(self.workflow_engine_parameters.to_dict()).encode(),
                "application/json",
            )

        workflow_url = (
            self.workflow_url
            if isinstance(self.workflow_url, Unset)
            else (None, str(self.workflow_url).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if workflow_params is not UNSET:
            field_dict["workflow_params"] = workflow_params
        if workflow_type is not UNSET:
            field_dict["workflow_type"] = workflow_type
        if workflow_type_version is not UNSET:
            field_dict["workflow_type_version"] = workflow_type_version
        if tags is not UNSET:
            field_dict["tags"] = tags
        if workflow_engine_parameters is not UNSET:
            field_dict["workflow_engine_parameters"] = workflow_engine_parameters
        if workflow_url is not UNSET:
            field_dict["workflow_url"] = workflow_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.run_request_tags import RunRequestTags
        from ..models.run_request_workflow_engine_parameters import RunRequestWorkflowEngineParameters
        from ..models.run_request_workflow_params import RunRequestWorkflowParams

        d = src_dict.copy()
        _workflow_params = d.pop("workflow_params", UNSET)
        workflow_params: Union[Unset, RunRequestWorkflowParams]
        if isinstance(_workflow_params, Unset):
            workflow_params = UNSET
        else:
            workflow_params = RunRequestWorkflowParams.from_dict(_workflow_params)

        workflow_type = d.pop("workflow_type", UNSET)

        workflow_type_version = d.pop("workflow_type_version", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: Union[Unset, RunRequestTags]
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = RunRequestTags.from_dict(_tags)

        _workflow_engine_parameters = d.pop("workflow_engine_parameters", UNSET)
        workflow_engine_parameters: Union[Unset, RunRequestWorkflowEngineParameters]
        if isinstance(_workflow_engine_parameters, Unset):
            workflow_engine_parameters = UNSET
        else:
            workflow_engine_parameters = RunRequestWorkflowEngineParameters.from_dict(_workflow_engine_parameters)

        workflow_url = d.pop("workflow_url", UNSET)

        run_request = cls(
            workflow_params=workflow_params,
            workflow_type=workflow_type,
            workflow_type_version=workflow_type_version,
            tags=tags,
            workflow_engine_parameters=workflow_engine_parameters,
            workflow_url=workflow_url,
        )

        run_request.additional_properties = d
        return run_request

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
