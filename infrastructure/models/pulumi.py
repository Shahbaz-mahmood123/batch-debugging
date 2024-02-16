from typing import Optional, Dict
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