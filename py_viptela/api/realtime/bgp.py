def getNeighbors(vmanage, vpnId, peerAddr, asNo, deviceId):
    """
    Get BGP neighbors list (Real Time)
    
    Parameters:
    vpnId	 (string):	VPN Id
	peerAddr	 (string):	Peer address
	asNo	 (string):	AS number
	deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/bgp/neighbors?vpnId={vpnId}&peerAddr={peerAddr}&as={asNo}&deviceId={deviceId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def createBGPRoutesList(vmanage, vpnId, prefix, nexthop, deviceId):
    """
    Get BGP routes list (Real Time)
    
    Parameters:
    vpnId	 (string):	VPN Id
	prefix	 (string):	IP prefix
	nexthop	 (string):	Next hop
	deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/bgp/routes?vpnId={vpnId}&prefix={prefix}&nexthop={nexthop}&deviceId={deviceId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def createBGPSummary(vmanage, deviceId):
    """
    Get BGP summary (Real Time)
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/bgp/summary?deviceId={deviceId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
