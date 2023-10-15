from typing import Optional


class ComputeEnvInterface:
    def list_compute_envs(self, status: Optional[str] = None, workspace_id: Optional[int] = None):
        pass
