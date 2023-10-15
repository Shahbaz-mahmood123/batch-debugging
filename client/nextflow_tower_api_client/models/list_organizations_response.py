from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.organization_db_dto import OrganizationDbDto


T = TypeVar("T", bound="ListOrganizationsResponse")


@_attrs_define
class ListOrganizationsResponse:
    """
    Attributes:
        total_size (int):
        organizations (List['OrganizationDbDto']):
    """

    total_size: int
    organizations: List["OrganizationDbDto"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_size = self.total_size
        organizations = []
        for organizations_item_data in self.organizations:
            organizations_item = organizations_item_data.to_dict()

            organizations.append(organizations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalSize": total_size,
                "organizations": organizations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.organization_db_dto import OrganizationDbDto

        d = src_dict.copy()
        total_size = d.pop("totalSize")

        organizations = []
        _organizations = d.pop("organizations")
        for organizations_item_data in _organizations:
            organizations_item = OrganizationDbDto.from_dict(organizations_item_data)

            organizations.append(organizations_item)

        list_organizations_response = cls(
            total_size=total_size,
            organizations=organizations,
        )

        list_organizations_response.additional_properties = d
        return list_organizations_response

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
