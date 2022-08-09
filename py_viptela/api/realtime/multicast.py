def createReplicatorList(vmanage, deviceId):
    """
    Get replicator list from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/multicast/replicator?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def createRpfList(vmanage, deviceId):
    """
    Get RPF list from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/multicast/rpf?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def createTopologyList(vmanage, deviceId):
    """
    Get topology list from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/multicast/topology?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def createPimTunnelList(vmanage, deviceId):
    """
    Get PIM tunnel from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/multicast/tunnel?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
