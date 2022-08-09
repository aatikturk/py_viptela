def getConnList(vmanage, deviceId):
    """
    Get connection list from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/orchestrator/connections?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getConnHist(vmanage, deviceId):
    """
    Get connection history list from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/orchestrator/connectionshistory?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getLocalProperties(vmanage, deviceId):
    """
    Get local properties list from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/orchestrator/localproperties?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getRevProxy(vmanage, deviceId):
    """
    Get reverse proxy mapping from vbond
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/orchestrator/proxymapping?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getStats(vmanage, deviceId):
    """
    Get statistics from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/orchestrator/statistics?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getConnSummary(vmanage, deviceId):
    """
    Get connection summary from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/orchestrator/summary?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getValidDevicesList(vmanage, deviceId):
    """
    Get valid device list from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/orchestrator/validvedges?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getValidVManageId(vmanage, deviceId):
    """
    Get valid vManage Id from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/orchestrator/validvmanageid?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getValidVSmartsList(vmanage, deviceId):
    """
    Get valid vSmart list from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/orchestrator/validvsmarts?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
