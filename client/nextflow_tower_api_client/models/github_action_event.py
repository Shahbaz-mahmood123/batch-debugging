import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubActionEvent")


@_attrs_define
class GithubActionEvent:
    """
    Attributes:
        ref (Union[Unset, str]):
        commit_id (Union[Unset, str]):
        commit_message (Union[Unset, str]):
        pusher_name (Union[Unset, str]):
        pusher_email (Union[Unset, str]):
        timestamp (Union[Unset, datetime.datetime]):
        discriminator (Union[Unset, str]):
    """

    ref: Union[Unset, str] = UNSET
    commit_id: Union[Unset, str] = UNSET
    commit_message: Union[Unset, str] = UNSET
    pusher_name: Union[Unset, str] = UNSET
    pusher_email: Union[Unset, str] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    discriminator: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ref = self.ref
        commit_id = self.commit_id
        commit_message = self.commit_message
        pusher_name = self.pusher_name
        pusher_email = self.pusher_email
        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        discriminator = self.discriminator

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ref is not UNSET:
            field_dict["ref"] = ref
        if commit_id is not UNSET:
            field_dict["commitId"] = commit_id
        if commit_message is not UNSET:
            field_dict["commitMessage"] = commit_message
        if pusher_name is not UNSET:
            field_dict["pusherName"] = pusher_name
        if pusher_email is not UNSET:
            field_dict["pusherEmail"] = pusher_email
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if discriminator is not UNSET:
            field_dict["discriminator"] = discriminator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ref = d.pop("ref", UNSET)

        commit_id = d.pop("commitId", UNSET)

        commit_message = d.pop("commitMessage", UNSET)

        pusher_name = d.pop("pusherName", UNSET)

        pusher_email = d.pop("pusherEmail", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        discriminator = d.pop("discriminator", UNSET)

        github_action_event = cls(
            ref=ref,
            commit_id=commit_id,
            commit_message=commit_message,
            pusher_name=pusher_name,
            pusher_email=pusher_email,
            timestamp=timestamp,
            discriminator=discriminator,
        )

        github_action_event.additional_properties = d
        return github_action_event

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
