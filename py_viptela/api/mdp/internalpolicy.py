from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def add(vmanage, policy):
    """
    Add internal policy from vmanage
    
    Parameters:
    policy:	    Internal Policy
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/mdp/policies/mdpconfig"
    response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, policy)
    return response
