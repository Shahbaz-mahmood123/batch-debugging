from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_db_dto import OrganizationDbDto


T = TypeVar("T", bound="CreateOrganizationResponse")


@_attrs_define
class CreateOrganizationResponse:
    """
    Attributes:
        organization (Union[Unset, OrganizationDbDto]):
    """

    organization: Union[Unset, "OrganizationDbDto"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        organization: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organization is not UNSET:
            field_dict["organization"] = organization

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.organization_db_dto import OrganizationDbDto

        d = src_dict.copy()
        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, OrganizationDbDto]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = OrganizationDbDto.from_dict(_organization)

        create_organization_response = cls(
            organization=organization,
        )

        create_organization_response.additional_properties = d
        return create_organization_response

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
