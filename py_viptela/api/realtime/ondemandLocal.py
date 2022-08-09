def get(vmanage, deviceId):
    """
    Get on-demand local (Real Time)
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/ondemand/local?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
