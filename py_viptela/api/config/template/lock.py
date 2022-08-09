def updateLeaseTime(vmanage, processId):
    """
    Update lease
    
    Parameters:
    processId	 (string):	Process Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/lock/{processId}"
    response = vmanage.apiCall("PUT", endpoint)
    return response

def removeLock(vmanage, processId):
    """
    Remove lock
    
    Parameters:
    processId	 (string):	Process Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/lock/{processId}"
    response = vmanage.apiCall("DELETE", endpoint)
    return response
