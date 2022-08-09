def getCflowdDPIDeviceFieldJSON(vmanage, isDeviceDashBoard):
    """
    Get Cflowd DPI query field JSON
    
    Parameters:
    isDeviceDashBoard	 (boolean):	Flag whether it is device dashboard request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/cflowd/application/fields?isDeviceDashBoard={isDeviceDashBoard}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getCollectorList(vmanage, deviceId):
    """
    Get cflowd collector list from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/cflowd/collector?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getDPIFieldJSON(vmanage, isDeviceDashBoard):
    """
    Get CflowdvDPI query field JSON
    
    Parameters:
    isDeviceDashBoard	 (boolean):	Flag whether it is device dashboard request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/cflowd/device/fields?isDeviceDashBoard={isDeviceDashBoard}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getFlows(vmanage, vpnId, src, dest, deviceId):
    """
    Get list of cflowd flows from device
    
    Parameters:
    vpnId	        (string):	VPN Id
	src	            (string):	Source IP
	dest	        (string):	Destination IP
	deviceId	    (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/cflowd/flows?vpn-id={vpnId}&src-ip={src}&dest-ip={dest}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getFlowsCount(vmanage, vpnId, src, dest, deviceId):
    """
    Get cflowd flow count from device
    
    Parameters:
    vpnId	        (string):	VPN Id
	src	            (string):	Source IP
	dest	        (string):	Destination IP
	deviceId	    (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/cflowd/flows-count?vpn-id={vpnId}&src-ip={src}&dest-ip={dest}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getFnFCacheStats(vmanage, deviceId):
    """
    Get FnF cache stats from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/cflowd/fnf/cache-stats?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getFnFExportClientStats(vmanage, deviceId):
    """
    Get FnF export client stats from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/cflowd/fnf/export-client-stats?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getFnFExportStats(vmanage, deviceId):
    """
    Get FnF export stats from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/cflowd/fnf/export-stats?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getFnf(vmanage, deviceId):
    """
    Get FnF from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/cflowd/fnf/flow-monitor?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getFnFMonitorStats(vmanage, deviceId):
    """
    Get FnF monitor stats from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/cflowd/fnf/monitor-stats?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getStatistics(vmanage, deviceId):
    """
    Get cflowd statistics from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/cflowd/statistics?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getTemplate(vmanage, deviceId):
    """
    Get cflowd template from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/cflowd/template?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
