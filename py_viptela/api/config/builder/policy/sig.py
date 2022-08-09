def getSigDataCenterList(vmanage, type):
    """
    Get list of data centers for zscaler or umbrella
    
    Parameters:
    type	 (string):	Provider type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sig/datacenters/{type}"
    response = vmanage.apiCall("GET", endpoint)
    return response
