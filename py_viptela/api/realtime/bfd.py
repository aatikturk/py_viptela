def getHistoryList(vmanage, systemIp, color, deviceId):
    """
    Get BFD session history from device (Real Time)
    
    Parameters:
    systemIp	    (string):	System IP
	color	        (string):	Remote color
	deviceId	    (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/bfd/history?system-ip={systemIp}&color={color}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getLinkList(vmanage, state):
    """
    Get list of BFD connections
    
    Parameters:
    state	 (string):	Device state
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/bfd/links?state={state}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getSessions(vmanage, systemIp, color, localColor, deviceId):
    """
    Get list of BFD sessions from vManage (Real Time)
    
    Parameters:
    systemIp	    (string):	System IP
	color	        (string):	Remote color
	local-color	    (string):	Source color
	deviceId	    (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/bfd/sessions?system-ip={systemIp}&color={color}&local-color={localColor}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getSiteStateDetail(vmanage):
    """
    Get detailed BFD site details
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/bfd/sites/detail"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getSitesSummary(vmanage, isCached, vpnId):
    """
    Get BFD site summary
    
    Parameters:
    isCached	 (boolean):	Flag for caching
	vpnId	 (array):	Filter VPN
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/bfd/sites/summary?isCached={isCached}&vpnId={vpnId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getStateSummary(vmanage, deviceId):
    """
    Get device BFD state summary
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/bfd/state/device?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getStateSummaryTloc(vmanage, deviceId):
    """
    Get device BFD state summary with tloc color
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/bfd/state/device/tloc?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getStatus(vmanage):
    """
    Get device BFD status
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/bfd/status"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getSummary(vmanage, deviceId):
    """
    Get BFD summary from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/bfd/summary?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getStatusSummary(vmanage, deviceId):
    """
    Get device BFD status summary
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/bfd/summary/device?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getSyncSession(vmanage, systemIp, color, localColor, deviceId):
    """
    Get list of BFD sessions from vManage synchronously
    
    Parameters:
    systemIp	    (string):	System IP
	color	        (string):	Remote color
	localColor	    (string):	Source color
	deviceId	    (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/bfd/synced/sessions?system-ip={systemIp}&color={color}&local-color={localColor}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getTLOCSummary(vmanage, deviceId):
    """
    Get TLOC summary from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/bfd/tloc?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
