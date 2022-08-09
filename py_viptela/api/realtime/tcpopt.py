def getActiveTCPFlows(vmanage, deviceId):
    """
    Get TCP optimized active flows from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/tcpopt/activeflows?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getExpiredTCPFlows(vmanage, deviceId):
    """
    Get TCP optimized expired flows from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/tcpopt/expiredflows?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getTCPSummary(vmanage, deviceId):
    """
    Get TCP optimization summary from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/tcpopt/summary?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
