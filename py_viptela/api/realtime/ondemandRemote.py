def get(vmanage, deviceId):
    """
    Get on-demand remote (Real Time)
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/ondemand/remote?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
