def getDreAutoBypassStats(vmanage, ip, port, deviceId):
    """
    Get DRE auto-bypass statistics
    
    Parameters:
    ip	            (string):	Server IP
	port	        (number):	Port
	deviceId	    (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/dre/auto-bypass-stats?appqoe-dre-auto-bypass-server-ip={ip}&appqoe-dre-auto-bypass-port={port}&deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getDreStats(vmanage, deviceId):
    """
    Get DRE statistics
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/dre/dre-stats?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getDreStatus(vmanage, deviceId):
    """
    Get DRE status
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/dre/dre-status?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getDrePeerStats(vmanage, ip, peerNo, deviceId):
    """
    Get DRE peer statistics
    
    Parameters:
    ip	 (string):	System IP
	peerNo	 (number):	Peer Number
	deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/dre/peer-stats?appqoe-dre-stats-peer-system-ip={ip}&appqoe-dre-stats-peer-peer-no={peerNo}&deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
