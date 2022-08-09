def getAlarms(vmanage, query):
    """
    Get alarms for last 30min if vManage query is not specified
    
    Parameters:
    query	 (dict):	 query data
    
    Returns
    response    (dict)
    
    Example query dictionary:
    query =   {"query": {"field": "active","type": "boolean", "value": ["true"], "operator": "equal" }}
    """
    
    query_string = vmanage.builder.generateQuery(query)
    endpoint = f"dataservice/alarms?query={query_string}"
    response     = vmanage.apiCall("GET", endpoint)
    return response
def getRawData(vmanage, alarmquerystring):
    """
    Gets lists of alarms along with the raw alarm data of each.
    
    Parameters:
    alarmquerystring:	Alarm query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms"
    response = vmanage.apiCall("POST", endpoint, alarmquerystring)
    return response
def getAggregationData(vmanage, query):
    """
    Gets aggregated list of alarms along with the raw alarm data of each aggregation
    
    Parameters:
    query	 (string):	Alarm query dict
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint = f"dataservice/alarms/aggregation?query={query_string}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getPostAggregationData(vmanage, inputquery):
    """
    Gets aggregated list of alarms along with the raw alarm data of each aggregation
    
    Parameters:
    inputquery:	Input query
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/aggregation"
    response = vmanage.apiCall("POST", endpoint, inputquery)
    return response
def clearStale(vmanage, alarm_uuid):
    """
    Clears specific stale alarm
    
    Parameters:
    alarm_uuid:	alarm_uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/clear"
    response = vmanage.apiCall("POST", endpoint, alarm_uuid)
    return response
def getNonViewedActiveCount(vmanage):
    """
    Get count of the alarms which are active and acknowledged by the user
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/count"
    response = vmanage.apiCall("GET", endpoint)
    return response
def listDisabled(vmanage):
    """
    List all disabled alarms
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/disabled"
    response = vmanage.apiCall("GET", endpoint)
    return response
def disableEnable(vmanage, alarmconfig, eventName, disable, time):
    """
    Enable/Disable a specific alarm
    
    Parameters:
    alarmconfig:	    alarm config
	eventName	 (string):	Event name
	disable	    (boolean):	Disable
	time	    (integer):	time in hours [1, 72], -1 means infinite
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/disabled?eventName={eventName}&disable={disable}&time={time}"
    response = vmanage.apiCall("POST", endpoint, alarmconfig)
    return response
def getCount(vmanage, query):
    """
    Get response count of a query
    
    Parameters:
    query	 (string):	Query
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint = f"dataservice/alarms/doccount?query={query_string}"
    response     = vmanage.apiCall("GET", endpoint)
    return response
def getCountPost(vmanage, query):
    """
    Get response count of a query
    
    Parameters:
    query:	Query
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/doccount"
    response = vmanage.apiCall("POST", endpoint, query)
    return response
def dumpCorrelationEngineData(vmanage):
    """
    dump correlation engine server data
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/dump"
    response = vmanage.apiCall("POST", endpoint)
    return response
def getStatDataFields(vmanage):
    """
    Get fields and type
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/fields"
    response = vmanage.apiCall("GET", endpoint)
    return response
def markAllAsViewed(vmanage, bodyParameter, type):
    """
    Mark all larms as acknowledged by the user
    
    Parameters:
    bodyParameter:	Description
	type	 (string):	Query filter, possible value are "active" "cleared"
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/markallasviewed?type={type}"
    response = vmanage.apiCall("POST", endpoint, bodyParameter)
    return response
def markAsViewed(vmanage, listofalarms):
    """
    Mark alarms as acknowledged by the user
    
    Parameters:
    listofalarms:	List of alarms
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/markviewed"
    response = vmanage.apiCall("POST", endpoint, listofalarms)
    return response
def getMasterManagerState(vmanage):
    """
    Get master manager state
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/master"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getNonViewed(vmanage):
    """
    Get alarms which are active and acknowledged by the user
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/notviewed"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getStatBulkAlarmRawData(vmanage, query, scrollId, count):
    """
    Get paginated alarm raw data
    
    Parameters:
    query	     (string):	Alarm query string
	scrollId	 (string):	Query offset
	count	    (integer):	Query size
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/page?query={query}&scrollId={scrollId}&count={count}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getPostStatBulkAlarmRawData(vmanage, alarmquerystring, scrollId, count):
    """
    Get paginated alarm raw data
    
    Parameters:
    alarmquerystring:	    Alarm query string
	scrollId	 (string):	Query offset
	count	    (integer):	Query size
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/page?scrollId={scrollId}&count={count}"
    response = vmanage.apiCall("POST", endpoint, alarmquerystring)
    return response
def setPeriodicPurgeTimer(vmanage, interval, activeTime):
    """
    Set alarm purge timer
    
    Parameters:
    interval	 (string):	Purge interval
	activeTime	 (string):	Purge activeTime
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/purgefrequency?interval={interval}&activeTime={activeTime}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getStatQueryFields(vmanage):
    """
    Get query fields
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/query/fields"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getQueryConfig(vmanage):
    """
    Get query configuration
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/query/input"
    response = vmanage.apiCall("GET", endpoint)
    return response
def correlAntiEntropy(vmanage):
    """
    Reset correlation engine data
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/reset"
    response = vmanage.apiCall("GET", endpoint)
    return response
def restartCorrelationEngine(vmanage):
    """
    Restart correlation engine
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/restart"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getTypesAsKeyValue(vmanage):
    """
    Gets alarm type as key value pair
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/rulenamedisplay/keyvalue"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getBySeverity(vmanage, level, deviceId, query):
    """
    Get alarm by severity
    
    Parameters:
    level	     (array):	Alarm severity
	deviceId	 (array):	Device Id
	query	    (string):	Query filter
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/severity?severity-level={level}&deviceId={deviceId}&query={query}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getSeverityCustomHistogram(vmanage, query):
    """
    Get alarm severity histogram
    
    Parameters:
    query	 (string):	Alarm histogram query string
    
    Returns
    response    (dict)
    
    
    """
    query_string = vmanage.builder.generateQuery(query)
    endpoint = f"dataservice/alarms/severity/summary?query={query_string}"
    response     = vmanage.apiCall("GET", endpoint)
    return response
def getSeverityMappings(vmanage):
    """
    Gets alarm severity mappings
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/severitymappings"
    response = vmanage.apiCall("GET", endpoint)
    return response
def startTracking(vmanage, testName):
    """
    Start tracking events
    
    Parameters:
    testName	 (string):	test name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/starttracking/{testName}"
    response = vmanage.apiCall("POST", endpoint)
    return response
def getStats(vmanage):
    """
    Get alarm statistics
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/stats"
    response = vmanage.apiCall("GET", endpoint)
    return response
def stopTracking(vmanage, testName):
    """
    Stop tracking events
    
    Parameters:
    testName	 (string):	test name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/stoptracking/{testName}"
    response = vmanage.apiCall("POST", endpoint)
    return response
def getDeviceTopic(vmanage, ip):
    """
    Get device topic state
    
    Parameters:
    ip	 (string):	Query topic
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/topic?ip={ip}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getDetails(vmanage, alarm_uuid):
    """
    Get alarm detail
    
    Parameters:
    alarm_uuid	 (string):	Alarm Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/alarms/uuid/{alarm_uuid}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def updateNotificationRule(vmanage, notificationrule, ruleId):
    """
    Update notification rule
    
    Parameters:
    notificationrule:	Notification rule
	ruleId	 (string):	Rule Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/notifications/rule?ruleId={ruleId}"
    response = vmanage.apiCall("PUT", endpoint, notificationrule)
    return response
def createNotificationRule(vmanage, notificationrule):
    """
    Add notification rule
    
    Parameters:
    notificationrule:	Notification rule
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/notifications/rule"
    response = vmanage.apiCall("POST", endpoint, notificationrule)
    return response
def getNotificationRule(vmanage, ruleId):
    """
    Get all rules or specific notification rule by its Id
    
    Parameters:
    ruleId	 (string):	Rule Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/notifications/rules?ruleId={ruleId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def deleteNotificationRule(vmanage, ruleId):
    """
    Delete notification rule
    
    Parameters:
    ruleId	 (string):	Rule Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/notifications/rules?ruleId={ruleId}"
    response = vmanage.apiCall("DELETE", endpoint)
    return response
