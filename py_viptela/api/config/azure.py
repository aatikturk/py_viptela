def getCortexStatus(vmanage):
    """
    Get Cortex List
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cortex"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def authAzureCredAndAdd(vmanage, credential):
    """
    Authenticate Cloud Account Credentials
    
    Parameters:
    credential:	Credential
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cortex/cloud/authenticate"
    response = vmanage.client.apiCall("POST", endpoint, credential)
    return response

def getMappedWanRG(vmanage, accountid, cloudregion):
    """
    Get Mapped WAN Resource Groups
    
    Parameters:
    accountid	 (string):	Account Id
	cloudregion	 (string):	Cloud region
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cortex/map?accountid={accountid}&cloudregion={cloudregion}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def syncWanRG(vmanage, wanRG):
    """
    Sync WAN Resource Groups
    
    Parameters:
    wanRG:	WAN resource group
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cortex/sync"
    response = vmanage.client.apiCall("POST", endpoint, wanRG)
    return response

def getWanRG(vmanage, accountid):
    """
    Get WAN Resource Groups
    
    Parameters:
    accountid	 (string):	Account Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cortex/wanrg?accountid={accountid}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def editWanRG(vmanage, wanRG):
    """
    Edit WAN Resource Groups
    
    Parameters:
    wanRG:	WAN resource group
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cortex/wanrg"
    response = vmanage.client.apiCall("PUT", endpoint, wanRG)
    return response

def saveWanRG(vmanage, wanRG):
    """
    Create WAN Resource Groups
    
    Parameters:
    wanRG:	WAN resource group
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cortex/wanrg"
    response = vmanage.client.apiCall("POST", endpoint, wanRG)
    return response

def deleteWanRG(vmanage, wanRG):
    """
    Delete WAN Resource Groups
    
    Parameters:
    wanRG:	WAN resource group
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cortex/wanrg"
    response = vmanage.client.apiCall("DELETE", endpoint, wanRG)
    return response
