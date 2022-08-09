def getCloudXStatus(vmanage):
    """
    Get CloudX feature list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cloudx"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
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
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cloudx/addcloudx/{type}"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, cloudx)
    return response

def getAttachedClientList(vmanage):
    """
    Get attached client site list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cloudx/attachedclient"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getAttachedDiaList(vmanage):
    """
    Get attached Dia site list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cloudx/attacheddia"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getAttachedGwList(vmanage):
    """
    Get attached gateway list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cloudx/attachedgateway"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getCloudXAvailableApps(vmanage):
    """
    Get CloudX available apps list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cloudx/availableapps"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getSiteList(vmanage):
    """
    Get site list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cloudx/clientlist"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getDiaList(vmanage):
    """
    Get Dia site list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cloudx/dialist"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getGwList(vmanage):
    """
    Get gateway list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cloudx/gatewaylist"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def addCloudxInterfaces(vmanage, cloudx):
    """
    Enable cloudx gateway
    
    Parameters:
    cloudx:	Cloudx
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cloudx/interfaces"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, cloudx)
    return response

def getApps(vmanage):
    """
    Get apps and vpns
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cloudx/manage/apps"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def editApps(vmanage, appVPN):
    """
    Edit apps and vpns
    
    Parameters:
    appVPN:	Cloudx apps and vpns
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cloudx/manage/apps"
    response = vmanage.client.apiCall(vmanage.PUT, endpoint, appVPN)
    return response

def addApps(vmanage, appVPN):
    """
    Add apps and vpns
    
    Parameters:
    appVPN:	Cloudx apps and vpns
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cloudx/manage/apps"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, appVPN)
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
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cloudx/status?appName={appName}&vpnId={vpnId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
