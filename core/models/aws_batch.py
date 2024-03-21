from typing import List, Optional
from pydantic import BaseModel

class Container(BaseModel):
    exitCode: Optional[int]
    reason: Optional[str]

class ArrayProperties(BaseModel):
    size: Optional[int]
    index: Optional[int]

class NodeProperties(BaseModel):
    isMainNode: bool
    numNodes: Optional[int]
    nodeIndex: Optional[int]

class JobSummary(BaseModel):
    jobArn: str
    jobId: str
    jobName: str
    createdAt: int
    status: str
    statusReason: Optional[str]
    startedAt: Optional[int]
    stoppedAt: Optional[int]
    container: Optional[Container]
    arrayProperties: Optional[ArrayProperties]
    nodeProperties: Optional[NodeProperties]
    jobDefinition: Optional[str]

class JobSummaryListResponse(BaseModel):
    jobSummaryList: List[JobSummary]
    nextToken: Optional[str]
