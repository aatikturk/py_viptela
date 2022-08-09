def getInterface(vmanage, vpnId, ifname, mac, deviceId):
    """
    Get IPv6 Neighbors from device (Real Time)
    
    Parameters:
    vpnId	        (string):	VPN Id
	ifname	        (string):	Interface name
	mac	            (string):	Mac address
	deviceId	    (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/ndv6?vpn-id={vpnId}&if-name={ifname}&mac={mac}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
