from client.nextflow_tower_api_client.client import AuthenticatedClient, Client
from core.debug_aws_batch import DebugAWSBatch
from core.client import AuthenticatedPlatformClient




authenticated_client = AuthenticatedPlatformClient()

debug_aws_batch = DebugAWSBatch(authenticated_client)


#Get autoscaling group 
autoscaling_group = debug_aws_batch.get_autoscaling_group("ShahbazCompute-2zHxdiwhxTzkM1SUjNkThy-work")
print(autoscaling_group)

##Get autoscaling group activity
# autoscaling_activity = debug_aws_batch.get_scaling_activities(autoscaling_group=autoscaling_group)
# print(autoscaling_activity)

##Get compute env status:
# compute_env_status = debug_aws_batch.get_compute_env_status("ShahbazCompute-40pV5hjSVBWMu87Gtd7Pt2-head")
# print(compute_env_status)

## fetch job queue status
# job_queue = debug_aws_batch.get_job_queue_status("ShahbazCompute-40pV5hjSVBWMu87Gtd7Pt2-head")
# print(job_queue)



##Fetch compute env list
#id_list = debug_aws_batch.get_tower_compute_envs_id_list('251085962711837', "AVAILABLE")
# #print(id_list)
# #print(id_list[1])

##this fetches the launch template object returned by boto3 based of a given CE.
# launch_template_id = debug_aws_batch.get_aws_batch_compute_env_launch_template_id("ShahbazCompute-2zHxdiwhxTzkM1SUjNkThy-work")

# print(launch_template_id)
## returns the user data of the launch template
# test = debug_aws_batch.get_user_data_from_launch_template(launch_template_id)
# print(test)