from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.team_db_dto import TeamDbDto


T = TypeVar("T", bound="ListTeamResponse")


@_attrs_define
class ListTeamResponse:
    """
    Attributes:
        total_size (int):
        teams (List['TeamDbDto']):
    """

    total_size: int
    teams: List["TeamDbDto"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_size = self.total_size
        teams = []
        for teams_item_data in self.teams:
            teams_item = teams_item_data.to_dict()

            teams.append(teams_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalSize": total_size,
                "teams": teams,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team_db_dto import TeamDbDto

        d = src_dict.copy()
        total_size = d.pop("totalSize")

        teams = []
        _teams = d.pop("teams")
        for teams_item_data in _teams:
            teams_item = TeamDbDto.from_dict(teams_item_data)

            teams.append(teams_item)

        list_team_response = cls(
            total_size=total_size,
            teams=teams,
        )

        list_team_response.additional_properties = d
        return list_team_response

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
