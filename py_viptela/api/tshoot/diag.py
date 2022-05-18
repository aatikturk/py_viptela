from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Diag(object):
    """
    Troubleshooting Tools - Diagnostics API
    
    Implements GET POST DEL PUT methods for Diagnostics endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getDBSchema(self):
        """
        Get the current database schema
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/diagnostics/dbschema"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getThreadPools(self):
        """
        Get information on the threadpools
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/diagnostics/threadpools"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatDataRawData(self, query):
        """
        Get stats raw data
        
        Parameters:
        query	 (string):	Query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/speedtest?query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatsRawData(self, query):
        """
        Get stats raw data
        
        Parameters:
        query:	Stats query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/speedtest"
        response = self.client.apiCall(HttpMethods.POST, endpoint, query)
        return response


    def getAggregationDataByQuery(self, query):
        """
        Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
        
        Parameters:
        query	 (string):	Query filter
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/speedtest/aggregation?query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getPostAggregationDataByQuery(self, query):
        """
        Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
        
        Parameters:
        query:	Stats query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/speedtest/aggregation"
        response = self.client.apiCall(HttpMethods.POST, endpoint, query)
        return response


    def getPostAggregationAppDataByQuery(self, query):
        """
        Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
        
        Parameters:
        query:	Stats query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/speedtest/app-agg/aggregation"
        response = self.client.apiCall(HttpMethods.POST, endpoint, query)
        return response


    def getStatDataRawDataAsCSV(self, query):
        """
        Get raw data with optional query as CSV
        
        Parameters:
        query	 (string):	Query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/speedtest/csv?query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCount(self, query):
        """
        Get response count of a query
        
        Parameters:
        query	 (string):	Query
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/speedtest/doccount?query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCountPost(self, query):
        """
        Get response count of a query
        
        Parameters:
        query:	Query
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/speedtest/doccount"
        response = self.client.apiCall(HttpMethods.POST, endpoint, query)
        return response


    def getStatDataFields(self):
        """
        Get fields and type
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/speedtest/fields"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatBulkRawData(self, query, scrollId, count):
        """
        Get stats raw data
        
        Parameters:
        query	 (string):	Query string
		scrollId	 (string):	ES scroll Id
		count	 (string):	Result size
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/speedtest/page?query={query}&scrollId={scrollId}&count={count}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getPostStatBulkRawData(self, query, scrollId, count):
        """
        Get stats raw data
        
        Parameters:
        query:	Stats query string
		scrollId	 (string):	ES scroll Id
		count	 (string):	Result size
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/speedtest/page?scrollId={scrollId}&count={count}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, query)
        return response


    def getStatQueryFields(self):
        """
        Get query fields
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/statistics/speedtest/query/fields"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSessionInfoCapture(self, payload):
        """
        getSessionInfoCapture Description
        
        Parameters:
        payload:    Request Payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/capture"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def disablePacketCaptureSession(self, sessionId):
        """
        disablePacketCaptureSession Description
        
        Parameters:
        Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/capture/disable/{sessionId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def downloadFile(self, sessionId):
        """
        downloadFile Description
        
        Parameters:
        Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/capture/download/{sessionId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def forceStopPcapSession(self, sessionId):
        """
        forceStopPcapSession Description
        
        Parameters:
        Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/capture/forcedisbale/{sessionId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def startPcapSession(self, sessionId):
        """
        startPcapSession Description
        
        Parameters:
        Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/capture/start/{sessionId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getFileDownloadStatus(self, sessionId):
        """
        getFileDownloadStatus Description
        
        Parameters:
        Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/capture/status/{sessionId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def stopPcapSession(self, sessionId):
        """
        stopPcapSession Description
        
        Parameters:
        Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/capture/stop/{sessionId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def formPostPacketCapture(self, deviceUUID, sessionId):
        """
        formPostPacketCapture Description
        
        Parameters:
        Parameter Description
		Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/capture/{deviceUUID}/{sessionId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getSessionInfoLog(self, payload):
        """
        getSessionInfoLog Description
        
        Parameters:
        payload:    Request Payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/log"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def disableDeviceLog(self, sessionId):
        """
        disableDeviceLog Description
        
        Parameters:
        sessionId	 (string):	Session Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/log/disable/{sessionId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def downloadDebugLog(self, sessionId):
        """
        downloadDebugLog Description
        
        Parameters:
        sessionId	 (string):	Session Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/log/download/{sessionId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def renewSessionInfo(self, sessionId):
        """
        renewSessionInfo Description
        
        Parameters:
        Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/log/renew/{sessionId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def searchDeviceLog(self, payload, sessionId):
        """
        searchDeviceLog Description
        
        Parameters:
        payload:    Request Payload
		sessionId	 (string):	Session Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/log/search/{sessionId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def getSessions(self):
        """
        getSessions Description
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/log/sessions"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def clearSession(self, sessionId):
        """
        clearSession Description
        
        Parameters:
        sessionId	 (string):	Session Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/log/sessions/clear/{sessionId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getLogType(self, uuid):
        """
        getLogType Description
        
        Parameters:
        uuid	 (string):	Device uuid
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/log/type?uuid={uuid}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def streamLog(self, payload, logType, deviceUUID, sessionId):
        """
        streamLog Description
        
        Parameters:
        payload:    Request Payload
		logType	 (string):	Log type
		deviceUUID	 (string):	Device uuid
		sessionId	 (string):	Session Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/log/{logType}/{deviceUUID}/{sessionId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def getDeviceLog(self, sessionId, logId):
        """
        getDeviceLog Description
        
        Parameters:
        Parameter Description
		Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/log/{sessionId}?logId={logId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatDataRawData(self, query):
        """
        Get stats raw data
        
        Parameters:
        query	 (string):	Query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi?query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatsRawData(self, query):
        """
        Get stats raw data
        
        Parameters:
        query:	Stats query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi"
        response = self.client.apiCall(HttpMethods.POST, endpoint, query)
        return response


    def getAggregationDataByQuery(self, query):
        """
        Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
        
        Parameters:
        query	 (string):	Query filter
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/aggregation?query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getPostAggregationDataByQuery(self, query):
        """
        Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
        
        Parameters:
        query:	Stats query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/aggregation"
        response = self.client.apiCall(HttpMethods.POST, endpoint, query)
        return response


    def getPostAggregationAppDataByQuery(self, query):
        """
        Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage
        
        Parameters:
        query:	Stats query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/app-agg/aggregation"
        response = self.client.apiCall(HttpMethods.POST, endpoint, query)
        return response


    def getConcurrentData(self, traceId, timestamp):
        """
        getConcurrentData Description
        
        Parameters:
        traceId	 (integer):	trace id
		timestamp	 (integer):	start time
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/concurrentData?traceId={traceId}&timestamp={timestamp}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getConcurrentDomainData(self, traceId, timestamp):
        """
        getConcurrentDomainData Description
        
        Parameters:
        traceId	 (integer):	trace id
		timestamp	 (integer):	start time
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/concurrentDomainData?traceId={traceId}&timestamp={timestamp}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatDataRawDataAsCSV(self, query):
        """
        Get raw data with optional query as CSV
        
        Parameters:
        query	 (string):	Query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/csv?query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCount(self, query):
        """
        Get response count of a query
        
        Parameters:
        query	 (string):	Query
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/doccount?query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCountPost(self, query):
        """
        Get response count of a query
        
        Parameters:
        query:	Query
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/doccount"
        response = self.client.apiCall(HttpMethods.POST, endpoint, query)
        return response


    def getDomainMetric(self, traceId, timestamp, domain, firstTimestamp, lastTimestamp):
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/domainMetric?traceId={traceId}&timestamp={timestamp}&domain={domain}&firstTimestamp={firstTimestamp}&lastTimestamp={lastTimestamp}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatDataFields(self):
        """
        Get fields and type
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/fields"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getFinalizedData(self, traceId, timestamp):
        """
        getFinalizedData Description
        
        Parameters:
        traceId	 (integer):	trace id
		timestamp	 (integer):	start time
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/finalizedData?traceId={traceId}&timestamp={timestamp}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getFinalizedDomainData(self, traceId, timestamp):
        """
        getFinalizedDomainData Description
        
        Parameters:
        traceId	 (integer):	trace id
		timestamp	 (integer):	start time
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/finalizedDomainData?traceId={traceId}&timestamp={timestamp}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getFlowDetail(self, traceId, timestamp, flowId):
        """
        getFlowDetail Description
        
        Parameters:
        traceId	 (integer):	trace id
		timestamp	 (integer):	start time
		flowId	 (integer):	flow id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/flowDetail?traceId={traceId}&timestamp={timestamp}&flowId={flowId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getFlowMetric(self, traceId, timestamp, flowId, firstTimestamp, lastTimestamp):
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/flowMetric?traceId={traceId}&timestamp={timestamp}&flowId={flowId}&firstTimestamp={firstTimestamp}&lastTimestamp={lastTimestamp}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getMonitorState(self, traceId, state):
        """
        getMonitorState Description
        
        Parameters:
        traceId	 (integer):	trace id
		state	 (string):	trace state
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/getMonitorState?traceId={traceId}&state={state}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def monitorStart(self, payload):
        """
        CXP Monitor Action - Start
        
        Parameters:
        payload:    Request Payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/monitor/start"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def monitorStop(self, payload):
        """
        CXP Monitor Action - Stop
        
        Parameters:
        payload:    Request Payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/monitor/stop"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def getNwpiDscp(self):
        """
        getNwpiDscp Description
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/nwpiDSCP"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getNwpiNbarAppGroup(self):
        """
        getNwpiNbarAppGroup Description
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/nwpiNbarAppGroup"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getNwpiProtocol(self):
        """
        getNwpiProtocol Description
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/nwpiProtocol"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getPacketFeatures(self, traceId, timestamp, flowId):
        """
        getPacketFeatures Description
        
        Parameters:
        traceId	 (integer):	trace id
		timestamp	 (integer):	start time
		flowId	 (integer):	flow id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/packetFeatures?traceId={traceId}&timestamp={timestamp}&flowId={flowId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatBulkRawData(self, query, scrollId, count):
        """
        Get stats raw data
        
        Parameters:
        query	 (string):	Query string
		scrollId	 (string):	ES scroll Id
		count	 (string):	Result size
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/page?query={query}&scrollId={scrollId}&count={count}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getPostStatBulkRawData(self, query, scrollId, count):
        """
        Get stats raw data
        
        Parameters:
        query:	Stats query string
		scrollId	 (string):	ES scroll Id
		count	 (string):	Result size
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/page?scrollId={scrollId}&count={count}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, query)
        return response


    def getStatQueryFields(self):
        """
        Get query fields
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/query/fields"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def traceDelete(self, traceId, timestamp):
        """
        Trace Action - Delete
        
        Parameters:
        traceId	 (string):	trace id
		timestamp	 (integer):	start time
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/trace/delete?traceId={traceId}&timestamp={timestamp}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def traceStart(self, payload):
        """
        Trace Action - Start
        
        Parameters:
        payload:    Request Payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/trace/start"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def traceStop(self, traceId):
        """
        Trace Action - Stop
        
        Parameters:
        Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/trace/stop/{traceId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def traceFinFlowWithQuery(self, traceId, timestamp, query):
        """
        Retrieve Certain Fin Flows
        
        Parameters:
        traceId	 (integer):	trace id
		timestamp	 (integer):	start time
		query	 (string):	Query filter
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/traceFinFlowWithQuery?traceId={traceId}&timestamp={timestamp}&query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTraceFlow(self, traceId, timestamp, state):
        """
        getTraceFlow Description
        
        Parameters:
        traceId	 (integer):	trace id
		timestamp	 (integer):	start time
		state	 (string):	trace state
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/traceFlow?traceId={traceId}&timestamp={timestamp}&state={state}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTraceHistory(self):
        """
        getTraceHistory Description
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/nwpi/traceHistory"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSession(self, payload):
        """
        getSession Description
        
        Parameters:
        payload:    Request Payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/speed"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def disableSpeedTestSession(self, sessionId):
        """
        disableSpeedTestSession Description
        
        Parameters:
        Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/speed/disable/{sessionId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getInterfaceBandwidth(self, circuit, deviceUUID):
        """
        getInterfaceBandwidth Description
        
        Parameters:
        Parameter Description
		Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/speed/interface/bandwidth?circuit={circuit}&deviceUUID={deviceUUID}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def startSpeedTest(self, sessionId):
        """
        startSpeedTest Description
        
        Parameters:
        Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/speed/start/{sessionId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSpeedTestStatus(self, sessionId):
        """
        getSpeedTestStatus Description
        
        Parameters:
        Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/speed/status/{sessionId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def stopSpeedTest(self, sessionId):
        """
        stopSpeedTest Description
        
        Parameters:
        Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/speed/stop/{sessionId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def saveSpeedTestResults(self, payload, deviceUUID, sessionId):
        """
        saveSpeedTestResults Description
        
        Parameters:
        payload:    Request Payload
		Parameter Description
		Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/speed/{deviceUUID}/{sessionId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def getSpeedTest(self, sessionId, logId):
        """
        getSpeedTest Description
        
        Parameters:
        Parameter Description
		Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/speed/{sessionId}?logId={logId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def processDeviceStatus(self, payload, deviceUUID):
        """
        Get device status stream
        
        Parameters:
        payload:    Request Payload
		deviceUUID	 (string):	Device uuid
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/stream/device/status/{deviceUUID}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


