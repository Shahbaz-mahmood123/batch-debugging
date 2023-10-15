from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wf_manifest import WfManifest


T = TypeVar("T", bound="PipelineInfo")


@_attrs_define
class PipelineInfo:
    """
    Attributes:
        project_name (Union[Unset, str]):
        simple_name (Union[Unset, str]):
        repository_url (Union[Unset, str]):
        clone_url (Union[Unset, str]):
        provider (Union[Unset, str]):
        config_files (Union[Unset, List[str]]):
        work_dirs (Union[Unset, List[str]]):
        revisions (Union[Unset, List[str]]):
        profiles (Union[Unset, List[str]]):
        manifest (Union[Unset, WfManifest]):
        warnings (Union[Unset, List[str]]):
    """

    project_name: Union[Unset, str] = UNSET
    simple_name: Union[Unset, str] = UNSET
    repository_url: Union[Unset, str] = UNSET
    clone_url: Union[Unset, str] = UNSET
    provider: Union[Unset, str] = UNSET
    config_files: Union[Unset, List[str]] = UNSET
    work_dirs: Union[Unset, List[str]] = UNSET
    revisions: Union[Unset, List[str]] = UNSET
    profiles: Union[Unset, List[str]] = UNSET
    manifest: Union[Unset, "WfManifest"] = UNSET
    warnings: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_name = self.project_name
        simple_name = self.simple_name
        repository_url = self.repository_url
        clone_url = self.clone_url
        provider = self.provider
        config_files: Union[Unset, List[str]] = UNSET
        if not isinstance(self.config_files, Unset):
            config_files = self.config_files

        work_dirs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.work_dirs, Unset):
            work_dirs = self.work_dirs

        revisions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.revisions, Unset):
            revisions = self.revisions

        profiles: Union[Unset, List[str]] = UNSET
        if not isinstance(self.profiles, Unset):
            profiles = self.profiles

        manifest: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.manifest, Unset):
            manifest = self.manifest.to_dict()

        warnings: Union[Unset, List[str]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_name is not UNSET:
            field_dict["projectName"] = project_name
        if simple_name is not UNSET:
            field_dict["simpleName"] = simple_name
        if repository_url is not UNSET:
            field_dict["repositoryUrl"] = repository_url
        if clone_url is not UNSET:
            field_dict["cloneUrl"] = clone_url
        if provider is not UNSET:
            field_dict["provider"] = provider
        if config_files is not UNSET:
            field_dict["configFiles"] = config_files
        if work_dirs is not UNSET:
            field_dict["workDirs"] = work_dirs
        if revisions is not UNSET:
            field_dict["revisions"] = revisions
        if profiles is not UNSET:
            field_dict["profiles"] = profiles
        if manifest is not UNSET:
            field_dict["manifest"] = manifest
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wf_manifest import WfManifest

        d = src_dict.copy()
        project_name = d.pop("projectName", UNSET)

        simple_name = d.pop("simpleName", UNSET)

        repository_url = d.pop("repositoryUrl", UNSET)

        clone_url = d.pop("cloneUrl", UNSET)

        provider = d.pop("provider", UNSET)

        config_files = cast(List[str], d.pop("configFiles", UNSET))

        work_dirs = cast(List[str], d.pop("workDirs", UNSET))

        revisions = cast(List[str], d.pop("revisions", UNSET))

        profiles = cast(List[str], d.pop("profiles", UNSET))

        _manifest = d.pop("manifest", UNSET)
        manifest: Union[Unset, WfManifest]
        if isinstance(_manifest, Unset):
            manifest = UNSET
        else:
            manifest = WfManifest.from_dict(_manifest)

        warnings = cast(List[str], d.pop("warnings", UNSET))

        pipeline_info = cls(
            project_name=project_name,
            simple_name=simple_name,
            repository_url=repository_url,
            clone_url=clone_url,
            provider=provider,
            config_files=config_files,
            work_dirs=work_dirs,
            revisions=revisions,
            profiles=profiles,
            manifest=manifest,
            warnings=warnings,
        )

        pipeline_info.additional_properties = d
        return pipeline_info

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
