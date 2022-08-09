def getDefinitions(vmanage):
    """
    Get policy definitions
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/definition/fxsdidport"
    response = vmanage.apiCall("GET", endpoint)
    return response

def create(vmanage, policydefinition):
    """
    Create policy definition
    
    Parameters:
    policydefinition:	Policy definition
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/definition/fxsdidport"
    response = vmanage.apiCall("POST", endpoint, policydefinition)
    return response

def saveInBulk(vmanage, policydefinition):
    """
    Create/Edit policy definitions in bulk
    
    Parameters:
    policydefinition:	Policy definition
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/definition/fxsdidport/bulk"
    response = vmanage.apiCall("PUT", endpoint, policydefinition)
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
    
    endpoint = f"dataservice/template/policy/definition/fxsdidport/multiple/{id}"
    response = vmanage.apiCall("PUT", endpoint, policydefinition)
    return response

def preview(vmanage, policydefinition):
    """
    Preview policy definition
    
    Parameters:
    policydefinition:	Policy definition
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/definition/fxsdidport/preview"
    response = vmanage.apiCall("POST", endpoint, policydefinition)
    return response

def previewById(vmanage, id):
    """
    Preview policy definition
    
    Parameters:
    id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/definition/fxsdidport/preview/{id}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def get(vmanage, id):
    """
    Get a specific policy definitions
    
    Parameters:
    id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/definition/fxsdidport/{id}"
    response = vmanage.apiCall("GET", endpoint)
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
    
    endpoint = f"dataservice/template/policy/definition/fxsdidport/{id}"
    response = vmanage.apiCall("PUT", endpoint, policydefinition)
    return response

def delete(vmanage, id):
    """
    Delete policy definition
    
    Parameters:
    id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/definition/fxsdidport/{id}"
    response = vmanage.apiCall("DELETE", endpoint)
    return response
