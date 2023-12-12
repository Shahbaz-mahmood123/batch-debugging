import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.workflow_status import WorkflowStatus

if TYPE_CHECKING:
    from ..models.wf_manifest import WfManifest
    from ..models.wf_nextflow import WfNextflow
    from ..models.wf_stats import WfStats
    from ..models.workflow_db_dto_params import WorkflowDbDtoParams


T = TypeVar("T", bound="WorkflowDbDto")


@_attrs_define
class WorkflowDbDto:
    """
    Attributes:
        container (str):
        profile (str):
        params (WorkflowDbDtoParams):
        command_line (str):
        complete (datetime.datetime):
        last_updated (datetime.datetime):
        exit_status (int):
        launch_dir (str):
        project_name (str):
        container_engine (str):
        run_name (str):
        project_dir (str):
        start (datetime.datetime):
        deleted (bool):
        error_report (str):
        resume (bool):
        date_created (datetime.datetime):
        nextflow (WfNextflow):
        success (bool):
        error_message (str):
        stats (WfStats):
        revision (str):
        submit (datetime.datetime):
        owner_id (int):
        repository (str):
        id (str):
        session_id (str):
        work_dir (str):
        commit_id (str):
        user_name (str):
        script_id (str):
        script_name (str):
        launch_id (str):
        status (WorkflowStatus):
        config_files (List[str]):
        config_text (str):
        manifest (WfManifest):
        home_dir (str):
        script_file (str):
        duration (int):
    """

    container: str
    profile: str
    params: "WorkflowDbDtoParams"
    command_line: str
    complete: datetime.datetime
    last_updated: datetime.datetime
    exit_status: int
    launch_dir: str
    project_name: str
    container_engine: str
    run_name: str
    project_dir: str
    start: datetime.datetime
    deleted: bool
    error_report: str
    resume: bool
    date_created: datetime.datetime
    nextflow: "WfNextflow"
    success: bool
    error_message: str
    stats: "WfStats"
    revision: str
    submit: datetime.datetime
    owner_id: int
    repository: str
    id: str
    session_id: str
    work_dir: str
    commit_id: str
    user_name: str
    script_id: str
    script_name: str
    launch_id: str
    status: WorkflowStatus
    config_files: List[str]
    config_text: str
    manifest: "WfManifest"
    home_dir: str
    script_file: str
    duration: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        container = self.container
        profile = self.profile
        params = self.params.to_dict()

        command_line = self.command_line
        complete = self.complete.isoformat()

        last_updated = self.last_updated.isoformat()

        exit_status = self.exit_status
        launch_dir = self.launch_dir
        project_name = self.project_name
        container_engine = self.container_engine
        run_name = self.run_name
        project_dir = self.project_dir
        start = self.start.isoformat()

        deleted = self.deleted
        error_report = self.error_report
        resume = self.resume
        date_created = self.date_created.isoformat()

        nextflow = self.nextflow.to_dict()

        success = self.success
        error_message = self.error_message
        stats = self.stats.to_dict()

        revision = self.revision
        submit = self.submit.isoformat()

        owner_id = self.owner_id
        repository = self.repository
        id = self.id
        session_id = self.session_id
        work_dir = self.work_dir
        commit_id = self.commit_id
        user_name = self.user_name
        script_id = self.script_id
        script_name = self.script_name
        launch_id = self.launch_id
        status = self.status.value

        config_files = self.config_files

        config_text = self.config_text
        manifest = self.manifest.to_dict()

        home_dir = self.home_dir
        script_file = self.script_file
        duration = self.duration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "container": container,
                "profile": profile,
                "params": params,
                "commandLine": command_line,
                "complete": complete,
                "lastUpdated": last_updated,
                "exitStatus": exit_status,
                "launchDir": launch_dir,
                "projectName": project_name,
                "containerEngine": container_engine,
                "runName": run_name,
                "projectDir": project_dir,
                "start": start,
                "deleted": deleted,
                "errorReport": error_report,
                "resume": resume,
                "dateCreated": date_created,
                "nextflow": nextflow,
                "success": success,
                "errorMessage": error_message,
                "stats": stats,
                "revision": revision,
                "submit": submit,
                "ownerId": owner_id,
                "repository": repository,
                "id": id,
                "sessionId": session_id,
                "workDir": work_dir,
                "commitId": commit_id,
                "userName": user_name,
                "scriptId": script_id,
                "scriptName": script_name,
                "launchId": launch_id,
                "status": status,
                "configFiles": config_files,
                "configText": config_text,
                "manifest": manifest,
                "homeDir": home_dir,
                "scriptFile": script_file,
                "duration": duration,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wf_manifest import WfManifest
        from ..models.wf_nextflow import WfNextflow
        from ..models.wf_stats import WfStats
        from ..models.workflow_db_dto_params import WorkflowDbDtoParams

        d = src_dict.copy()
        container = d.pop("container")

        profile = d.pop("profile")

        params = WorkflowDbDtoParams.from_dict(d.pop("params"))

        command_line = d.pop("commandLine")

        complete = isoparse(d.pop("complete"))

        last_updated = isoparse(d.pop("lastUpdated"))

        exit_status = d.pop("exitStatus")

        launch_dir = d.pop("launchDir")

        project_name = d.pop("projectName")

        container_engine = d.pop("containerEngine")

        run_name = d.pop("runName")

        project_dir = d.pop("projectDir")

        start = isoparse(d.pop("start"))

        deleted = d.pop("deleted")

        error_report = d.pop("errorReport")

        resume = d.pop("resume")

        date_created = isoparse(d.pop("dateCreated"))

        nextflow = WfNextflow.from_dict(d.pop("nextflow"))

        success = d.pop("success")

        error_message = d.pop("errorMessage")

        stats = WfStats.from_dict(d.pop("stats"))

        revision = d.pop("revision")

        submit = isoparse(d.pop("submit"))

        owner_id = d.pop("ownerId")

        repository = d.pop("repository")

        id = d.pop("id")

        session_id = d.pop("sessionId")

        work_dir = d.pop("workDir")

        commit_id = d.pop("commitId")

        user_name = d.pop("userName")

        script_id = d.pop("scriptId")

        script_name = d.pop("scriptName")

        launch_id = d.pop("launchId")

        status = WorkflowStatus(d.pop("status"))

        config_files = cast(List[str], d.pop("configFiles"))

        config_text = d.pop("configText")

        manifest = WfManifest.from_dict(d.pop("manifest"))

        home_dir = d.pop("homeDir")

        script_file = d.pop("scriptFile")

        duration = d.pop("duration")

        workflow_db_dto = cls(
            container=container,
            profile=profile,
            params=params,
            command_line=command_line,
            complete=complete,
            last_updated=last_updated,
            exit_status=exit_status,
            launch_dir=launch_dir,
            project_name=project_name,
            container_engine=container_engine,
            run_name=run_name,
            project_dir=project_dir,
            start=start,
            deleted=deleted,
            error_report=error_report,
            resume=resume,
            date_created=date_created,
            nextflow=nextflow,
            success=success,
            error_message=error_message,
            stats=stats,
            revision=revision,
            submit=submit,
            owner_id=owner_id,
            repository=repository,
            id=id,
            session_id=session_id,
            work_dir=work_dir,
            commit_id=commit_id,
            user_name=user_name,
            script_id=script_id,
            script_name=script_name,
            launch_id=launch_id,
            status=status,
            config_files=config_files,
            config_text=config_text,
            manifest=manifest,
            home_dir=home_dir,
            script_file=script_file,
            duration=duration,
        )

        workflow_db_dto.additional_properties = d
        return workflow_db_dto

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
