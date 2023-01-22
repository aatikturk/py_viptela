def getInterface(vmanage, deviceId, vpnId=None, ifname=None, af=None):
    """
    Get device interfaces
    
    Parameters:
    vpnId	        (string):	VPN Id
	ifname	        (string):	IF Name
	af  	        (string):	AF Type
	deviceId	    (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/interface?vpn-id={vpnId}&ifname={ifname}&af-type={af}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getInterfaceByDeviceIp(vmanage, deviceId):
    """
    Get device interfaces
    
    Parameters:
	deviceId	    (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/interface?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getARPStats(vmanage, vpnId, ifname, af, deviceId):
    """
    Get interface ARP statistics
    
    Parameters:
    vpnId	        (string):	VPN Id
	ifname	        (string):	IF Name
	af  	        (string):	AF Type
	deviceId	    (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/interface/arp_stats?vpn-id={vpnId}&ifname={ifname}&af-type={af}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getErrorStats(vmanage, vpnId, ifname, af, deviceId):
    """
    Get interface error stats
    
    Parameters:
    vpnId	        (string):	VPN Id
	ifname	        (string):	IF Name
	af  	        (string):	AF Type
	deviceId	    (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/interface/error_stats?vpn-id={vpnId}&ifname={ifname}&af-type={af}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getV6Stats(vmanage, vpnId, ifname, af, deviceId):
    """
    Get interface IPv6 stats
    
    Parameters:
    vpnId	        (string):	VPN Id
	ifname	        (string):	IF Name
	af  	        (string):	AF Type
	deviceId	    (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/interface/ipv6Stats?vpn-id={vpnId}&ifname={ifname}&af-type={af}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getPktSizes(vmanage, vpnId, ifname, af, deviceId):
    """
    Get interface packet size
    
    Parameters:
    vpnId	        (string):	VPN Id
	ifname	        (string):	IF Name
	af  	        (string):	AF Type
	deviceId	    (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/interface/pkt_size?vpn-id={vpnId}&ifname={ifname}&af-type={af}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getPortStats(vmanage, vpnId, ifname, af, deviceId):
    """
    Get interface port stats
    
    Parameters:
    vpnId	        (string):	VPN Id
	ifname	        (string):	IF Name
	af  	        (string):	AF Type
	deviceId	    (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/interface/port_stats?vpn-id={vpnId}&ifname={ifname}&af-type={af}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getQosStats(vmanage, vpnId, ifname, af, deviceId):
    """
    Get interface QOS stats
    
    Parameters:
    vpnId	        (string):	VPN Id
	ifname	        (string):	IF Name
	af  	        (string):	AF Type
	deviceId	    (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/interface/qosStats?vpn-id={vpnId}&ifname={ifname}&af-type={af}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getQueueStats(vmanage, vpnId, ifname, af, deviceId):
    """
    Get interface queue stats
    
    Parameters:
    vpnId	        (string):	VPN Id
	ifname	        (string):	IF Name
	af  	        (string):	AF Type
	deviceId	    (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/interface/queue_stats?vpn-id={vpnId}&ifname={ifname}&af-type={af}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getDeviceSerialInterface(vmanage, vpnId, ifname, af, deviceId):
    """
    Get serial interface
    
    Parameters:
    vpnId	        (string):	VPN Id
	ifname	        (string):	IF Name
	af  	        (string):	AF Type
	deviceId	    (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/interface/serial?vpn-id={vpnId}&ifname={ifname}&af-type={af}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getStats(vmanage, vpnId, ifname, af, deviceId):
    """
    Get interface stats
    
    Parameters:
    vpnId	        (string):	VPN Id
	ifname	        (string):	IF Name
	af  	        (string):	AF Type
	deviceId	    (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/interface/stats?vpn-id={vpnId}&ifname={ifname}&af-type={af}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getSyncedInterface(vmanage, deviceId, vpnId=None, ifname=None, af=None):
    """
    Get device interfaces synchronously
    
    Parameters:
    vpnId	        (string):	VPN Id
	ifname	        (string):	IF Name
	af  	        (string):	AF Type
	deviceId	    (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    endpoint = f"dataservice/device/interface/synced?deviceId={deviceId}"
    
    if vpnId:
        endpoint = f"{endpoint}&vpn-id={vpnId}"
    if ifname:
        endpoint = f"{endpoint}&ifname={ifname}"
    if af:
        endpoint = f"{endpoint}&af={af}"
    
    response = vmanage.apiCall("GET", endpoint)
    return response
def trustsec(vmanage, deviceId):
    """
    Get policy filter memory usage from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/interface/trustsec?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getInterfaceVPN(vmanage, deviceId):
    """
    Get device interfaces per VPN
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/interface/vpn?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
