def get(vmanage):
    """
    Get network circuits
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/networkdesign/circuit"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def create(vmanage, networkcircuit):
    """
    Create network circuits
    
    Parameters:
    networkcircuit:	Network circuit
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/networkdesign/circuit"
    response = vmanage.client.apiCall("POST", endpoint, networkcircuit)
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
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/networkdesign/circuit/{id}"
    response = vmanage.client.apiCall("PUT", endpoint, networkcircuit)
    return response

def delete(vmanage, id):
    """
    Delete network circuits
    
    Parameters:
    id	 (string):	Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/networkdesign/circuit/{id}"
    response = vmanage.client.apiCall("DELETE", endpoint)
    return response
