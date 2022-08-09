def getApp(vmanage):
    """
    Get policy lists
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/app"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def createApp(vmanage, policylist):
    """
    Create policy list
    
    Parameters:
    policylist:	Policy list
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/app"
    response = vmanage.client.apiCall("POST", endpoint, policylist)
    return response

def previewApp(vmanage, policylist):
    """
    Preview a policy list based on the policy list type
    
    Parameters:
    policylist:	Policy list
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/app/preview"
    response = vmanage.client.apiCall("POST", endpoint, policylist)
    return response

def previewAppById(vmanage, id):
    """
    Preview a specific policy list entry based on id provided
    
    Parameters:
    id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/app/preview/{id}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getAppListsById(vmanage, id):
    """
    Get a specific policy list based on the id
    
    Parameters:
    id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/app/{id}"
    response = vmanage.client.apiCall("GET", endpoint)
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
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/app/{id}"
    response = vmanage.client.apiCall("PUT", endpoint, policylist)
    return response

def deleteApp(vmanage, id):
    """
    Delete policy list entry for a specific type of policy list
    
    Parameters:
    id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/app/{id}"
    response = vmanage.client.apiCall("DELETE", endpoint)
    return response

def getLocalApp(vmanage):
    """
    Get policy lists
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/localapp"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def createLocalApp(vmanage, policylist):
    """
    Create policy list
    
    Parameters:
    policylist:	Policy list
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/localapp"
    response = vmanage.client.apiCall("POST", endpoint, policylist)
    return response

def previewLocalApp(vmanage, policylist):
    """
    Preview a policy list based on the policy list type
    
    Parameters:
    policylist:	Policy list
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/localapp/preview"
    response = vmanage.client.apiCall("POST", endpoint, policylist)
    return response

def previewLocalAppById(vmanage, id):
    """
    Preview a specific policy list entry based on id provided
    
    Parameters:
    id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/localapp/preview/{id}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getLocalAppListsById(vmanage, id):
    """
    Get a specific policy list based on the id
    
    Parameters:
    id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/localapp/{id}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def editLocalApp(vmanage, policylist, id):
    """
    Edit policy list entries for a specific type of policy list
    
    Parameters:
    policylist:	Policy list
	id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/localapp/{id}"
    response = vmanage.client.apiCall("PUT", endpoint, policylist)
    return response

def deleteLocalApp(vmanage, id):
    """
    Delete policy list entry for a specific type of policy list
    
    Parameters:
    id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/localapp/{id}"
    response = vmanage.client.apiCall("DELETE", endpoint)
    return response
