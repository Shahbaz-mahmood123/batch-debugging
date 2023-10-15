from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access_token import AccessToken


T = TypeVar("T", bound="CreateAccessTokenResponse")


@_attrs_define
class CreateAccessTokenResponse:
    """
    Attributes:
        access_key (Union[Unset, str]):
        token (Union[Unset, AccessToken]):
    """

    access_key: Union[Unset, str] = UNSET
    token: Union[Unset, "AccessToken"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_key = self.access_key
        token: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.token, Unset):
            token = self.token.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_key is not UNSET:
            field_dict["accessKey"] = access_key
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.access_token import AccessToken

        d = src_dict.copy()
        access_key = d.pop("accessKey", UNSET)

        _token = d.pop("token", UNSET)
        token: Union[Unset, AccessToken]
        if isinstance(_token, Unset):
            token = UNSET
        else:
            token = AccessToken.from_dict(_token)

        create_access_token_response = cls(
            access_key=access_key,
            token=token,
        )

        create_access_token_response.additional_properties = d
        return create_access_token_response

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
