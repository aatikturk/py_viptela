def checkGivenIpList(vmanage, devicedetail):
    """
    Block IP based on list
    
    Parameters:
    devicedetail:	Device detail
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/software/compliance/ip/origin/check"
    response = vmanage.apiCall("POST", endpoint, devicedetail)
    return response
