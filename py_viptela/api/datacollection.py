def createStats(vmanage, statsquery):
    """
    Get statistics data
    
    Parameters:
    statsquery:	Stats query
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/dca/analytics"
    response = vmanage.apiCall("PUT", endpoint, statsquery)
    return response
def getAllStatsDataDCA(vmanage, statssetting):
    """
    Get all statistics setting data
    
    Parameters:
    statssetting:	Stats setting
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/dca/analytics/all"
    response = vmanage.apiCall("POST", endpoint, statssetting)
    return response
def getAccessToken(vmanage):
    """
    Get DCA access token
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/dca/cloudservices/accesstoken"
    response = vmanage.apiCall("GET", endpoint)
    return response
def storeAccessToken(vmanage, dcaaccesstoken):
    """
    Set DCA access token
    
    Parameters:
    dcaaccesstoken:	DCA access token
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/dca/cloudservices/accesstoken"
    response = vmanage.apiCall("POST", endpoint, dcaaccesstoken)
    return response
def generateAlarm(vmanage, msg):
    """
    Generate DCA alarms
    
    Parameters:
    msg:	DCA alarm message
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/dca/cloudservices/alarm"
    response = vmanage.apiCall("POST", endpoint, msg)
    return response
def getIdToken(vmanage):
    """
    Get DCA Id token
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/dca/cloudservices/idtoken"
    response = vmanage.apiCall("GET", endpoint)
    return response
def storeIdToken(vmanage, token):
    """
    Set DCA Id token
    
    Parameters:
    token:	DCA Id token
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/dca/cloudservices/idtoken"
    response = vmanage.apiCall("POST", endpoint, token)
    return response
def getTelemetrySettings(vmanage):
    """
    Get DCA telemetry settings
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/dca/cloudservices/telemetry"
    response = vmanage.apiCall("GET", endpoint)
    return response
def generateDCADeviceStateData(vmanage, query, state_data_type):
    """
    Get device state data
    
    Parameters:
    query:	Query string
	state_data_type	 (string):	Device state data
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/dca/data/device/state/{state_data_type}"
    response = vmanage.apiCall("POST", endpoint, query)
    return response
def generateDCADeviceStatisticsData(vmanage, query, dataType):
    """
    Get device statistics data
    
    Parameters:
    query:	Query string
	dataType	 (string):	Device statistics data
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/dca/data/device/statistics/{dataType}"
    response = vmanage.apiCall("POST", endpoint, query)
    return response
def getDCATenantOwners(vmanage):
    """
    Get DCA tenant owners
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/dca/dcatenantowners"
    response = vmanage.apiCall("GET", endpoint)
    return response
def listAllDevicesDCA(vmanage, query):
    """
    Get all devices
    
    Parameters:
    query:	Query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/dca/device"
    response = vmanage.apiCall("POST", endpoint, query)
    return response
def getCrashLogs(vmanage, query):
    """
    Get crash log
    
    Parameters:
    query:	Query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/dca/device/crashlog/details"
    response = vmanage.apiCall("POST", endpoint, query)
    return response
def getCrashLogsSynced(vmanage, deviceId):
    """
    Get device crash log
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/dca/device/crashlog/synced?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getCloudServicesConfigurationDCA(vmanage):
    """
    Get DCA cloud service configuration
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/dca/settings/configuration/cloudservices/dca"
    response = vmanage.apiCall("GET", endpoint)
    return response
def createDCAAnalyticsDataFile(vmanage, query, type):
    """
    Create analytics config data
    
    Parameters:
    query:	Query string
	type	 (string):	Data type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/dca/settings/configuration/{type}/dca"
    response = vmanage.apiCall("POST", endpoint, query)
    return response
def getStatsDBIndexStatus(vmanage, statssetting):
    """
    Get statistics setting status
    
    Parameters:
    statssetting:	Stats setting
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/dca/statistics/settings/status"
    response = vmanage.apiCall("POST", endpoint, statssetting)
    return response
def getDevicesDetailsDCA(vmanage, query):
    """
    Get device details
    
    Parameters:
    query:	Query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/dca/system/device"
    response = vmanage.apiCall("POST", endpoint, query)
    return response
def getDCAAttachedConfigToDevice(vmanage, query):
    """
    Get attached config to device
    
    Parameters:
    query:	Query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/dca/template/device/config/attachedconfig"
    response = vmanage.apiCall("POST", endpoint, query)
    return response
def getTemplatePolicyDefinitionsDCA(vmanage, query):
    """
    Get template policy definitions
    
    Parameters:
    query:	Query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/dca/template/policy/definition/approute"
    response = vmanage.apiCall("POST", endpoint, query)
    return response
def getVPNListsDCA(vmanage, query):
    """
    Get VPN details
    
    Parameters:
    query:	Query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/dca/template/policy/list/vpn"
    response = vmanage.apiCall("POST", endpoint, query)
    return response
def getVedgeTemplateListDCA(vmanage, query):
    """
    Get vEdge template list
    
    Parameters:
    query:	Query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/dca/template/policy/vedge"
    response = vmanage.apiCall("POST", endpoint, query)
    return response
def getVsmartTemplateListDCA(vmanage, query):
    """
    Get vSmart template list
    
    Parameters:
    query:	Query string
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/dca/template/policy/vsmart"
    response = vmanage.apiCall("POST", endpoint, query)
    return response
