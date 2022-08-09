def getDBSchema(vmanage):
    """
    Get the current database schema
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/diagnostics/dbschema"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getThreadPools(vmanage):
    """
    Get information on the threadpools
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/diagnostics/threadpools"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getStatDataRawData(vmanage, query):
    """
    Get stats raw data
    
    Parameters:
    query	 (string):	Query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/speedtest?query={query}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getStatsRawData(vmanage, query):
    """
    Get stats raw data
    
    Parameters:
    query:	Stats query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/speedtest"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, query)
    return response
def getAggregationDataByQuery(vmanage, query):
    """
    Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
    
    Parameters:
    query	 (string):	Query filter
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/speedtest/aggregation?query={query}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getPostAggregationDataByQuery(vmanage, query):
    """
    Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
    
    Parameters:
    query:	Stats query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/speedtest/aggregation"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, query)
    return response
def getPostAggregationAppDataByQuery(vmanage, query):
    """
    Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
    
    Parameters:
    query:	Stats query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/speedtest/app-agg/aggregation"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, query)
    return response
def getStatDataRawDataAsCSV(vmanage, query):
    """
    Get raw data with optional query as CSV
    
    Parameters:
    query	 (string):	Query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/speedtest/csv?query={query}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getCount(vmanage, query):
    """
    Get response count of a query
    
    Parameters:
    query	 (string):	Query
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/speedtest/doccount?query={query}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getCountPost(vmanage, query):
    """
    Get response count of a query
    
    Parameters:
    query:	Query
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/speedtest/doccount"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, query)
    return response
def getStatDataFields(vmanage):
    """
    Get fields and type
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/speedtest/fields"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getStatBulkRawData(vmanage, query, scrollId, count):
    """
    Get stats raw data
    
    Parameters:
    query	 (string):	Query string
	scrollId	 (string):	ES scroll Id
	count	 (string):	Result size
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/speedtest/page?query={query}&scrollId={scrollId}&count={count}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getPostStatBulkRawData(vmanage, query, scrollId, count):
    """
    Get stats raw data
    
    Parameters:
    query:	Stats query string
	scrollId	 (string):	ES scroll Id
	count	 (string):	Result size
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/speedtest/page?scrollId={scrollId}&count={count}"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, query)
    return response
def getStatQueryFields(vmanage):
    """
    Get query fields
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/statistics/speedtest/query/fields"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getSessionInfoCapture(vmanage, payload):
    """
    getSessionInfoCapture Description
    
    Parameters:
    payload:    Request Payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/capture"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, payload)
    return response
def disablePacketCaptureSession(vmanage, sessionId):
    """
    disablePacketCaptureSession Description
    
    Parameters:
    sessionId  (string): Process uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/capture/disable/{sessionId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def downloadFile(vmanage, sessionId):
    """
    downloadFile Description
    
    Parameters:
    sessionId  (string): Process uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/capture/download/{sessionId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def forceStopPcapSession(vmanage, sessionId):
    """
    forceStopPcapSession Description
    
    Parameters:
    sessionId  (string): Process uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/capture/forcedisbale/{sessionId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def startPcapSession(vmanage, sessionId):
    """
    startPcapSession Description
    
    Parameters:
    sessionId  (string): Process uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/capture/start/{sessionId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getFileDownloadStatus(vmanage, sessionId):
    """
    getFileDownloadStatus Description
    
    Parameters:
    sessionId  (string): Process uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/capture/status/{sessionId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def stopPcapSession(vmanage, sessionId):
    """
    stopPcapSession Description
    
    Parameters:
    sessionId  (string): Process uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/capture/stop/{sessionId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def formPostPacketCapture(vmanage, deviceUUID, sessionId):
    """
    formPostPacketCapture Description
    
    Parameters:
    deviceUUID:     (string) Device uuid
	sessionId:      (string) Process uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/capture/{deviceUUID}/{sessionId}"
    response = vmanage.client.apiCall(vmanage.POST, endpoint)
    return response
def getSessionInfoLog(vmanage, payload):
    """
    getSessionInfoLog Description
    
    Parameters:
    payload:    Request Payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/log"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, payload)
    return response
def disableDeviceLog(vmanage, sessionId):
    """
    disableDeviceLog Description
    
    Parameters:
    sessionId	 (string):	Session Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/log/disable/{sessionId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def downloadDebugLog(vmanage, sessionId):
    """
    downloadDebugLog Description
    
    Parameters:
    sessionId  (string): Process uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/log/download/{sessionId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def renewSessionInfo(vmanage, sessionId):
    """
    renewSessionInfo Description
    
    Parameters:
    sessionId  (string): Process uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/log/renew/{sessionId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def searchDeviceLog(vmanage, payload, sessionId):
    """
    searchDeviceLog Description
    
    Parameters:
    payload:    Request Payload
	sessionId  (string): Process uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/log/search/{sessionId}"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, payload)
    return response
def getSessions(vmanage):
    """
    getSessions Description
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/log/sessions"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def clearSession(vmanage, sessionId):
    """
    clearSession Description
    
    Parameters:
    sessionId  (string): Process uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/log/sessions/clear/{sessionId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getLogType(vmanage, uuid):
    """
    getLogType Description
    
    Parameters:
    uuid	 (string):	Device uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/log/type?uuid={uuid}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def streamLog(vmanage, payload, logType, deviceUUID, sessionId):
    """
    streamLog Description
    
    Parameters:
    payload:    Request Payload
	logType	 (string):	Log type
	deviceUUID	 (string):	Device uuid
	sessionId  (string): Process uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/log/{logType}/{deviceUUID}/{sessionId}"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, payload)
    return response
def getDeviceLog(vmanage, sessionId, logId):
    """
    getDeviceLog Description
    
    Parameters:
    sessionId   (string): Process uuid
	logId       (string): log ID
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/log/{sessionId}?logId={logId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getStatDataRawData(vmanage, query):
    """
    Get stats raw data
    
    Parameters:
    query	 (string):	Query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi?query={query}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getStatsRawData(vmanage, query):
    """
    Get stats raw data
    
    Parameters:
    query:	Stats query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, query)
    return response
def getAggregationDataByQuery(vmanage, query):
    """
    Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
    
    Parameters:
    query	 (string):	Query filter
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/aggregation?query={query}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getPostAggregationDataByQuery(vmanage, query):
    """
    Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
    
    Parameters:
    query:	Stats query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/aggregation"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, query)
    return response
def getPostAggregationAppDataByQuery(vmanage, query):
    """
    Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
    
    Parameters:
    query:	Stats query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/app-agg/aggregation"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, query)
    return response
def getConcurrentData(vmanage, traceId, timestamp):
    """
    getConcurrentData Description
    
    Parameters:
    traceId	 (integer):	trace id
	timestamp	 (integer):	start time
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/concurrentData?traceId={traceId}&timestamp={timestamp}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getConcurrentDomainData(vmanage, traceId, timestamp):
    """
    getConcurrentDomainData Description
    
    Parameters:
    traceId	 (integer):	trace id
	timestamp	 (integer):	start time
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/concurrentDomainData?traceId={traceId}&timestamp={timestamp}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getStatDataRawDataAsCSV(vmanage, query):
    """
    Get raw data with optional query as CSV
    
    Parameters:
    query	 (string):	Query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/csv?query={query}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getCount(vmanage, query):
    """
    Get response count of a query
    
    Parameters:
    query	 (string):	Query
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/doccount?query={query}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getCountPost(vmanage, query):
    """
    Get response count of a query
    
    Parameters:
    query:	Query
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/doccount"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, query)
    return response
def getDomainMetric(vmanage, traceId, timestamp, domain, firstTimestamp, lastTimestamp):
    """
    getDomainMetric Description
    
    Parameters:
    traceId	 (integer):	trace id
	timestamp	 (integer):	start time
	domain	 (string):	domain name
	firstTimestamp	 (integer):	first timestamp of xAxis
	lastTimestamp	 (integer):	last timestamp of xAxis
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/domainMetric?traceId={traceId}&timestamp={timestamp}&domain={domain}&firstTimestamp={firstTimestamp}&lastTimestamp={lastTimestamp}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getStatDataFields(vmanage):
    """
    Get fields and type
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/fields"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getFinalizedData(vmanage, traceId, timestamp):
    """
    getFinalizedData Description
    
    Parameters:
    traceId	 (integer):	trace id
	timestamp	 (integer):	start time
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/finalizedData?traceId={traceId}&timestamp={timestamp}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getFinalizedDomainData(vmanage, traceId, timestamp):
    """
    getFinalizedDomainData Description
    
    Parameters:
    traceId	 (integer):	trace id
	timestamp	 (integer):	start time
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/finalizedDomainData?traceId={traceId}&timestamp={timestamp}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getFlowDetail(vmanage, traceId, timestamp, flowId):
    """
    getFlowDetail Description
    
    Parameters:
    traceId	 (integer):	trace id
	timestamp	 (integer):	start time
	flowId	 (integer):	flow id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/flowDetail?traceId={traceId}&timestamp={timestamp}&flowId={flowId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getFlowMetric(vmanage, traceId, timestamp, flowId, firstTimestamp, lastTimestamp):
    """
    getFlowMetric Description
    
    Parameters:
    traceId	 (integer):	trace id
	timestamp	 (integer):	start time
	flowId	 (integer):	flow id
	firstTimestamp	 (integer):	first timestamp of xAxis
	lastTimestamp	 (integer):	last timestamp of xAxis
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/flowMetric?traceId={traceId}&timestamp={timestamp}&flowId={flowId}&firstTimestamp={firstTimestamp}&lastTimestamp={lastTimestamp}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getMonitorState(vmanage, traceId, state):
    """
    getMonitorState Description
    
    Parameters:
    traceId	 (integer):	trace id
	state	 (string):	trace state
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/getMonitorState?traceId={traceId}&state={state}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def monitorStart(vmanage, payload):
    """
    CXP Monitor Action - Start
    
    Parameters:
    payload:    Request Payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/monitor/start"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, payload)
    return response
def monitorStop(vmanage, payload):
    """
    CXP Monitor Action - Stop
    
    Parameters:
    payload:    Request Payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/monitor/stop"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, payload)
    return response
def getNwpiDscp(vmanage):
    """
    getNwpiDscp Description
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/nwpiDSCP"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getNwpiNbarAppGroup(vmanage):
    """
    getNwpiNbarAppGroup Description
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/nwpiNbarAppGroup"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getNwpiProtocol(vmanage):
    """
    getNwpiProtocol Description
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/nwpiProtocol"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getPacketFeatures(vmanage, traceId, timestamp, flowId):
    """
    getPacketFeatures Description
    
    Parameters:
    traceId	 (integer):	trace id
	timestamp	 (integer):	start time
	flowId	 (integer):	flow id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/packetFeatures?traceId={traceId}&timestamp={timestamp}&flowId={flowId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getStatBulkRawData(vmanage, query, scrollId, count):
    """
    Get stats raw data
    
    Parameters:
    query	 (string):	Query string
	scrollId	 (string):	ES scroll Id
	count	 (string):	Result size
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/page?query={query}&scrollId={scrollId}&count={count}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getPostStatBulkRawData(vmanage, query, scrollId, count):
    """
    Get stats raw data
    
    Parameters:
    query:	Stats query string
	scrollId	 (string):	ES scroll Id
	count	 (string):	Result size
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/page?scrollId={scrollId}&count={count}"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, query)
    return response
def getStatQueryFields(vmanage):
    """
    Get query fields
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/query/fields"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def traceDelete(vmanage, traceId, timestamp):
    """
    Trace Action - Delete
    
    Parameters:
    traceId	 (string):	trace id
	timestamp	 (integer):	start time
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/trace/delete?traceId={traceId}&timestamp={timestamp}"
    response = vmanage.client.apiCall(vmanage.DELETE, endpoint)
    return response
def traceStart(vmanage, payload):
    """
    Trace Action - Start
    
    Parameters:
    payload:    Request Payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/trace/start"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, payload)
    return response
def traceStop(vmanage, traceId):
    """
    Trace Action - Stop
    
    Parameters:
    Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/trace/stop/{traceId}"
    response = vmanage.client.apiCall(vmanage.POST, endpoint)
    return response
def traceFinFlowWithQuery(vmanage, traceId, timestamp, query):
    """
    Retrieve Certain Fin Flows
    
    Parameters:
    traceId	 (integer):	trace id
	timestamp	 (integer):	start time
	query	 (string):	Query filter
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/traceFinFlowWithQuery?traceId={traceId}&timestamp={timestamp}&query={query}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getTraceFlow(vmanage, traceId, timestamp, state):
    """
    getTraceFlow Description
    
    Parameters:
    traceId	 (integer):	trace id
	timestamp	 (integer):	start time
	state	 (string):	trace state
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/traceFlow?traceId={traceId}&timestamp={timestamp}&state={state}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getTraceHistory(vmanage):
    """
    getTraceHistory Description
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/nwpi/traceHistory"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getSession(vmanage, payload):
    """
    getSession Description
    
    Parameters:
    payload:    Request Payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/speed"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, payload)
    return response
def disableSpeedTestSession(vmanage, sessionId):
    """
    disableSpeedTestSession Description
    
    Parameters:
    sessionId  (string): Process uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/speed/disable/{sessionId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getInterfaceBandwidth(vmanage, circuit, deviceUUID):
    """
    getInterfaceBandwidth Description
    
    Parameters:
    circuit     (string):   Circuit
	deviceUUID  (string):   Device ID
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/speed/interface/bandwidth?circuit={circuit}&deviceUUID={deviceUUID}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def startSpeedTest(vmanage, sessionId):
    """
    startSpeedTest Description
    
    Parameters:
    sessionId  (string): Process uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/speed/start/{sessionId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getSpeedTestStatus(vmanage, sessionId):
    """
    getSpeedTestStatus Description
    
    Parameters:
    sessionId  (string): Process uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/speed/status/{sessionId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def stopSpeedTest(vmanage, sessionId):
    """
    stopSpeedTest Description
    
    Parameters:
    sessionId  (string): Process uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/speed/stop/{sessionId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def saveSpeedTestResults(vmanage, payload, deviceUUID, sessionId):
    """
    saveSpeedTestResults Description
    
    Parameters:
    payload:    Request Payload
	deviceUUID  (string):   Device ID
	sessionId  (string): Process uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/speed/{deviceUUID}/{sessionId}"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, payload)
    return response
def getSpeedTest(vmanage, sessionId, logId):
    """
    getSpeedTest Description
    
    Parameters:
    sessionId  (string): Process uuid
	logId       (string): Log ID
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/speed/{sessionId}?logId={logId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def processDeviceStatus(vmanage, payload, deviceUUID):
    """
    Get device status stream
    
    Parameters:
    payload:    Request Payload
	deviceUUID	 (string):	Device uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/stream/device/status/{deviceUUID}"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, payload)
    return response
