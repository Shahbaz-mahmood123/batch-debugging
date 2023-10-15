from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.org_role import OrgRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationDbDto")


@_attrs_define
class OrganizationDbDto:
    """
    Attributes:
        org_id (Union[Unset, int]):
        name (Union[Unset, str]):
        full_name (Union[Unset, str]):
        description (Union[Unset, str]):
        location (Union[Unset, str]):
        website (Union[Unset, str]):
        logo_id (Union[Unset, str]):
        logo_url (Union[Unset, str]):
        member_id (Union[Unset, int]):
        member_role (Union[Unset, OrgRole]):
        paying (Union[Unset, bool]):
    """

    org_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    logo_id: Union[Unset, str] = UNSET
    logo_url: Union[Unset, str] = UNSET
    member_id: Union[Unset, int] = UNSET
    member_role: Union[Unset, OrgRole] = UNSET
    paying: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        org_id = self.org_id
        name = self.name
        full_name = self.full_name
        description = self.description
        location = self.location
        website = self.website
        logo_id = self.logo_id
        logo_url = self.logo_url
        member_id = self.member_id
        member_role: Union[Unset, str] = UNSET
        if not isinstance(self.member_role, Unset):
            member_role = self.member_role.value

        paying = self.paying

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if org_id is not UNSET:
            field_dict["orgId"] = org_id
        if name is not UNSET:
            field_dict["name"] = name
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if description is not UNSET:
            field_dict["description"] = description
        if location is not UNSET:
            field_dict["location"] = location
        if website is not UNSET:
            field_dict["website"] = website
        if logo_id is not UNSET:
            field_dict["logoId"] = logo_id
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if member_id is not UNSET:
            field_dict["memberId"] = member_id
        if member_role is not UNSET:
            field_dict["memberRole"] = member_role
        if paying is not UNSET:
            field_dict["paying"] = paying

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        org_id = d.pop("orgId", UNSET)

        name = d.pop("name", UNSET)

        full_name = d.pop("fullName", UNSET)

        description = d.pop("description", UNSET)

        location = d.pop("location", UNSET)

        website = d.pop("website", UNSET)

        logo_id = d.pop("logoId", UNSET)

        logo_url = d.pop("logoUrl", UNSET)

        member_id = d.pop("memberId", UNSET)

        _member_role = d.pop("memberRole", UNSET)
        member_role: Union[Unset, OrgRole]
        if isinstance(_member_role, Unset):
            member_role = UNSET
        else:
            member_role = OrgRole(_member_role)

        paying = d.pop("paying", UNSET)

        organization_db_dto = cls(
            org_id=org_id,
            name=name,
            full_name=full_name,
            description=description,
            location=location,
            website=website,
            logo_id=logo_id,
            logo_url=logo_url,
            member_id=member_id,
            member_role=member_role,
            paying=paying,
        )

        organization_db_dto.additional_properties = d
        return organization_db_dto

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
