def getCortexStatus(vmanage):
    """
    Get Cortex List
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/cortex"
    response = vmanage.apiCall("GET", endpoint)
    return response

def authAzureCredAndAdd(vmanage, credential):
    """
    Authenticate Cloud Account Credentials
    
    Parameters:
    credential:	Credential
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/cortex/cloud/authenticate"
    response = vmanage.apiCall("POST", endpoint, credential)
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
    
    endpoint = f"dataservice/template/cortex/map?accountid={accountid}&cloudregion={cloudregion}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def syncWanRG(vmanage, wanRG):
    """
    Sync WAN Resource Groups
    
    Parameters:
    wanRG:	WAN resource group
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/cortex/sync"
    response = vmanage.apiCall("POST", endpoint, wanRG)
    return response

def getWanRG(vmanage, accountid):
    """
    Get WAN Resource Groups
    
    Parameters:
    accountid	 (string):	Account Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/cortex/wanrg?accountid={accountid}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def editWanRG(vmanage, wanRG):
    """
    Edit WAN Resource Groups
    
    Parameters:
    wanRG:	WAN resource group
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/cortex/wanrg"
    response = vmanage.apiCall("PUT", endpoint, wanRG)
    return response

def saveWanRG(vmanage, wanRG):
    """
    Create WAN Resource Groups
    
    Parameters:
    wanRG:	WAN resource group
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/cortex/wanrg"
    response = vmanage.apiCall("POST", endpoint, wanRG)
    return response

def deleteWanRG(vmanage, wanRG):
    """
    Delete WAN Resource Groups
    
    Parameters:
    wanRG:	WAN resource group
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/cortex/wanrg"
    response = vmanage.apiCall("DELETE", endpoint, wanRG)
    return response
