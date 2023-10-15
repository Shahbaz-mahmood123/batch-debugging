from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.participant_db_dto import ParticipantDbDto


T = TypeVar("T", bound="AddParticipantResponse")


@_attrs_define
class AddParticipantResponse:
    """
    Attributes:
        participant (Union[Unset, ParticipantDbDto]):
    """

    participant: Union[Unset, "ParticipantDbDto"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        participant: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.participant, Unset):
            participant = self.participant.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if participant is not UNSET:
            field_dict["participant"] = participant

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.participant_db_dto import ParticipantDbDto

        d = src_dict.copy()
        _participant = d.pop("participant", UNSET)
        participant: Union[Unset, ParticipantDbDto]
        if isinstance(_participant, Unset):
            participant = UNSET
        else:
            participant = ParticipantDbDto.from_dict(_participant)

        add_participant_response = cls(
            participant=participant,
        )

        add_participant_response.additional_properties = d
        return add_participant_response

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
