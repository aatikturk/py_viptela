def getCloudXStatus(vmanage):
    """
    Get CloudX feature list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/cloudx"
    response = vmanage.apiCall("GET", endpoint)
    return response

def addCloudxType(vmanage, cloudx, type):
    """
    Add cloudx gateway
    
    Parameters:
    cloudx:	Cloudx
	type	 (string):	Cloudx type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/cloudx/addcloudx/{type}"
    response = vmanage.apiCall("POST", endpoint, cloudx)
    return response

def getAttachedClientList(vmanage):
    """
    Get attached client site list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/cloudx/attachedclient"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getAttachedDiaList(vmanage):
    """
    Get attached Dia site list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/cloudx/attacheddia"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getAttachedGwList(vmanage):
    """
    Get attached gateway list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/cloudx/attachedgateway"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getCloudXAvailableApps(vmanage):
    """
    Get CloudX available apps list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/cloudx/availableapps"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getSiteList(vmanage):
    """
    Get site list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/cloudx/clientlist"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getDiaList(vmanage):
    """
    Get Dia site list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/cloudx/dialist"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getGwList(vmanage):
    """
    Get gateway list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/cloudx/gatewaylist"
    response = vmanage.apiCall("GET", endpoint)
    return response

def addCloudxInterfaces(vmanage, cloudx):
    """
    Enable cloudx gateway
    
    Parameters:
    cloudx:	Cloudx
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/cloudx/interfaces"
    response = vmanage.apiCall("POST", endpoint, cloudx)
    return response

def getApps(vmanage):
    """
    Get apps and vpns
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/cloudx/manage/apps"
    response = vmanage.apiCall("GET", endpoint)
    return response

def editApps(vmanage, appVPN):
    """
    Edit apps and vpns
    
    Parameters:
    appVPN:	Cloudx apps and vpns
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/cloudx/manage/apps"
    response = vmanage.apiCall("PUT", endpoint, appVPN)
    return response

def addApps(vmanage, appVPN):
    """
    Add apps and vpns
    
    Parameters:
    appVPN:	Cloudx apps and vpns
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/cloudx/manage/apps"
    response = vmanage.apiCall("POST", endpoint, appVPN)
    return response

def sitePerApp(vmanage, appName, vpnId):
    """
    Get sites per application per vpn
    
    Parameters:
    appName	 (string):	App name
	vpnId	 (integer):	VPN Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/cloudx/status?appName={appName}&vpnId={vpnId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
