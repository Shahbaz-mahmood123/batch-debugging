from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_db_dto import TeamDbDto


T = TypeVar("T", bound="DescribeTeamResponse")


@_attrs_define
class DescribeTeamResponse:
    """
    Attributes:
        team (Union[Unset, TeamDbDto]):
    """

    team: Union[Unset, "TeamDbDto"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if team is not UNSET:
            field_dict["team"] = team

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team_db_dto import TeamDbDto

        d = src_dict.copy()
        _team = d.pop("team", UNSET)
        team: Union[Unset, TeamDbDto]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = TeamDbDto.from_dict(_team)

        describe_team_response = cls(
            team=team,
        )

        describe_team_response.additional_properties = d
        return describe_team_response

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
