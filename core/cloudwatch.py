from core.models.cloudwatch import LogGroup, LogGroupResponse, LogStream, LogStreamResponse
import pprint

class CloudWatchInterface():
    def get_log_groups(self) -> LogGroupResponse:  
        pass
    
    def get_log_streams(self, log_group: LogGroup=None ,log_group_name=None) -> LogStreamResponse:
        pass
    
class CloudWatch(CloudWatchInterface):
    def __init__(self, cloudwatch_client):
        self.cloudwatch_client = cloudwatch_client

    def get_log_groups(self) -> LogGroupResponse:  
        try:
            log_groups = self.cloudwatch_client.describe_log_groups()
        except Exception as e:
            return f"An error occured fetching the log groups: {e}"
        finally:
            log_group_response = LogGroupResponse(logGroups=log_groups['logGroups'])
            return log_group_response 
        
    def get_log_streams(self, log_group: LogGroup=None ,log_group_name=None) -> LogStreamResponse:

        if log_group_name is None:
            log_group_name = log_group.logGroupName
        elif log_group is None and log_group_name is "":
            return f"Please pass either a log group object or the log group name"
        
        if "tower/forge" in log_group_name:
            try: 
                log_stream = self.cloudwatch_client.describe_log_streams(logGroupIdentifier=log_group_name, orderBy="LastEventTime")
            except Exception as e:
                return f"An error occured fetching the logstream {e}"   
            finally:
                log_stream_response = LogStreamResponse(logStreams=log_stream['logStreams'])
                return log_stream_response
        else: 
            return f"Please pass a valid log group object"   
        
    def get_logs(self, log_stream: LogStream, log_group_name: LogGroup):
        pass
   
        
 
                        
                