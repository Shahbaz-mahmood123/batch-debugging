from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateOrganizationRequest")


@_attrs_define
class UpdateOrganizationRequest:
    """
    Attributes:
        location (Union[Unset, str]):
        description (Union[Unset, str]):
        logo_id (Union[Unset, str]):
        full_name (Union[Unset, str]):
        paying (Union[Unset, None, bool]):
        website (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    location: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    logo_id: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    paying: Union[Unset, None, bool] = UNSET
    website: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        location = self.location
        description = self.description
        logo_id = self.logo_id
        full_name = self.full_name
        paying = self.paying
        website = self.website
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location is not UNSET:
            field_dict["location"] = location
        if description is not UNSET:
            field_dict["description"] = description
        if logo_id is not UNSET:
            field_dict["logoId"] = logo_id
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if paying is not UNSET:
            field_dict["paying"] = paying
        if website is not UNSET:
            field_dict["website"] = website
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        location = d.pop("location", UNSET)

        description = d.pop("description", UNSET)

        logo_id = d.pop("logoId", UNSET)

        full_name = d.pop("fullName", UNSET)

        paying = d.pop("paying", UNSET)

        website = d.pop("website", UNSET)

        name = d.pop("name", UNSET)

        update_organization_request = cls(
            location=location,
            description=description,
            logo_id=logo_id,
            full_name=full_name,
            paying=paying,
            website=website,
            name=name,
        )

        update_organization_request.additional_properties = d
        return update_organization_request

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
