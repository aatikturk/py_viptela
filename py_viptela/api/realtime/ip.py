def getFib(vmanage, vpnId, af, prefix, tloc, color, deviceId):
    """
    Get FIB list from device (Real Time)
    
    Parameters:
    vpnId	 (string):	VPN Id
	af	 (string):	Address family
	prefix	 (string):	IP prefix
	tloc	 (string):	tloc IP
	color	 (string):	tloc color
	deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/ip/fib?vpnId={vpnId}&af={af}&prefix={prefix}&tloc={tloc}&color={color}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getIetfRouting(vmanage, instanceName, af, outIf, srcProto, nextHop, deviceId):
    """
    Get ietf routing list from device
    
    Parameters:
    instanceName	 (string):	VPN Id
	af	 (string):	Address family
	outIf	 (string):	Outgoing Interface
	srcProto	 (string):	Source Protocol
	nextHop	 (string):	Next Hop Address
	deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/ip/ipRoutes?instanceName={instanceName}&af={af}&outIf={outIf}&srcProto={srcProto}&nextHop={nextHop}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getIPMfibOil(vmanage, deviceId):
    """
    Get IP MFIB OIL list from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/ip/mfiboil?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getIPMfibStats(vmanage, deviceId):
    """
    Get IP MFIB statistics list from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/ip/mfibstats?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getIPMfibSummary(vmanage, deviceId):
    """
    Get IP MFIB summary list from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/ip/mfibsummary?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getNatFilter(vmanage, natVpnId, natIfname, privateSrcAddr, proto, deviceId):
    """
    Get NAT filter list from device
    
    Parameters:
    natVpnId	 (string):	NAT VPN Id
	natIfname	 (string):	NAT interface name
	privateSrcAddr	 (string):	Private source address
	proto	 (string):	Protocol
	deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/ip/nat/filter?natVpnId={natVpnId}&natIfname={natIfname}&privateSrcAddr={privateSrcAddr}&proto={proto}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getNatInterface(vmanage, deviceId):
    """
    Get NAT interface list from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/ip/nat/interface?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getNatIfStats(vmanage, deviceId):
    """
    Get NAT interface statistics list from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/ip/nat/interfacestatistics?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getNatTranslations(vmanage, deviceId):
    """
    Get NAT translation list from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/ip/nat/translation?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getNat64Translations(vmanage, deviceId):
    """
    Get NAT64 interface list from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/ip/nat64/translation?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getRouteTable(vmanage, vpnId, af, prefix, protocol, deviceId):
    """
    Get route table list from device (Real Time)
    
    Parameters:
    vpnId	 (string):	VPN Id
	af	 (string):	Address family
	prefix	 (string):	IP prefix
	protocol	 (string):	IP protocol
	deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/ip/routetable?vpnId={vpnId}&af={af}&prefix={prefix}&protocol={protocol}&deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
