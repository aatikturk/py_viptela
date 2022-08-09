def updateLeaseTime(vmanage, processId):
    """
    Update lease
    
    Parameters:
    processId	 (string):	Process Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/lock/{processId}"
    response = vmanage.client.apiCall(vmanage.PUT, endpoint)
    return response

def removeLock(vmanage, processId):
    """
    Remove lock
    
    Parameters:
    processId	 (string):	Process Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/lock/{processId}"
    response = vmanage.client.apiCall(vmanage.DELETE, endpoint)
    return response
