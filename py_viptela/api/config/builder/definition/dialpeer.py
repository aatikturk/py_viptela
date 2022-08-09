from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def getDefinitions(vmanage):
    """
    Get policy definitions
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/definition/dialpeer"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def create(vmanage, policydefinition):
    """
    Create policy definition
    
    Parameters:
    policydefinition:	Policy definition
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/definition/dialpeer"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, policydefinition)
    return response

def saveInBulk(vmanage, policydefinition):
    """
    Create/Edit policy definitions in bulk
    
    Parameters:
    policydefinition:	Policy definition
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/definition/dialpeer/bulk"
    response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, policydefinition)
    return response

def editMultiple(vmanage, policydefinition, id):
    """
    Edit multiple policy definitions
    
    Parameters:
    policydefinition:	Policy definition
	id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/definition/dialpeer/multiple/{id}"
    response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, policydefinition)
    return response

def preview(vmanage, policydefinition):
    """
    Preview policy definition
    
    Parameters:
    policydefinition:	Policy definition
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/definition/dialpeer/preview"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, policydefinition)
    return response

def previewById(vmanage, id):
    """
    Preview policy definition
    
    Parameters:
    id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/definition/dialpeer/preview/{id}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def get(vmanage, id):
    """
    Get a specific policy definitions
    
    Parameters:
    id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/definition/dialpeer/{id}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def edit(vmanage, policydefinition, id):
    """
    Edit a policy definitions
    
    Parameters:
    policydefinition:	Policy definition
	id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/definition/dialpeer/{id}"
    response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, policydefinition)
    return response

def delete(vmanage, id):
    """
    Delete policy definition
    
    Parameters:
    id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/definition/dialpeer/{id}"
    response = vmanage.client.apiCall(HttpMethods.DELETE, endpoint)
    return response

def getDefinitionsSRST(vmanage):
    """
    Get policy definitions
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/definition/srstphoneprofile"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def createSRST(vmanage, policydefinition):
    """
    Create policy definition
    
    Parameters:
    policydefinition:	Policy definition
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/definition/srstphoneprofile"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, policydefinition)
    return response

def saveInBulkSRST(vmanage, policydefinition):
    """
    Create/Edit policy definitions in bulk
    
    Parameters:
    policydefinition:	Policy definition
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/definition/srstphoneprofile/bulk"
    response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, policydefinition)
    return response

def editMultipleSRST(vmanage, policydefinition, id):
    """
    Edit multiple policy definitions
    
    Parameters:
    policydefinition:	Policy definition
	id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/definition/srstphoneprofile/multiple/{id}"
    response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, policydefinition)
    return response

def previewSRST(vmanage, policydefinition):
    """
    Preview policy definition
    
    Parameters:
    policydefinition:	Policy definition
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/definition/srstphoneprofile/preview"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, policydefinition)
    return response

def previewByIdSRST(vmanage, id):
    """
    Preview policy definition
    
    Parameters:
    id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/definition/srstphoneprofile/preview/{id}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def getSRST(vmanage, id):
    """
    Get a specific policy definitions
    
    Parameters:
    id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/definition/srstphoneprofile/{id}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def editSRST(vmanage, policydefinition, id):
    """
    Edit a policy definitions
    
    Parameters:
    policydefinition:	Policy definition
	id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/definition/srstphoneprofile/{id}"
    response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, policydefinition)
    return response

def deleteSRST(vmanage, id):
    """
    Delete policy definition
    
    Parameters:
    id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/definition/srstphoneprofile/{id}"
    response = vmanage.client.apiCall(HttpMethods.DELETE, endpoint)
    return response
