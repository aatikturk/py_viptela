from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def createCryptoIpsecIdentity(vmanage, rTlocAddr, rTlocColor, lTlocColor, deviceId):
    """
    Get Crypto IPSEC identity entry from device
    
    Parameters:
    rTlocAddr	 (string):	Remote TLOC address
	rTlocColor	 (string):	Remote tloc color
	lTlocColor	 (string):	Local tloc color
	deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/ipsec/identity?rTlocAddr={rTlocAddr}&rTlocColor={rTlocColor}&lTlocColor={lTlocColor}&deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def createIkeInboundList(vmanage, deviceId):
    """
    Get IPsec IKE inbound connection list from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/ipsec/ike/inbound?deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def createIkeOutboundList(vmanage, deviceId):
    """
    Get IPsec IKE outbound connection list from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/ipsec/ike/outbound?deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def createIkeSessions(vmanage, rTlocAddr, rTlocColor, deviceId):
    """
    Get IPsec IKE sessions from device
    
    Parameters:
    rTlocAddr	 (string):	Remote TLOC address
	rTlocColor	 (string):	Remote tloc color
	deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/ipsec/ike/sessions?rTlocAddr={rTlocAddr}&rTlocColor={rTlocColor}&deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def createCryptov1LocalSAList(vmanage, rTlocAddr, rTlocColor, deviceId):
    """
    Get Crypto IKEv1 SA entry from device
    
    Parameters:
    rTlocAddr	 (string):	Remote TLOC address
	rTlocColor	 (string):	Remote tloc color
	deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/ipsec/ikev1?rTlocAddr={rTlocAddr}&rTlocColor={rTlocColor}&deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def createCryptov2LocalSAList(vmanage, deviceId):
    """
    Get Crypto IKEv2 SA entry from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/ipsec/ikev2?deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def createInBoundList(vmanage, rTlocAddr, rTlocColor, lTlocColor, deviceId):
    """
    Get IPsec inbound connection list from device (Real Time)
    
    Parameters:
    rTlocAddr	 (string):	Remote TLOC address
	rTlocColor	 (string):	Remote tloc color
	lTlocColor	 (string):	Local tloc color
	deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/ipsec/inbound?rTlocAddr={rTlocAddr}&rTlocColor={rTlocColor}&lTlocColor={lTlocColor}&deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def createLocalSAList(vmanage, deviceId):
    """
    Get IPsec local SA list from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/ipsec/localsa?deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def createOutBoundList(vmanage, rTlocAddr, rTlocColor, deviceId):
    """
    Get IPsec outbound connection list from device (Real Time)
    
    Parameters:
    rTlocAddr	 (string):	Remote TLOC address
	rTlocColor	 (string):	Remote tloc color
	deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/ipsec/outbound?rTlocAddr={rTlocAddr}&rTlocColor={rTlocColor}&deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def createIPsecPWKInboundConnections(vmanage, rTlocAddr, rTlocColor, lTlocColor, deviceId):
    """
    Get IPSEC pairwise key inbound entry from device
    
    Parameters:
    rTlocAddr	 (string):	Remote TLOC address
	rTlocColor	 (string):	Remote tloc color
	lTlocColor	 (string):	Local tloc color
	deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/ipsec/pwk/inbound?rTlocAddr={rTlocAddr}&rTlocColor={rTlocColor}&lTlocColor={lTlocColor}&deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def createIPsecPWKLocalSA(vmanage, rTlocAddr, rTlocColor, lTlocColor, deviceId):
    """
    Get IPSEC pairwise key local SA  entry from device
    
    Parameters:
    rTlocAddr	 (string):	Remote TLOC address
	rTlocColor	 (string):	Remote tloc color
	lTlocColor	 (string):	Local tloc color
	deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/ipsec/pwk/localsa?rTlocAddr={rTlocAddr}&rTlocColor={rTlocColor}&lTlocColor={lTlocColor}&deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def createIPsecPWKOutboundConnections(vmanage, rTlocAddr, rTlocColor, lTlocColor, deviceId):
    """
    Get IPSEC pairwise key outbound entry from device
    
    Parameters:
    rTlocAddr	 (string):	Remote TLOC address
	rTlocColor	 (string):	Remote tloc color
	lTlocColor	 (string):	Local tloc color
	deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/ipsec/pwk/outbound?rTlocAddr={rTlocAddr}&rTlocColor={rTlocColor}&lTlocColor={lTlocColor}&deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
