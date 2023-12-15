from core.debug_aws_batch import DebugAWSBatch
from core.client import AuthenticatedPlatformClient
from core.gcp_batch import GCPBatch

from core.compute_envs import SeqeraComputeEnvsWrapper
from google.cloud import batch_v1

authenticated_client = AuthenticatedPlatformClient()


seqera = SeqeraComputeEnvsWrapper()

test = seqera.get_compute_env("5tQSF2ahyA19GNS5b8rzNS")
recommendations = seqera.optimize_compute_env(test)
#print(test) 
print(recommendations)


# gcp_batch = GCPBatch()

debug_aws_batch = DebugAWSBatch()

#ShahbazCompute-5tQSF2ahyA19GNS5b8rzNS-work

# gcp_job = gcp_batch.create_test_job("batch-debug")
# print(gcp_job)

#AWS_REGION
##Fetch  wuth different status
# jobs = debug_aws_batch.get_running_jobs("ShahbazCompute-5tQSF2ahyA19GNS5b8rzNS-work")
# print("running jobs")
# print(jobs)
# jobs = debug_aws_batch.get_succeeded_jobs("ShahbazCompute-5tQSF2ahyA19GNS5b8rzNS-work")
# print("succeeded jobs")
# print(jobs)
# jobs = debug_aws_batch.get_failed_jobs("ShahbazCompute-5tQSF2ahyA19GNS5b8rzNS-work")
# print("failed jobs")
# print(jobs)

##Fetch ECS Cluster
# ecs_cluster = debug_aws_batch.get_ecs_cluster(compute_env_id="ShahbazCompute-4EIsD1KeFL46MRnmovBMMk-work")
# print(ecs_cluster)

##Get autoscaling group 
# autoscaling_group = debug_aws_batch.get_autoscaling_group("ShahbazCompute-5tQSF2ahyA19GNS5b8rzNS-work")
#print(autoscaling_group)

##Get autoscaling group activity
# autoscaling_activity = debug_aws_batch.get_scaling_activities(autoscaling_group=autoscaling_group)
# print(autoscaling_activity)

##Get compute env status:
# compute_env_status = debug_aws_batch.get_compute_env_status("ShahbazCompute-40pV5hjSVBWMu87Gtd7Pt2-head")
# print(compute_env_status)

## fetch job queue status
# job_queue = debug_aws_batch.get_job_queue_status("ShahbazCompute-4EIsD1KeFL46MRnmovBMMk-work")
# print(job_queue)


##Fetch compute env list
#id_list = debug_aws_batch.get_tower_compute_envs_id_list('251085962711837', "AVAILABLE")
# #print(id_list)
# #print(id_list[1])

##this fetches the launch template object returned by boto3 based of a given CE.
#launch_template_id = debug_aws_batch.get_aws_batch_compute_env_launch_template_id("ShahbazCompute-4EIsD1KeFL46MRnmovBMMk-head")

# print(launch_template_id)
## returns the user data of the launch template
#test = debug_aws_batch.get_user_data_from_launch_template(launch_template_id)
#print(test)

##Get launch template:
# launch_template_userdata = debug_aws_batch.extract_and_decode_user_data(test)
# print(launch_template_userdata)


seqera_compute_env = SeqeraComputeEnvsWrapper(client=authenticated_client)

##
# Fetch seqera compute env
# \\compute_env = seqera_compute_env.get_compute_env(compute_env_id='2zHxdiwhxTzkM1SUjNkThy')
# \\print(compute_env)