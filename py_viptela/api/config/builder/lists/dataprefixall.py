def getListsForAllDataPrefixes(vmanage):
    """
    Get policy lists for all data prefixes
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/list/dataprefixall"
    response = vmanage.apiCall("GET", endpoint)
    return response

def create(vmanage, policylist):
    """
    Create policy list
    
    Parameters:
    policylist:	Policy list
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/list/dataprefixall"
    response = vmanage.apiCall("POST", endpoint, policylist)
    return response

def preview(vmanage, policylist):
    """
    Preview a policy list based on the policy list type
    
    Parameters:
    policylist:	Policy list
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/list/dataprefixall/preview"
    response = vmanage.apiCall("POST", endpoint, policylist)
    return response

def previewById(vmanage, id):
    """
    Preview a specific policy list entry based on id provided
    
    Parameters:
    id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/list/dataprefixall/preview/{id}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getListsById(vmanage, id):
    """
    Get a specific policy list based on the id
    
    Parameters:
    id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/list/dataprefixall/{id}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def edit(vmanage, policylist, id):
    """
    Edit policy list entries for a specific type of policy list
    
    Parameters:
    policylist:	Policy list
	id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/list/dataprefixall/{id}"
    response = vmanage.apiCall("PUT", endpoint, policylist)
    return response

def delete(vmanage, id):
    """
    Delete policy list entry for a specific type of policy list
    
    Parameters:
    id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/list/dataprefixall/{id}"
    response = vmanage.apiCall("DELETE", endpoint)
    return response
