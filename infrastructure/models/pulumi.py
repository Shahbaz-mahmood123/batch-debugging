import datetime
from typing import Any, Optional, Dict, List

from pydantic import BaseModel

class Diagnostics(BaseModel):
    warning: str

class Outputs(BaseModel):
    bucket_url: str
    config_files_populate: str
    instanceIP: str
    instanceName: str
    network_id: str
    static_ip_address: str
    subnetwork_id: str
    tags: str
    temp_bucket_url: str

class PreviewResult(BaseModel):
    stdout: str
    stderr: str
    change_summary: Dict[str, int]
    diagnostics: Optional[Dict[str, Diagnostics]]
    outputs: Optional[Outputs]

class UpdateSummary(BaseModel):
    result: str
    version: int
    start_time: str
    end_time: str
    kind: str
    message: str
    environment: Dict[str, str]
    resource_changes: Dict[str, int]
    config: Dict[str, Any]
    Deployment: Any

class DestroyResult(BaseModel):
    stdout: str
    stderr: str
    summary: UpdateSummary
    
class UpResult(BaseModel):
    stdout: str
    stderr: str
    outputs: Dict[str, Any]
    summary: UpdateSummary

class RefreshResult(BaseModel):
    stdout: str
    stderr: str
    summary: UpdateSummary