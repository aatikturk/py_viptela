def getSigDataCenterList(vmanage, type):
    """
    Get list of data centers for zscaler or umbrella
    
    Parameters:
    type	 (string):	Provider type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sig/datacenters/{type}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
