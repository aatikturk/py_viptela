from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def get(vmanage):
    """
    Get policy lists
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/community"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def create(vmanage, policylist):
    """
    Create policy list
    
    Parameters:
    policylist:	Policy list
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/community"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, policylist)
    return response

def preview(vmanage, policylist):
    """
    Preview a policy list based on the policy list type
    
    Parameters:
    policylist:	Policy list
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/community/preview"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, policylist)
    return response

def previewById(vmanage, id):
    """
    Preview a specific policy list entry based on id provided
    
    Parameters:
    id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/community/preview/{id}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def getListsById(vmanage, id):
    """
    Get a specific policy list based on the id
    
    Parameters:
    id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/community/{id}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
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
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/community/{id}"
    response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, policylist)
    return response

def delete(vmanage, id):
    """
    Delete policy list entry for a specific type of policy list
    
    Parameters:
    id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/community/{id}"
    response = vmanage.client.apiCall(HttpMethods.DELETE, endpoint)
    return response
