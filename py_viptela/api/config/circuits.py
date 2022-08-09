def get(vmanage):
    """
    Get network circuits
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/networkdesign/circuit"
    response = vmanage.apiCall("GET", endpoint)
    return response

def create(vmanage, networkcircuit):
    """
    Create network circuits
    
    Parameters:
    networkcircuit:	Network circuit
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/networkdesign/circuit"
    response = vmanage.apiCall("POST", endpoint, networkcircuit)
    return response

def edit(vmanage, networkcircuit, id):
    """
    Edit network circuits
    
    Parameters:
    networkcircuit:	Network circuit
	id	 (string):	Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/networkdesign/circuit/{id}"
    response = vmanage.apiCall("PUT", endpoint, networkcircuit)
    return response

def delete(vmanage, id):
    """
    Delete network circuits
    
    Parameters:
    id	 (string):	Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/networkdesign/circuit/{id}"
    response = vmanage.apiCall("DELETE", endpoint)
    return response
