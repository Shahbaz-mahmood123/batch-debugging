from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AbstractGridConfig")


@_attrs_define
class AbstractGridConfig:
    """
    Attributes:
        work_dir (Union[Unset, str]):
        launch_dir (Union[Unset, str]):
        user_name (Union[Unset, str]):
        host_name (Union[Unset, str]):
        port (Union[Unset, int]):
        head_queue (Union[Unset, str]):
        compute_queue (Union[Unset, str]):
        max_queue_size (Union[Unset, int]):
        head_job_options (Union[Unset, str]):
        propagate_head_job_options (Union[Unset, bool]):
        pre_run_script (Union[Unset, str]):
        post_run_script (Union[Unset, str]):
    """

    work_dir: Union[Unset, str] = UNSET
    launch_dir: Union[Unset, str] = UNSET
    user_name: Union[Unset, str] = UNSET
    host_name: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    head_queue: Union[Unset, str] = UNSET
    compute_queue: Union[Unset, str] = UNSET
    max_queue_size: Union[Unset, int] = UNSET
    head_job_options: Union[Unset, str] = UNSET
    propagate_head_job_options: Union[Unset, bool] = UNSET
    pre_run_script: Union[Unset, str] = UNSET
    post_run_script: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        work_dir = self.work_dir
        launch_dir = self.launch_dir
        user_name = self.user_name
        host_name = self.host_name
        port = self.port
        head_queue = self.head_queue
        compute_queue = self.compute_queue
        max_queue_size = self.max_queue_size
        head_job_options = self.head_job_options
        propagate_head_job_options = self.propagate_head_job_options
        pre_run_script = self.pre_run_script
        post_run_script = self.post_run_script

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if work_dir is not UNSET:
            field_dict["workDir"] = work_dir
        if launch_dir is not UNSET:
            field_dict["launchDir"] = launch_dir
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if port is not UNSET:
            field_dict["port"] = port
        if head_queue is not UNSET:
            field_dict["headQueue"] = head_queue
        if compute_queue is not UNSET:
            field_dict["computeQueue"] = compute_queue
        if max_queue_size is not UNSET:
            field_dict["maxQueueSize"] = max_queue_size
        if head_job_options is not UNSET:
            field_dict["headJobOptions"] = head_job_options
        if propagate_head_job_options is not UNSET:
            field_dict["propagateHeadJobOptions"] = propagate_head_job_options
        if pre_run_script is not UNSET:
            field_dict["preRunScript"] = pre_run_script
        if post_run_script is not UNSET:
            field_dict["postRunScript"] = post_run_script

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        work_dir = d.pop("workDir", UNSET)

        launch_dir = d.pop("launchDir", UNSET)

        user_name = d.pop("userName", UNSET)

        host_name = d.pop("hostName", UNSET)

        port = d.pop("port", UNSET)

        head_queue = d.pop("headQueue", UNSET)

        compute_queue = d.pop("computeQueue", UNSET)

        max_queue_size = d.pop("maxQueueSize", UNSET)

        head_job_options = d.pop("headJobOptions", UNSET)

        propagate_head_job_options = d.pop("propagateHeadJobOptions", UNSET)

        pre_run_script = d.pop("preRunScript", UNSET)

        post_run_script = d.pop("postRunScript", UNSET)

        abstract_grid_config = cls(
            work_dir=work_dir,
            launch_dir=launch_dir,
            user_name=user_name,
            host_name=host_name,
            port=port,
            head_queue=head_queue,
            compute_queue=compute_queue,
            max_queue_size=max_queue_size,
            head_job_options=head_job_options,
            propagate_head_job_options=propagate_head_job_options,
            pre_run_script=pre_run_script,
            post_run_script=post_run_script,
        )

        abstract_grid_config.additional_properties = d
        return abstract_grid_config

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
