def getPolicies(vmanage, nmsId):
    """
    Retrieve MDP policies
    
    Parameters:
    nmsId:  NMS server ID
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/mdp/policies/{nmsId}"
    response = vmanage.apiCall("GET", endpoint)
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
    
    endpoint = f"dataservice/mdp/policies/{nmsId}"
    response = vmanage.apiCall("PUT", endpoint, policylist)
    return response
