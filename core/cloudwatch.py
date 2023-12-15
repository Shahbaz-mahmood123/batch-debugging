class LogGroup:
    def __init__(self, logGroupName, creationTime, retentionInDays, metricFilterCount, arn, storedBytes, kmsKeyId, dataProtectionStatus, inheritedProperties, logGroupClass):
        self.logGroupName = logGroupName
        self.creationTime = creationTime
        self.retentionInDays = retentionInDays
        self.metricFilterCount = metricFilterCount
        self.arn = arn
        self.storedBytes = storedBytes
        self.kmsKeyId = kmsKeyId
        self.dataProtectionStatus = dataProtectionStatus
        self.inheritedProperties = inheritedProperties
        self.logGroupClass = logGroupClass

class LogGroupResponse:
    def __init__(self, logGroups, nextToken):
        self.logGroups = [LogGroup(**group) for group in logGroups]
        self.nextToken = nextToken

class LogStream:
    def __init__(self, logStreamName, creationTime, firstEventTimestamp, lastEventTimestamp, lastIngestionTime, uploadSequenceToken, arn, storedBytes):
        self.logStreamName = logStreamName
        self.creationTime = creationTime
        self.firstEventTimestamp = firstEventTimestamp
        self.lastEventTimestamp = lastEventTimestamp
        self.lastIngestionTime = lastIngestionTime
        self.uploadSequenceToken = uploadSequenceToken
        self.arn = arn
        self.storedBytes = storedBytes

class LogStreamResponse:
    def __init__(self, logStreams, nextToken):
        self.logStreams = [LogStream(**stream) for stream in logStreams]
        self.nextToken = nextToken

class CloudWatchInterface():
    def get_log_groups() -> LogGroupResponse:
        pass
    
    def get_log_streams(log_group = [LogGroup]) -> LogStreamResponse:
        pass
    
class CloudWatch(CloudWatchInterface):
    def __init__(self, cloudwatch_client):
        self.cloudwatch_client = cloudwatch_client

    def get_log_groups(self) -> LogGroupResponse:  
        try:
            log_groups = self.cloudwatch_client.describe_log_groups()
            return log_groups 
        except Exception as e:
            return f"An error occured fetching the log groups {e}"
        
    def get_log_streams(self, log_group = LogGroup) -> LogStreamResponse:
        pass 