from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.participant_db_dto import ParticipantDbDto


T = TypeVar("T", bound="ListParticipantsResponse")


@_attrs_define
class ListParticipantsResponse:
    """
    Attributes:
        total_size (int):
        participants (List['ParticipantDbDto']):
    """

    total_size: int
    participants: List["ParticipantDbDto"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_size = self.total_size
        participants = []
        for participants_item_data in self.participants:
            participants_item = participants_item_data.to_dict()

            participants.append(participants_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalSize": total_size,
                "participants": participants,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.participant_db_dto import ParticipantDbDto

        d = src_dict.copy()
        total_size = d.pop("totalSize")

        participants = []
        _participants = d.pop("participants")
        for participants_item_data in _participants:
            participants_item = ParticipantDbDto.from_dict(participants_item_data)

            participants.append(participants_item)

        list_participants_response = cls(
            total_size=total_size,
            participants=participants,
        )

        list_participants_response.additional_properties = d
        return list_participants_response

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
