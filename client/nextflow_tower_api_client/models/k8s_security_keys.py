from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="K8SSecurityKeys")


@_attrs_define
class K8SSecurityKeys:
    """
    Attributes:
        certificate (Union[Unset, str]):
        private_key (Union[Unset, str]):
        token (Union[Unset, str]):
        discriminator (Union[Unset, str]):
    """

    certificate: Union[Unset, str] = UNSET
    private_key: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    discriminator: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        certificate = self.certificate
        private_key = self.private_key
        token = self.token
        discriminator = self.discriminator

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if certificate is not UNSET:
            field_dict["certificate"] = certificate
        if private_key is not UNSET:
            field_dict["privateKey"] = private_key
        if token is not UNSET:
            field_dict["token"] = token
        if discriminator is not UNSET:
            field_dict["discriminator"] = discriminator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        certificate = d.pop("certificate", UNSET)

        private_key = d.pop("privateKey", UNSET)

        token = d.pop("token", UNSET)

        discriminator = d.pop("discriminator", UNSET)

        k8s_security_keys = cls(
            certificate=certificate,
            private_key=private_key,
            token=token,
            discriminator=discriminator,
        )

        k8s_security_keys.additional_properties = d
        return k8s_security_keys

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
