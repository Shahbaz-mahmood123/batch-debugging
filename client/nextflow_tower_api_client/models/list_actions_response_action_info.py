import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.action_source import ActionSource
from ..models.action_status import ActionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_tower_action_event import ActionTowerActionEvent
    from ..models.github_action_event import GithubActionEvent
    from ..models.label_db_dto import LabelDbDto


T = TypeVar("T", bound="ListActionsResponseActionInfo")


@_attrs_define
class ListActionsResponseActionInfo:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        pipeline (Union[Unset, str]):
        source (Union[Unset, ActionSource]):
        status (Union[Unset, ActionStatus]):
        last_seen (Union[Unset, datetime.datetime]):
        date_created (Union[Unset, datetime.datetime]):
        event (Union['ActionTowerActionEvent', 'GithubActionEvent', Unset]):
        endpoint (Union[Unset, str]):
        labels (Union[Unset, List['LabelDbDto']]):
        usage_cmd (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    pipeline: Union[Unset, str] = UNSET
    source: Union[Unset, ActionSource] = UNSET
    status: Union[Unset, ActionStatus] = UNSET
    last_seen: Union[Unset, datetime.datetime] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    event: Union["ActionTowerActionEvent", "GithubActionEvent", Unset] = UNSET
    endpoint: Union[Unset, str] = UNSET
    labels: Union[Unset, List["LabelDbDto"]] = UNSET
    usage_cmd: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.github_action_event import GithubActionEvent

        id = self.id
        name = self.name
        pipeline = self.pipeline
        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        last_seen: Union[Unset, str] = UNSET
        if not isinstance(self.last_seen, Unset):
            last_seen = self.last_seen.isoformat()

        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        event: Union[Dict[str, Any], Unset]
        if isinstance(self.event, Unset):
            event = UNSET

        elif isinstance(self.event, GithubActionEvent):
            event = self.event.to_dict()

        else:
            event = self.event.to_dict()

        endpoint = self.endpoint
        labels: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()

                labels.append(labels_item)

        usage_cmd = self.usage_cmd

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if pipeline is not UNSET:
            field_dict["pipeline"] = pipeline
        if source is not UNSET:
            field_dict["source"] = source
        if status is not UNSET:
            field_dict["status"] = status
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if event is not UNSET:
            field_dict["event"] = event
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if labels is not UNSET:
            field_dict["labels"] = labels
        if usage_cmd is not UNSET:
            field_dict["usageCmd"] = usage_cmd

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.action_tower_action_event import ActionTowerActionEvent
        from ..models.github_action_event import GithubActionEvent
        from ..models.label_db_dto import LabelDbDto

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        pipeline = d.pop("pipeline", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, ActionSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ActionSource(_source)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ActionStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ActionStatus(_status)

        _last_seen = d.pop("lastSeen", UNSET)
        last_seen: Union[Unset, datetime.datetime]
        if isinstance(_last_seen, Unset):
            last_seen = UNSET
        else:
            last_seen = isoparse(_last_seen)

        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        def _parse_event(data: object) -> Union["ActionTowerActionEvent", "GithubActionEvent", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_action_event_type_type_0 = GithubActionEvent.from_dict(data)

                return componentsschemas_action_event_type_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_action_event_type_type_1 = ActionTowerActionEvent.from_dict(data)

            return componentsschemas_action_event_type_type_1

        event = _parse_event(d.pop("event", UNSET))

        endpoint = d.pop("endpoint", UNSET)

        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in _labels or []:
            labels_item = LabelDbDto.from_dict(labels_item_data)

            labels.append(labels_item)

        usage_cmd = d.pop("usageCmd", UNSET)

        list_actions_response_action_info = cls(
            id=id,
            name=name,
            pipeline=pipeline,
            source=source,
            status=status,
            last_seen=last_seen,
            date_created=date_created,
            event=event,
            endpoint=endpoint,
            labels=labels,
            usage_cmd=usage_cmd,
        )

        list_actions_response_action_info.additional_properties = d
        return list_actions_response_action_info

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
