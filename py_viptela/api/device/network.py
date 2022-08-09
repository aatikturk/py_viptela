def getVmanageControlStatus(vmanage, isCached, vpnId):
    """
    Retrieve vManage control status
    
    Parameters:
    isCached	 (boolean):	Is cached flag
	vpnId	 (array):	VPN Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/network/connectionssummary?isCached={isCached}&vpnId={vpnId}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getRebootCount(vmanage, isCached):
    """
    Retrieve reboot count
    
    Parameters:
    isCached	 (boolean):	Is cached flag
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/network/issues/rebootcount?isCached={isCached}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getNetworkIssuesSummary(vmanage):
    """
    Retrieve network issues summary
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/network/issues/summary"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getNetworkStatusSummary(vmanage):
    """
    Retrieve network status summary
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/network/status"
    response = vmanage.apiCall("GET", endpoint)
    return response
