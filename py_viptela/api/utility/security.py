def checkGivenIpList(vmanage, devicedetail):
    """
    Block IP based on list
    
    Parameters:
    devicedetail:	Device detail
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/software/compliance/ip/origin/check"
    response = vmanage.client.apiCall("POST", endpoint, devicedetail)
    return response
