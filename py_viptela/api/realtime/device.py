def getV6Data(vmanage, deviceId):
    """
    Get ipv6 data from device
    
    Parameters:
    Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/ipv6/nd6?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
