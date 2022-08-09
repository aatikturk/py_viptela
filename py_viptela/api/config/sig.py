def getSigTunnelList(vmanage, deviceId):
    """
    Get Secure Internet Gateway Tunnel List
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/cloudx/sig_tunnels?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
