def createSDAConfig(vmanage, config, partnerId):
    """
    Create SDA enabled device
    
    Parameters:
    config:	Device SDA configuration
	partnerId	 (string):	Partner Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/partner/dnac/sda/config/{partnerId}"
    response = vmanage.apiCall("POST", endpoint, config)
    return response
def getSDAEnabledDevices(vmanage, partnerId):
    """
    Get SDA enabled devices
    
    Parameters:
    partnerId	 (string):	Partner Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/partner/dnac/sda/device/{partnerId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getDeviceDetails(vmanage, partnerId, uuid):
    """
    Get SDA enabled devices detail
    
    Parameters:
    partnerId	 (string):	Partner Id
	uuid	 (string):	Device uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/partner/dnac/sda/device/{partnerId}/{uuid}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def createSDAConfigFromNetconf(vmanage, config, partnerId):
    """
    Create SDA enabled device from Netconf
    
    Parameters:
    config:	Device SDA configuration
	partnerId	 (string):	Partner Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/partner/dnac/sda/netconfconfig/{partnerId}"
    response = vmanage.apiCall("POST", endpoint, config)
    return response
def getSitesForPartner(vmanage, partnerId):
    """
    Get SDA enabled devices
    
    Parameters:
    partnerId	 (string):	Partner Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/partner/dnac/sda/site/{partnerId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getOverlayVPNList(vmanage):
    """
    Get Overlay VPN list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/partner/dnac/sda/vpn"
    response = vmanage.apiCall("GET", endpoint)
    return response
