from query_builder import Builder
import HttpMethods

class Agent(object):
    """
    Data Collection Agent API
    
    Implements GET POST DEL PUT methods for DataCollectionAgent endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def createStats(self, statsquery):
        """
        Get statistics data
        
        Parameters:
        statsquery:	Stats query
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/analytics"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, statsquery)
        return response


    def getAllStatsDataDCA(self, statssetting):
        """
        Get all statistics setting data
        
        Parameters:
        statssetting:	Stats setting
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/analytics/all"
        response = self.client.apiCall(HttpMethods.POST, endpoint, statssetting)
        return response


    def getAccessToken(self):
        """
        Get DCA access token
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/cloudservices/accesstoken"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def storeAccessToken(self, dcaaccesstoken):
        """
        Set DCA access token
        
        Parameters:
        dcaaccesstoken:	DCA access token
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/cloudservices/accesstoken"
        response = self.client.apiCall(HttpMethods.POST, endpoint, dcaaccesstoken)
        return response


    def generateAlarm(self, dcaalarmmessage):
        """
        Generate DCA alarms
        
        Parameters:
        dcaalarmmessage:	DCA alarm message
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/cloudservices/alarm"
        response = self.client.apiCall(HttpMethods.POST, endpoint, dcaalarmmessage)
        return response


    def getIdToken(self):
        """
        Get DCA Id token
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/cloudservices/idtoken"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def storeIdToken(self, dcaidtoken):
        """
        Set DCA Id token
        
        Parameters:
        dcaidtoken:	DCA Id token
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/cloudservices/idtoken"
        response = self.client.apiCall(HttpMethods.POST, endpoint, dcaidtoken)
        return response


    def getTelemetrySettings(self):
        """
        Get DCA telemetry settings
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/cloudservices/telemetry"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def generateDCADeviceStateData(self, querystring, state_data_type):
        """
        Get device state data
        
        Parameters:
        querystring:	Query string
		state_data_type	 (string):	Device state data
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/data/device/state/{state_data_type}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, querystring)
        return response


    def generateDCADeviceStatisticsData(self, querystring, stats_data_type):
        """
        Get device statistics data
        
        Parameters:
        querystring:	Query string
		stats_data_type	 (string):	Device statistics data
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/data/device/statistics/{stats_data_type}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, querystring)
        return response


    def getDCATenantOwners(self):
        """
        Get DCA tenant owners
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/dcatenantowners"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def listAllDevicesDCA(self, querystring):
        """
        Get all devices
        
        Parameters:
        querystring:	Query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/device"
        response = self.client.apiCall(HttpMethods.POST, endpoint, querystring)
        return response


    def getCrashLogs(self, querystring):
        """
        Get crash log
        
        Parameters:
        querystring:	Query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/device/crashlog/details"
        response = self.client.apiCall(HttpMethods.POST, endpoint, querystring)
        return response


    def getCrashLogsSynced(self, deviceId):
        """
        Get device crash log
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/device/crashlog/synced?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCloudServicesConfigurationDCA(self):
        """
        Get DCA cloud service configuration
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/settings/configuration/cloudservices/dca"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createDCAAnalyticsDataFile(self, querystring, type):
        """
        Create analytics config data
        
        Parameters:
        querystring:	Query string
		type	 (string):	Data type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/settings/configuration/{type}/dca"
        response = self.client.apiCall(HttpMethods.POST, endpoint, querystring)
        return response


    def getStatsDBIndexStatus(self, statssetting):
        """
        Get statistics setting status
        
        Parameters:
        statssetting:	Stats setting
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/statistics/settings/status"
        response = self.client.apiCall(HttpMethods.POST, endpoint, statssetting)
        return response


    def getDevicesDetailsDCA(self, querystring):
        """
        Get device details
        
        Parameters:
        querystring:	Query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/system/device"
        response = self.client.apiCall(HttpMethods.POST, endpoint, querystring)
        return response


    def getDCAAttachedConfigToDevice(self, querystring):
        """
        Get attached config to device
        
        Parameters:
        querystring:	Query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/template/device/config/attachedconfig"
        response = self.client.apiCall(HttpMethods.POST, endpoint, querystring)
        return response


    def getTemplatePolicyDefinitionsDCA(self, querystring):
        """
        Get template policy definitions
        
        Parameters:
        querystring:	Query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/template/policy/definition/approute"
        response = self.client.apiCall(HttpMethods.POST, endpoint, querystring)
        return response


    def getVPNListsDCA(self, querystring):
        """
        Get VPN details
        
        Parameters:
        querystring:	Query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/template/policy/list/vpn"
        response = self.client.apiCall(HttpMethods.POST, endpoint, querystring)
        return response


    def getVedgeTemplateListDCA(self, querystring):
        """
        Get vEdge template list
        
        Parameters:
        querystring:	Query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/template/policy/vedge"
        response = self.client.apiCall(HttpMethods.POST, endpoint, querystring)
        return response


    def getVsmartTemplateListDCA(self, querystring):
        """
        Get vSmart template list
        
        Parameters:
        querystring:	Query string
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/dca/template/policy/vsmart"
        response = self.client.apiCall(HttpMethods.POST, endpoint, querystring)
        return response


