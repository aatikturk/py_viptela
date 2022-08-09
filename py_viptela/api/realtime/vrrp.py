def getIf(vmanage, deviceId):
    """
    Get VRRP interface list from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/vrrp?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
