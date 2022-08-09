def add(vmanage, policy):
    """
    Add internal policy from vmanage
    
    Parameters:
    policy:	    Internal Policy
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/mdp/policies/mdpconfig"
    response = vmanage.apiCall("PUT", endpoint, policy)
    return response
