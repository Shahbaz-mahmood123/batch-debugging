import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessToken")


@_attrs_define
class AccessToken:
    """
    Attributes:
        name (str):
        basic_auth (Union[Unset, str]):
        id (Union[Unset, None, int]):
        last_used (Union[Unset, datetime.datetime]):
        date_created (Union[Unset, datetime.datetime]):
    """

    name: str
    basic_auth: Union[Unset, str] = UNSET
    id: Union[Unset, None, int] = UNSET
    last_used: Union[Unset, datetime.datetime] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        basic_auth = self.basic_auth
        id = self.id
        last_used: Union[Unset, str] = UNSET
        if not isinstance(self.last_used, Unset):
            last_used = self.last_used.isoformat()

        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if basic_auth is not UNSET:
            field_dict["basicAuth"] = basic_auth
        if id is not UNSET:
            field_dict["id"] = id
        if last_used is not UNSET:
            field_dict["lastUsed"] = last_used
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        basic_auth = d.pop("basicAuth", UNSET)

        id = d.pop("id", UNSET)

        _last_used = d.pop("lastUsed", UNSET)
        last_used: Union[Unset, datetime.datetime]
        if isinstance(_last_used, Unset):
            last_used = UNSET
        else:
            last_used = isoparse(_last_used)

        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        access_token = cls(
            name=name,
            basic_auth=basic_auth,
            id=id,
            last_used=last_used,
            date_created=date_created,
        )

        access_token.additional_properties = d
        return access_token

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
