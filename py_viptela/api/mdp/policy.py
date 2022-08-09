def getPolicies(vmanage, nmsId):
    """
    Retrieve MDP policies
    
    Parameters:
    nmsId:  NMS server ID
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/mdp/policies/{nmsId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
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
    response = vmanage.client.apiCall(vmanage.PUT, endpoint, policylist)
    return response
