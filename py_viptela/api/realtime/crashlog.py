def getLogs(vmanage, deviceId):
    """
    Get device crash logs from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/crashlog?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getAllLogs(vmanage):
    """
    Get device crash logs for all device
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/crashlog/details"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getInfo(vmanage, deviceId, filename):
    """
    Get device crash info from device
    
    Parameters:
    deviceId	 (string):	Device IP
	filename	 (string):	Crash file name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/crashlog/log?deviceId={deviceId}&filename={filename}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getLogsSynced(vmanage, deviceId):
    """
    Get device crash logs synchronously from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/crashlog/synced?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
