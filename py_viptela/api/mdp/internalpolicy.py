def add(vmanage, policy):
    """
    Add internal policy from vmanage
    
    Parameters:
    policy:	    Internal Policy
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/mdp/policies/mdpconfig"
    response = vmanage.client.apiCall(vmanage.PUT, endpoint, policy)
    return response
