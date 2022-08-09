def cancelPending(vmanage, processId):
    """
    Bulk cancel task status
    
    Parameters:
    processId	 (string):	Process Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/status/cancel/{processId}"
    response = vmanage.client.apiCall(vmanage.POST, endpoint)
    return response

def cleanStatus(vmanage, cleanStatus):
    """
    Delete task and status vertex
    
    Parameters:
    cleanStatus	 (boolean):	Clear status flag
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/status/clean?cleanStatus={cleanStatus}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def deleteStatus(vmanage, processId):
    """
    Delete status of action
    
    Parameters:
    processId	 (string):	Process Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/status/clear?processId={processId}"
    response = vmanage.client.apiCall(vmanage.DELETE, endpoint)
    return response

def findRunning(vmanage):
    """
    Find running tasks
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/status/tasks"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getActiveCount(vmanage):
    """
    Get active task count
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/status/tasks/activeCount"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getCleanStatus(vmanage, processId):
    """
    Delete task and status vertex
    
    Parameters:
    processId	 (string):	Process Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/status/tasks/clean?processId={processId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def findStatus(vmanage, actionName):
    """
    Find status of action
    
    Parameters:
    actionName	 (string):	Action name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/status/{actionName}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
