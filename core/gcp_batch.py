import os
import uuid

from google.cloud import batch_v1

class GCPBatchInterface():
    
    def create_test_job(self, job_name: str) -> batch_v1.Job:
        pass   
    
class GCPBatch(GCPBatchInterface):
    
    def __init__(self):
        """
        Initializes the gcp_batch class.

        Args:
            batch_client: An instance of the GCP Batch client.
        """
        self.project_id = os.getenv("GCP_PROJECT_ID")
        self.region = os.getenv("GCP_REGION") 
        self.batch_client = batch_v1.BatchServiceClient()
    
    #https://cloud.google.com/batch/docs/create-run-basic-job#create-basic-container-job
    def create_test_job(self, job_name: str) -> batch_v1.Job:
        runnable = batch_v1.Runnable()
        runnable.container = batch_v1.Runnable.Container()
        runnable.container.image_uri = "gcr.io/google-containers/busybox"
        runnable.container.entrypoint = "/bin/sh"
        runnable.container.commands = [
            "-c",
            "echo Hello world! This is task ${BATCH_TASK_INDEX}. This job has a total of ${BATCH_TASK_COUNT} tasks.",
        ]         
        # Jobs can be divided into tasks. In this case, we have only one task.
        task = batch_v1.TaskSpec()
        task.runnables = [runnable]

        # We can specify what resources are requested by each task.
        resources = batch_v1.ComputeResource()
        resources.cpu_milli = 2000  # in milliseconds per cpu-second. This means the task requires 2 whole CPUs.
        resources.memory_mib = 16  # in MiB
        task.compute_resource = resources

        task.max_retry_count = 2
        task.max_run_duration = "3600s"

        # Tasks are grouped inside a job using TaskGroups.
        # Currently, it's possible to have only one task group.
        group = batch_v1.TaskGroup()
        group.task_count = 4
        group.task_spec = task

        # Policies are used to define on what kind of virtual machines the tasks will run on.
        # In this case, we tell the system to use "e2-standard-4" machine type.
        # Read more about machine types here: https://cloud.google.com/compute/docs/machine-types
        policy = batch_v1.AllocationPolicy.InstancePolicy()
        policy.machine_type = "e2-standard-4"
        instances = batch_v1.AllocationPolicy.InstancePolicyOrTemplate()
        instances.policy = policy
        allocation_policy = batch_v1.AllocationPolicy()
        allocation_policy.instances = [instances]

        job = batch_v1.Job()
        job.task_groups = [group]
        job.allocation_policy = allocation_policy
        job.labels = {"env": "testing", "type": "container"}
        # We use Cloud Logging as it's an out of the box available option
        job.logs_policy = batch_v1.LogsPolicy()
        job.logs_policy.destination = batch_v1.LogsPolicy.Destination.CLOUD_LOGGING

        create_request = batch_v1.CreateJobRequest()
        create_request.job = job
        create_request.job_id = job_name+"-"+str(uuid.uuid4())
        # The job's parent is the region in which the job will run
        create_request.parent = f"projects/{self.project_id}/locations/{self.region}"

        return self.batch_client.create_job(create_request)
