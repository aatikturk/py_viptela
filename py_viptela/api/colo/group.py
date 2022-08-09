def getServiceChain(vmanage, serviceGroupName):
    """
    Get service chain by name
    
    Parameters:
    serviceGroupName	 (string):	Service group name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/servicegroup?serviceGroupName={serviceGroupName}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def update(vmanage, servicegroup):
    """
    Update service group
    
    Parameters:
    servicegroup:	Service group
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/servicegroup"
    response = vmanage.apiCall("PUT", endpoint, servicegroup)
    return response

def create(vmanage, servicegroup):
    """
    Add new service group
    
    Parameters:
    servicegroup:	Service group
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/servicegroup"
    response = vmanage.apiCall("POST", endpoint, servicegroup)
    return response

def getGroupInCluster(vmanage, ClusterId, UserGroupName):
    """
    Get service chains in cluster
    
    Parameters:
    ClusterId	 (string):	Cluster Id
	UserGroupName	 (string):	UserGroup Name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/servicegroup/attached?ClusterId={ClusterId}&UserGroupName={UserGroupName}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getDefaultChain(vmanage):
    """
    Get default service chains
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/servicegroup/servicechain/default"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getAvailableChains(vmanage):
    """
    Get all service chains
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/servicegroup/servicechains"
    response = vmanage.apiCall("GET", endpoint)
    return response

def delete(vmanage, name):
    """
    Delete service group
    
    Parameters:
    name	 (string):	Service group name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/servicegroup/{name}"
    response = vmanage.apiCall("DELETE", endpoint)
    return response
