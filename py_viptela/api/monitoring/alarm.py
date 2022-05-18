from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Alarm(object):
    """
    Monitoring - Alarms Details API
    
    Implements GET POST DEL PUT methods for AlarmsDetails endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getAlarms(self, query):
        """
        Get alarms for last 30min if vManage query is not specified
        
        Parameters:
        query	 (string):	Alarm query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms?query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getRawData(self, alarmquerystring):
        """
        Gets lists of alarms along with the raw alarm data of each.
        
        Parameters:
        alarmquerystring:	Alarm query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms"
        response = self.client.apiCall(HttpMethods.POST, endpoint, alarmquerystring)
        return response


    def getAggregationData(self, query):
        """
        Gets aggregated list of alarms along with the raw alarm data of each aggregation
        
        Parameters:
        query	 (string):	Alarm query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/aggregation?query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getPostAggregationData(self, inputquery):
        """
        Gets aggregated list of alarms along with the raw alarm data of each aggregation
        
        Parameters:
        inputquery:	Input query
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/aggregation"
        response = self.client.apiCall(HttpMethods.POST, endpoint, inputquery)
        return response


    def clearStale(self, alarm_uuid):
        """
        Clears specific stale alarm
        
        Parameters:
        alarm_uuid:	alarm_uuid
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/clear"
        response = self.client.apiCall(HttpMethods.POST, endpoint, alarm_uuid)
        return response


    def getNonViewedActiveCount(self):
        """
        Get count of the alarms which are active and acknowledged by the user
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/count"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def listDisabled(self):
        """
        List all disabled alarms
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/disabled"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def disableEnable(self, alarmconfig, eventName, disable, time):
        """
        Enable/Disable a specific alarm
        
        Parameters:
        alarmconfig:	alarm config
		eventName	 (string):	Event name
		disable	 (boolean):	Disable
		time	 (integer):	time in hours [1, 72], -1 means infinite
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/disabled?eventName={eventName}&disable={disable}&time={time}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, alarmconfig)
        return response


    def getCount(self, query):
        """
        Get response count of a query
        
        Parameters:
        query	 (string):	Query
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/doccount?query={query}"
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/doccount"
        response = self.client.apiCall(HttpMethods.POST, endpoint, query)
        return response


    def dumpCorrelationEngineData(self):
        """
        dump correlation engine server data
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/dump"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getStatDataFields(self):
        """
        Get fields and type
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/fields"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def markAllAsViewed(self, bodyParameter, type):
        """
        Mark all larms as acknowledged by the user
        
        Parameters:
        bodyParameter:	Description
		type	 (string):	Query filter, possible value are "active" "cleared"
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/markallasviewed?type={type}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, bodyParameter)
        return response


    def markAsViewed(self, listofalarms):
        """
        Mark alarms as acknowledged by the user
        
        Parameters:
        listofalarms:	List of alarms
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/markviewed"
        response = self.client.apiCall(HttpMethods.POST, endpoint, listofalarms)
        return response


    def getMasterManagerState(self):
        """
        Get master manager state
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/master"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getNonViewed(self):
        """
        Get alarms which are active and acknowledged by the user
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/notviewed"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatBulkAlarmRawData(self, query, scrollId, count):
        """
        Get paginated alarm raw data
        
        Parameters:
        query	 (string):	Alarm query string
		scrollId	 (string):	Query offset
		count	 (integer):	Query size
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/page?query={query}&scrollId={scrollId}&count={count}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getPostStatBulkAlarmRawData(self, alarmquerystring, scrollId, count):
        """
        Get paginated alarm raw data
        
        Parameters:
        alarmquerystring:	Alarm query string
		scrollId	 (string):	Query offset
		count	 (integer):	Query size
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/page?scrollId={scrollId}&count={count}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, alarmquerystring)
        return response


    def setPeriodicPurgeTimer(self, interval, activeTime):
        """
        Set alarm purge timer
        
        Parameters:
        interval	 (string):	Purge interval
		activeTime	 (string):	Purge activeTime
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/purgefrequency?interval={interval}&activeTime={activeTime}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatQueryFields(self):
        """
        Get query fields
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/query/fields"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getQueryConfig(self):
        """
        Get query configuration
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/query/input"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def correlAntiEntropy(self):
        """
        Reset correlation engine data
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/reset"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def restartCorrelationEngine(self):
        """
        Restart correlation engine
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/restart"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTypesAsKeyValue(self):
        """
        Gets alarm type as key value pair
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/rulenamedisplay/keyvalue"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getBySeverity(self, level, deviceId, query):
        """
        Get alarm by severity
        
        Parameters:
        level	 (array):	Alarm severity
		deviceId	 (array):	Device Id
		query	 (string):	Query filter
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/severity?severity-level={level}&deviceId={deviceId}&query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSeverityCustomHistogram(self, query):
        """
        Get alarm severity histogram
        
        Parameters:
        query	 (string):	Alarm histogram query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/severity/summary?query={query}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSeverityMappings(self):
        """
        Gets alarm severity mappings
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/severitymappings"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def startTracking(self, testName):
        """
        Start tracking events
        
        Parameters:
        testName	 (string):	test name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/starttracking/{testName}"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getStats(self):
        """
        Get alarm statistics
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/stats"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def stopTracking(self, testName):
        """
        Stop tracking events
        
        Parameters:
        testName	 (string):	test name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/stoptracking/{testName}"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getDeviceTopic(self, ip):
        """
        Get device topic state
        
        Parameters:
        ip	 (string):	Query topic
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/topic?ip={ip}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDetails(self, alarm_uuid):
        """
        Get alarm detail
        
        Parameters:
        alarm_uuid	 (string):	Alarm Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/alarms/uuid/{alarm_uuid}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateNotificationRule(self, notificationrule, ruleId):
        """
        Update notification rule
        
        Parameters:
        notificationrule:	Notification rule
		ruleId	 (string):	Rule Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/notifications/rule?ruleId={ruleId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, notificationrule)
        return response


    def createNotificationRule(self, notificationrule):
        """
        Add notification rule
        
        Parameters:
        notificationrule:	Notification rule
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/notifications/rule"
        response = self.client.apiCall(HttpMethods.POST, endpoint, notificationrule)
        return response


    def getNotificationRule(self, ruleId):
        """
        Get all rules or specific notification rule by its Id
        
        Parameters:
        ruleId	 (string):	Rule Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/notifications/rules?ruleId={ruleId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def deleteNotificationRule(self, ruleId):
        """
        Delete notification rule
        
        Parameters:
        ruleId	 (string):	Rule Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/notifications/rules?ruleId={ruleId}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


