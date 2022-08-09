def getFlowCount(vmanage, deviceId):
    """
    Get App log flows count from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/app/log/flow-count?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getFlows(vmanage, deviceId):
    """
    Get App log flows from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/app/log/flows?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
