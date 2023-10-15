import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="UserDbDto")


@_attrs_define
class UserDbDto:
    """
    Attributes:
        id (int):
        user_name (str):
        email (str):
        first_name (str):
        last_name (str):
        organization (str):
        description (str):
        avatar (str):
        avatar_id (str):
        notification (bool):
        terms_of_use_consent (bool):
        marketing_consent (bool):
        last_access (datetime.datetime):
        date_created (datetime.datetime):
        last_updated (datetime.datetime):
        deleted (bool):
    """

    id: int
    user_name: str
    email: str
    first_name: str
    last_name: str
    organization: str
    description: str
    avatar: str
    avatar_id: str
    notification: bool
    terms_of_use_consent: bool
    marketing_consent: bool
    last_access: datetime.datetime
    date_created: datetime.datetime
    last_updated: datetime.datetime
    deleted: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        user_name = self.user_name
        email = self.email
        first_name = self.first_name
        last_name = self.last_name
        organization = self.organization
        description = self.description
        avatar = self.avatar
        avatar_id = self.avatar_id
        notification = self.notification
        terms_of_use_consent = self.terms_of_use_consent
        marketing_consent = self.marketing_consent
        last_access = self.last_access.isoformat()

        date_created = self.date_created.isoformat()

        last_updated = self.last_updated.isoformat()

        deleted = self.deleted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "userName": user_name,
                "email": email,
                "firstName": first_name,
                "lastName": last_name,
                "organization": organization,
                "description": description,
                "avatar": avatar,
                "avatarId": avatar_id,
                "notification": notification,
                "termsOfUseConsent": terms_of_use_consent,
                "marketingConsent": marketing_consent,
                "lastAccess": last_access,
                "dateCreated": date_created,
                "lastUpdated": last_updated,
                "deleted": deleted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        user_name = d.pop("userName")

        email = d.pop("email")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        organization = d.pop("organization")

        description = d.pop("description")

        avatar = d.pop("avatar")

        avatar_id = d.pop("avatarId")

        notification = d.pop("notification")

        terms_of_use_consent = d.pop("termsOfUseConsent")

        marketing_consent = d.pop("marketingConsent")

        last_access = isoparse(d.pop("lastAccess"))

        date_created = isoparse(d.pop("dateCreated"))

        last_updated = isoparse(d.pop("lastUpdated"))

        deleted = d.pop("deleted")

        user_db_dto = cls(
            id=id,
            user_name=user_name,
            email=email,
            first_name=first_name,
            last_name=last_name,
            organization=organization,
            description=description,
            avatar=avatar,
            avatar_id=avatar_id,
            notification=notification,
            terms_of_use_consent=terms_of_use_consent,
            marketing_consent=marketing_consent,
            last_access=last_access,
            date_created=date_created,
            last_updated=last_updated,
            deleted=deleted,
        )

        user_db_dto.additional_properties = d
        return user_db_dto

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
