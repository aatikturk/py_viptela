def getPolicedInterface(vmanage, deviceId):
    """
    Get policed interface list from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/policer?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
