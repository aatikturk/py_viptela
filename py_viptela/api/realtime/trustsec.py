def getCtsPac(vmanage, deviceId):
    """
    get Cisco TrustSec PAC information from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/ctsPac?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getEnvData(vmanage, deviceId):
    """
    get Cisco TrustSec Environment Data information from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/environmentData?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getRadiusServer(vmanage, deviceId):
    """
    get Cisco TrustSec Environment Data Radius Server list from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/environmentData/radiusServer?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getRBCounters(vmanage, deviceId):
    """
    get Cisco TrustSec Role Based Counters information from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/roleBasedCounters?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getRBv6Counters(vmanage, deviceId):
    """
    get Cisco TrustSec Role Based Ipv6 Counters information from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/roleBasedIpv6Counters?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getRBv6Perms(vmanage, deviceId):
    """
    get Cisco TrustSec Role Based ipv6 Permissions information from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/roleBasedIpv6Permissions?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getRBPermissions(vmanage, deviceId):
    """
    get Cisco TrustSec Role Based Permissions information from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/roleBasedPermissions?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getRBSgtMap(vmanage, deviceId):
    """
    get Cisco TrustSec Role Based SGT Map information from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/roleBasedSgtMap?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getSxpConnections(vmanage, deviceId):
    """
    get Cisco TrustSec SXP Connections information from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/sxpConnections?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
