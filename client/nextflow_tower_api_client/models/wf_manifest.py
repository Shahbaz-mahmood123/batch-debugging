from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfManifest")


@_attrs_define
class WfManifest:
    """
    Attributes:
        nextflow_version (Union[Unset, str]):
        default_branch (Union[Unset, str]):
        version (Union[Unset, str]):
        home_page (Union[Unset, str]):
        gitmodules (Union[Unset, str]):
        description (Union[Unset, str]):
        name (Union[Unset, str]):
        main_script (Union[Unset, str]):
        author (Union[Unset, str]):
    """

    nextflow_version: Union[Unset, str] = UNSET
    default_branch: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    home_page: Union[Unset, str] = UNSET
    gitmodules: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    main_script: Union[Unset, str] = UNSET
    author: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nextflow_version = self.nextflow_version
        default_branch = self.default_branch
        version = self.version
        home_page = self.home_page
        gitmodules = self.gitmodules
        description = self.description
        name = self.name
        main_script = self.main_script
        author = self.author

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nextflow_version is not UNSET:
            field_dict["nextflowVersion"] = nextflow_version
        if default_branch is not UNSET:
            field_dict["defaultBranch"] = default_branch
        if version is not UNSET:
            field_dict["version"] = version
        if home_page is not UNSET:
            field_dict["homePage"] = home_page
        if gitmodules is not UNSET:
            field_dict["gitmodules"] = gitmodules
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if main_script is not UNSET:
            field_dict["mainScript"] = main_script
        if author is not UNSET:
            field_dict["author"] = author

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        nextflow_version = d.pop("nextflowVersion", UNSET)

        default_branch = d.pop("defaultBranch", UNSET)

        version = d.pop("version", UNSET)

        home_page = d.pop("homePage", UNSET)

        gitmodules = d.pop("gitmodules", UNSET)

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        main_script = d.pop("mainScript", UNSET)

        author = d.pop("author", UNSET)

        wf_manifest = cls(
            nextflow_version=nextflow_version,
            default_branch=default_branch,
            version=version,
            home_page=home_page,
            gitmodules=gitmodules,
            description=description,
            name=name,
            main_script=main_script,
            author=author,
        )

        wf_manifest.additional_properties = d
        return wf_manifest

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
