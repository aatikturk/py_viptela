def requestDNSSecActions(vmanage, action):
    """
    Request DNS-Sec actions
    
    Parameters:
    action	 (string):	DNS-Sec action
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/fedramp/dnssec/actions?action={action}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def configureDNSSec(vmanage, request):
    """
    Configure DNS-Sec
    
    Parameters:
    request:	DNS sec config request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/fedramp/dnssec/config"
    response = vmanage.client.apiCall("POST", endpoint, request)
    return response
def getDNSSecStatus(vmanage):
    """
    Get DNS-Sec status
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/fedramp/dnssec/status"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def configFedrampMode(vmanage, mode):
    """
    Set network deployment mode
    
    Parameters:
    mode:	Network deployment mode
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/fedramp/status"
    response = vmanage.client.apiCall("POST", endpoint, mode)
    return response
def requestWazuhActions(vmanage, action):
    """
    Wazuh agent action
    
    Parameters:
    action	 (string):	Wazhuh Action
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/fedramp/wazuh/actions?action={action}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def configureWazuhClient(vmanage, wazhuhConfig):
    """
    Configure Wazuh agent
    
    Parameters:
    wazhuhConfig:	Wazhuh configuration
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/fedramp/wazuh/config"
    response = vmanage.client.apiCall("POST", endpoint, wazhuhConfig)
    return response
def getWazuhAgentStatus(vmanage):
    """
    Get Wazuh agent status
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/fedramp/wazuh/status"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
