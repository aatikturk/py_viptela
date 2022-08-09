def MapTrafficProfiles(vmanage, apppayload):
    """
    Set SLA class for policy cloud discovered applications
    
    Parameters:
    apppayload:	App payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/clouddiscoveredapp"
    response = vmanage.apiCall("POST", endpoint, apppayload)
    return response

def getCustomApps(vmanage):
    """
    Get all policy custom applications
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/customapp"
    response = vmanage.apiCall("GET", endpoint)
    return response

def create(vmanage, apppayload):
    """
    Create a policy custom applications
    
    Parameters:
    apppayload:	App payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/customapp"
    response = vmanage.apiCall("POST", endpoint, apppayload)
    return response

def getById(vmanage, id):
    """
    Get a policy custom applications
    
    Parameters:
    id	 (string):	Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/customapp/{id}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def edit(vmanage, apppayload, id):
    """
    Edit a policy custom applications
    
    Parameters:
    apppayload:	App payload
	id	 (string):	Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/customapp/{id}"
    response = vmanage.apiCall("PUT", endpoint, apppayload)
    return response

def delete(vmanage, id):
    """
    Delete a policy custom applications
    
    Parameters:
    id	 (string):	Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/customapp/{id}"
    response = vmanage.apiCall("DELETE", endpoint)
    return response
