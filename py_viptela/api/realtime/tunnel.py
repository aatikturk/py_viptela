def getBfdStats(vmanage, deviceId):
    """
    Get tunnel BFD statistics all devices
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/tunnel/bfd_statistics?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getFecStats(vmanage, deviceId):
    """
    Get tunnel fec statistics
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/tunnel/fec_statistics?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getGreKeepalives(vmanage, deviceId):
    """
    Get GRE keep alive information
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/tunnel/gre-keepalives?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getIpsecStats(vmanage, deviceId):
    """
    Get tunnel IPSec statistics all devices
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/tunnel/ipsec_statistics?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getPacketDuplicateStats(vmanage, deviceId):
    """
    Get tunnel statistics packet duplication statistics
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/tunnel/packet-duplicate?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getStats(vmanage, deviceId):
    """
    Get tunnel statistics all devices
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/tunnel/statistics?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
