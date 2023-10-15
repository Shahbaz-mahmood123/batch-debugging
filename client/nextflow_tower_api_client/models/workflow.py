import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.workflow_status import WorkflowStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wf_manifest import WfManifest
    from ..models.wf_nextflow import WfNextflow
    from ..models.wf_stats import WfStats
    from ..models.workflow_params import WorkflowParams


T = TypeVar("T", bound="Workflow")


@_attrs_define
class Workflow:
    """
    Attributes:
        submit (datetime.datetime):
        run_name (str):
        session_id (str):
        work_dir (str):
        user_name (str):
        command_line (str):
        project_name (str):
        status (Union[Unset, WorkflowStatus]):
        owner_id (Union[Unset, int]):
        repository (Union[Unset, str]):
        id (Union[Unset, str]):
        start (Union[Unset, datetime.datetime]):
        complete (Union[Unset, datetime.datetime]):
        date_created (Union[Unset, None, datetime.datetime]):
        last_updated (Union[Unset, None, datetime.datetime]):
        profile (Union[Unset, str]):
        commit_id (Union[Unset, str]):
        script_id (Union[Unset, str]):
        revision (Union[Unset, str]):
        script_name (Union[Unset, str]):
        launch_id (Union[Unset, str]):
        config_files (Union[Unset, List[str]]):
        params (Union[Unset, WorkflowParams]):
        config_text (Union[Unset, str]):
        manifest (Union[Unset, WfManifest]):
        nextflow (Union[Unset, WfNextflow]):
        stats (Union[Unset, WfStats]):
        error_message (Union[Unset, str]):
        error_report (Union[Unset, str]):
        deleted (Union[Unset, bool]):
        project_dir (Union[Unset, str]):
        home_dir (Union[Unset, str]):
        container (Union[Unset, str]):
        container_engine (Union[Unset, str]):
        script_file (Union[Unset, str]):
        launch_dir (Union[Unset, str]):
        duration (Union[Unset, int]):
        exit_status (Union[Unset, int]):
        resume (Union[Unset, bool]):
        success (Union[Unset, bool]):
        log_file (Union[Unset, str]):
        out_file (Union[Unset, str]):
        operation_id (Union[Unset, str]):
    """

    submit: datetime.datetime
    run_name: str
    session_id: str
    work_dir: str
    user_name: str
    command_line: str
    project_name: str
    status: Union[Unset, WorkflowStatus] = UNSET
    owner_id: Union[Unset, int] = UNSET
    repository: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    start: Union[Unset, datetime.datetime] = UNSET
    complete: Union[Unset, datetime.datetime] = UNSET
    date_created: Union[Unset, None, datetime.datetime] = UNSET
    last_updated: Union[Unset, None, datetime.datetime] = UNSET
    profile: Union[Unset, str] = UNSET
    commit_id: Union[Unset, str] = UNSET
    script_id: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    script_name: Union[Unset, str] = UNSET
    launch_id: Union[Unset, str] = UNSET
    config_files: Union[Unset, List[str]] = UNSET
    params: Union[Unset, "WorkflowParams"] = UNSET
    config_text: Union[Unset, str] = UNSET
    manifest: Union[Unset, "WfManifest"] = UNSET
    nextflow: Union[Unset, "WfNextflow"] = UNSET
    stats: Union[Unset, "WfStats"] = UNSET
    error_message: Union[Unset, str] = UNSET
    error_report: Union[Unset, str] = UNSET
    deleted: Union[Unset, bool] = UNSET
    project_dir: Union[Unset, str] = UNSET
    home_dir: Union[Unset, str] = UNSET
    container: Union[Unset, str] = UNSET
    container_engine: Union[Unset, str] = UNSET
    script_file: Union[Unset, str] = UNSET
    launch_dir: Union[Unset, str] = UNSET
    duration: Union[Unset, int] = UNSET
    exit_status: Union[Unset, int] = UNSET
    resume: Union[Unset, bool] = UNSET
    success: Union[Unset, bool] = UNSET
    log_file: Union[Unset, str] = UNSET
    out_file: Union[Unset, str] = UNSET
    operation_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        submit = self.submit.isoformat()

        run_name = self.run_name
        session_id = self.session_id
        work_dir = self.work_dir
        user_name = self.user_name
        command_line = self.command_line
        project_name = self.project_name
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        owner_id = self.owner_id
        repository = self.repository
        id = self.id
        start: Union[Unset, str] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        complete: Union[Unset, str] = UNSET
        if not isinstance(self.complete, Unset):
            complete = self.complete.isoformat()

        date_created: Union[Unset, None, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat() if self.date_created else None

        last_updated: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat() if self.last_updated else None

        profile = self.profile
        commit_id = self.commit_id
        script_id = self.script_id
        revision = self.revision
        script_name = self.script_name
        launch_id = self.launch_id
        config_files: Union[Unset, List[str]] = UNSET
        if not isinstance(self.config_files, Unset):
            config_files = self.config_files

        params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        config_text = self.config_text
        manifest: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.manifest, Unset):
            manifest = self.manifest.to_dict()

        nextflow: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.nextflow, Unset):
            nextflow = self.nextflow.to_dict()

        stats: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        error_message = self.error_message
        error_report = self.error_report
        deleted = self.deleted
        project_dir = self.project_dir
        home_dir = self.home_dir
        container = self.container
        container_engine = self.container_engine
        script_file = self.script_file
        launch_dir = self.launch_dir
        duration = self.duration
        exit_status = self.exit_status
        resume = self.resume
        success = self.success
        log_file = self.log_file
        out_file = self.out_file
        operation_id = self.operation_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "submit": submit,
                "runName": run_name,
                "sessionId": session_id,
                "workDir": work_dir,
                "userName": user_name,
                "commandLine": command_line,
                "projectName": project_name,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if repository is not UNSET:
            field_dict["repository"] = repository
        if id is not UNSET:
            field_dict["id"] = id
        if start is not UNSET:
            field_dict["start"] = start
        if complete is not UNSET:
            field_dict["complete"] = complete
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if profile is not UNSET:
            field_dict["profile"] = profile
        if commit_id is not UNSET:
            field_dict["commitId"] = commit_id
        if script_id is not UNSET:
            field_dict["scriptId"] = script_id
        if revision is not UNSET:
            field_dict["revision"] = revision
        if script_name is not UNSET:
            field_dict["scriptName"] = script_name
        if launch_id is not UNSET:
            field_dict["launchId"] = launch_id
        if config_files is not UNSET:
            field_dict["configFiles"] = config_files
        if params is not UNSET:
            field_dict["params"] = params
        if config_text is not UNSET:
            field_dict["configText"] = config_text
        if manifest is not UNSET:
            field_dict["manifest"] = manifest
        if nextflow is not UNSET:
            field_dict["nextflow"] = nextflow
        if stats is not UNSET:
            field_dict["stats"] = stats
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if error_report is not UNSET:
            field_dict["errorReport"] = error_report
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if project_dir is not UNSET:
            field_dict["projectDir"] = project_dir
        if home_dir is not UNSET:
            field_dict["homeDir"] = home_dir
        if container is not UNSET:
            field_dict["container"] = container
        if container_engine is not UNSET:
            field_dict["containerEngine"] = container_engine
        if script_file is not UNSET:
            field_dict["scriptFile"] = script_file
        if launch_dir is not UNSET:
            field_dict["launchDir"] = launch_dir
        if duration is not UNSET:
            field_dict["duration"] = duration
        if exit_status is not UNSET:
            field_dict["exitStatus"] = exit_status
        if resume is not UNSET:
            field_dict["resume"] = resume
        if success is not UNSET:
            field_dict["success"] = success
        if log_file is not UNSET:
            field_dict["logFile"] = log_file
        if out_file is not UNSET:
            field_dict["outFile"] = out_file
        if operation_id is not UNSET:
            field_dict["operationId"] = operation_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wf_manifest import WfManifest
        from ..models.wf_nextflow import WfNextflow
        from ..models.wf_stats import WfStats
        from ..models.workflow_params import WorkflowParams

        d = src_dict.copy()
        submit = isoparse(d.pop("submit"))

        run_name = d.pop("runName")

        session_id = d.pop("sessionId")

        work_dir = d.pop("workDir")

        user_name = d.pop("userName")

        command_line = d.pop("commandLine")

        project_name = d.pop("projectName")

        _status = d.pop("status", UNSET)
        status: Union[Unset, WorkflowStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WorkflowStatus(_status)

        owner_id = d.pop("ownerId", UNSET)

        repository = d.pop("repository", UNSET)

        id = d.pop("id", UNSET)

        _start = d.pop("start", UNSET)
        start: Union[Unset, datetime.datetime]
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = isoparse(_start)

        _complete = d.pop("complete", UNSET)
        complete: Union[Unset, datetime.datetime]
        if isinstance(_complete, Unset):
            complete = UNSET
        else:
            complete = isoparse(_complete)

        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, None, datetime.datetime]
        if _date_created is None:
            date_created = None
        elif isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, None, datetime.datetime]
        if _last_updated is None:
            last_updated = None
        elif isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        profile = d.pop("profile", UNSET)

        commit_id = d.pop("commitId", UNSET)

        script_id = d.pop("scriptId", UNSET)

        revision = d.pop("revision", UNSET)

        script_name = d.pop("scriptName", UNSET)

        launch_id = d.pop("launchId", UNSET)

        config_files = cast(List[str], d.pop("configFiles", UNSET))

        _params = d.pop("params", UNSET)
        params: Union[Unset, WorkflowParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = WorkflowParams.from_dict(_params)

        config_text = d.pop("configText", UNSET)

        _manifest = d.pop("manifest", UNSET)
        manifest: Union[Unset, WfManifest]
        if isinstance(_manifest, Unset):
            manifest = UNSET
        else:
            manifest = WfManifest.from_dict(_manifest)

        _nextflow = d.pop("nextflow", UNSET)
        nextflow: Union[Unset, WfNextflow]
        if isinstance(_nextflow, Unset):
            nextflow = UNSET
        else:
            nextflow = WfNextflow.from_dict(_nextflow)

        _stats = d.pop("stats", UNSET)
        stats: Union[Unset, WfStats]
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = WfStats.from_dict(_stats)

        error_message = d.pop("errorMessage", UNSET)

        error_report = d.pop("errorReport", UNSET)

        deleted = d.pop("deleted", UNSET)

        project_dir = d.pop("projectDir", UNSET)

        home_dir = d.pop("homeDir", UNSET)

        container = d.pop("container", UNSET)

        container_engine = d.pop("containerEngine", UNSET)

        script_file = d.pop("scriptFile", UNSET)

        launch_dir = d.pop("launchDir", UNSET)

        duration = d.pop("duration", UNSET)

        exit_status = d.pop("exitStatus", UNSET)

        resume = d.pop("resume", UNSET)

        success = d.pop("success", UNSET)

        log_file = d.pop("logFile", UNSET)

        out_file = d.pop("outFile", UNSET)

        operation_id = d.pop("operationId", UNSET)

        workflow = cls(
            submit=submit,
            run_name=run_name,
            session_id=session_id,
            work_dir=work_dir,
            user_name=user_name,
            command_line=command_line,
            project_name=project_name,
            status=status,
            owner_id=owner_id,
            repository=repository,
            id=id,
            start=start,
            complete=complete,
            date_created=date_created,
            last_updated=last_updated,
            profile=profile,
            commit_id=commit_id,
            script_id=script_id,
            revision=revision,
            script_name=script_name,
            launch_id=launch_id,
            config_files=config_files,
            params=params,
            config_text=config_text,
            manifest=manifest,
            nextflow=nextflow,
            stats=stats,
            error_message=error_message,
            error_report=error_report,
            deleted=deleted,
            project_dir=project_dir,
            home_dir=home_dir,
            container=container,
            container_engine=container_engine,
            script_file=script_file,
            launch_dir=launch_dir,
            duration=duration,
            exit_status=exit_status,
            resume=resume,
            success=success,
            log_file=log_file,
            out_file=out_file,
            operation_id=operation_id,
        )

        workflow.additional_properties = d
        return workflow

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
