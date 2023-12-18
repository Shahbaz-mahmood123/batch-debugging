class LogGroup:
    def __init__(self, logGroupName, creationTime, metricFilterCount, arn, storedBytes, logGroupClass=None,
                 retentionInDays=None ,kmsKeyId=None,dataProtectionStatus=None, inheritedProperties=None ):
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
    def __init__(self, logGroups, nextToken=None):
        self.logGroups = [LogGroup(**group) for group in logGroups]
        self.nextToken = nextToken

class LogStream:
    def __init__(self, logStreamName, creationTime, arn, storedBytes, 
                 firstEventTimestamp=None,lastEventTimestamp=None, lastIngestionTime=None, uploadSequenceToken=None):
        self.logStreamName = logStreamName
        self.creationTime = creationTime
        self.firstEventTimestamp = firstEventTimestamp
        self.lastEventTimestamp = lastEventTimestamp
        self.lastIngestionTime = lastIngestionTime
        self.uploadSequenceToken = uploadSequenceToken
        self.arn = arn
        self.storedBytes = storedBytes

class LogStreamResponse:
    def __init__(self, logStreams, nextToken=None):
        self.logStreams = [LogStream(**stream) for stream in logStreams]
        self.nextToken = nextToken

class LogEvent:
    def __init__(self, timestamp, message, ingestionTime):
        self.timestamp = timestamp
        self.message = message
        self.ingestionTime = ingestionTime

class LogEventsResponse:
    def __init__(self, events, nextForwardToken=None, nextBackwardToken=None):
        self.events = [LogEvent(**event) for event in events]
        self.nextForwardToken = nextForwardToken
        self.nextBackwardToken = nextBackwardToken
