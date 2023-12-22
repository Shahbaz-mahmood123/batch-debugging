from core.models.cloudwatch import LogGroup, LogGroupResponse, LogStream, LogStreamResponse, LogEvent, LogEventsResponse

class CloudWatchInterface():
    def get_log_groups(self) -> LogGroupResponse:  
        pass
    
    def get_log_streams(self, log_group: LogGroup=None ,log_group_name=None) -> LogStreamResponse:
        pass
    
    def get_log_events(self, log_stream_name: str, log_group_name: str) -> LogEventsResponse:
        pass
    
class CloudWatch(CloudWatchInterface):
    def __init__(self, cloudwatch_client):
        self.cloudwatch_client = cloudwatch_client

    def get_log_groups(self) -> LogGroupResponse:  
        """Fetches log groups in AWS account.

        Returns:
            LogGroupResponse: Returns iterable LogGroupResponse object. Iterate over LogGroupResponse.logGroups
            to get data from each object. 
        """
        try:
            log_groups = self.cloudwatch_client.describe_log_groups()
        except Exception as e:
            return f"An error occured fetching the log groups: {e}"
        finally:
            log_group_response = LogGroupResponse(logGroups=log_groups['logGroups'])
            return log_group_response 
        
    def get_log_streams(self, log_group: LogGroup=None ,log_group_name=None) -> LogStreamResponse:
        """Returns all log streams in AWS account for a sepcified log group. Accepts either 
           Log group name or LogGroup object returned from get_log_group function, Please only
           specify one. 

        Args:
            log_group (LogGroup, optional): Log Group object wanting to be passed in Defaults to None.
            log_group_name (_type_, optional: Name of log group in AWS. Defaults to None.

        Returns:
            LogStreamResponse: Returns log stream response object.
        """
        if log_group_name is None:
            log_group_name = log_group.logGroupName
        elif log_group is None and log_group_name == "":
            return f"Please pass either a log group object or the log group name"
        
        try: 
            log_stream = self.cloudwatch_client.describe_log_streams(logGroupIdentifier=log_group_name, orderBy="LastEventTime", descending=True, limit=50)
        except Exception as e:
            return f"An error occured fetching the logstream {e}"   
        else:
            log_stream_response = LogStreamResponse(logStreams=log_stream['logStreams'])
            return log_stream_response
   
        
    def get_log_events(self, log_stream_name: str, log_group_name: str) -> LogEventsResponse:
        """Fetches events for a specified log stream
        Args:
            log_stream_name (str): The name of the log stream you want the events for.
            log_group_name (str): The name of the group where the log stream lives. 
        """
        if log_group_name and log_stream_name:
            try:
                all_events = self.cloudwatch_client.get_log_events(logGroupIdentifier=log_group_name,logStreamName=log_stream_name)
            except Exception as e:
                return f"An error occured fetching the logs for the specified log group and log strea: {e}"
            else:
                events = LogEventsResponse(events=all_events['events'])
                return events
 
                        
                