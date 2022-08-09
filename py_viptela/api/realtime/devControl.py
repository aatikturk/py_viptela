def getAffinityConfig(vmanage, deviceId):
    """
    Get affinity config from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/control/affinity/config?deviceId={deviceId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getAffinityStatus(vmanage, deviceId):
    """
    Get affinity status from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/control/affinity/status?deviceId={deviceId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def createRealTimeConnectionList(vmanage, peerType, sysIp, deviceId):
    """
    Get connections list from device (Real Time)
    
    Parameters:
    peerType	    (string):	Peer type
	sysIp	        (string):	Peer system IP
	deviceId	    (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/control/connections?peerType={peerType}&sysIp={sysIp}&deviceId={deviceId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def createConnectionHistoryListRealTime(vmanage, peerType, sysIp, deviceId):
    """
    Get connections history list from device (Real Time)
    
    Parameters:
    peerType	 (string):	Peer type
	sysIp	 (string):	Peer system IP
	deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/control/connectionshistory?peerType={peerType}&sysIp={sysIp}&deviceId={deviceId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getTotalCountForDeviceStates(vmanage, isCached):
    """
    Get number of vedges and vsmart device in different control states
    
    Parameters:
    isCached	 (boolean):	Device State cached
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/control/count?isCached={isCached}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def createLinkList(vmanage, state):
    """
    Get connections list
    
    Parameters:
    state	 (string):	Device State
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/control/links?state={state}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def createLocalPropertiesListListRealTIme(vmanage, deviceId):
    """
    Get local properties list (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/control/localproperties?deviceId={deviceId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def networkSummary(vmanage, state):
    """
    Get list of unreachable devices
    
    Parameters:
    state	 (string):	Device State
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/control/networksummary?state={state}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getConnectionStatistics(vmanage, deviceId):
    """
    Get connection statistics from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/control/statistics?deviceId={deviceId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getLocalDeviceStatus(vmanage):
    """
    Get local device status
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/control/status"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def createConnectionsSummary(vmanage, deviceId):
    """
    Get connections summary from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/control/summary?deviceId={deviceId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getDeviceControlStatusSummary(vmanage, deviceId):
    """
    Get device control status summary
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/control/summary/device?deviceId={deviceId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def createSyncedConnectionList(vmanage, peerType, sysIp, deviceId):
    """
    Get connections list from vManage
    
    Parameters:
    peerType	 (string):	Peer type
	sysIp	 (string):	Peer system IP
	deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/control/synced/connections?peerType={peerType}&sysIp={sysIp}&deviceId={deviceId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def createLocalPropertiesSyncedList(vmanage, deviceId):
    """
    Get local properties list
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/control/synced/localproperties?deviceId={deviceId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def createWanInterfaceSyncedList(vmanage, deviceId):
    """
    Get WAN interface list
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/control/synced/waninterface?deviceId={deviceId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def createValidDevicesListRealTime(vmanage, deviceId):
    """
    Get valid device list (Real Time)
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/control/validdevices?deviceId={deviceId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getValidVManageIdRealTime(vmanage, deviceId):
    """
    Get valid vManage from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/control/validvmanageid?deviceId={deviceId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def createValidVSmartsListRealTime(vmanage, deviceId):
    """
    Get valid vSmart list from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/control/validvsmarts?deviceId={deviceId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def createWanInterfaceListList(vmanage, deviceId):
    """
    Get WAN interface list (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/control/waninterface?deviceId={deviceId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getPortHopColor(vmanage, deviceId):
    """
    Get port hop colors
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/control/waninterface/color?deviceId={deviceId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
