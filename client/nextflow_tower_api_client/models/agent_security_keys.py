from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentSecurityKeys")


@_attrs_define
class AgentSecurityKeys:
    """
    Attributes:
        connection_id (Union[Unset, str]):
        work_dir (Union[Unset, str]):
        shared (Union[Unset, bool]):
        discriminator (Union[Unset, str]):
    """

    connection_id: Union[Unset, str] = UNSET
    work_dir: Union[Unset, str] = UNSET
    shared: Union[Unset, bool] = UNSET
    discriminator: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_id = self.connection_id
        work_dir = self.work_dir
        shared = self.shared
        discriminator = self.discriminator

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if work_dir is not UNSET:
            field_dict["workDir"] = work_dir
        if shared is not UNSET:
            field_dict["shared"] = shared
        if discriminator is not UNSET:
            field_dict["discriminator"] = discriminator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_id = d.pop("connectionId", UNSET)

        work_dir = d.pop("workDir", UNSET)

        shared = d.pop("shared", UNSET)

        discriminator = d.pop("discriminator", UNSET)

        agent_security_keys = cls(
            connection_id=connection_id,
            work_dir=work_dir,
            shared=shared,
            discriminator=discriminator,
        )

        agent_security_keys.additional_properties = d
        return agent_security_keys

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
