from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def getPolicies(vmanage, nmsId):
    """
    Retrieve MDP policies
    
    Parameters:
    nmsId:  NMS server ID
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/mdp/policies/{nmsId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def updatePolicyStatus(vmanage, policylist, nmsId):
    """
    update policy status
    
    Parameters:
    policylist:	policyList
	nmsId:  NMS server ID
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/mdp/policies/{nmsId}"
    response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, policylist)
    return response
