from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AwsSecurityKeys")


@_attrs_define
class AwsSecurityKeys:
    """
    Attributes:
        access_key (Union[Unset, str]):
        secret_key (Union[Unset, str]):
        assume_role_arn (Union[Unset, str]):
        discriminator (Union[Unset, str]):
    """

    access_key: Union[Unset, str] = UNSET
    secret_key: Union[Unset, str] = UNSET
    assume_role_arn: Union[Unset, str] = UNSET
    discriminator: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_key = self.access_key
        secret_key = self.secret_key
        assume_role_arn = self.assume_role_arn
        discriminator = self.discriminator

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_key is not UNSET:
            field_dict["accessKey"] = access_key
        if secret_key is not UNSET:
            field_dict["secretKey"] = secret_key
        if assume_role_arn is not UNSET:
            field_dict["assumeRoleArn"] = assume_role_arn
        if discriminator is not UNSET:
            field_dict["discriminator"] = discriminator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_key = d.pop("accessKey", UNSET)

        secret_key = d.pop("secretKey", UNSET)

        assume_role_arn = d.pop("assumeRoleArn", UNSET)

        discriminator = d.pop("discriminator", UNSET)

        aws_security_keys = cls(
            access_key=access_key,
            secret_key=secret_key,
            assume_role_arn=assume_role_arn,
            discriminator=discriminator,
        )

        aws_security_keys.additional_properties = d
        return aws_security_keys

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
