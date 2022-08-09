from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def updateLeaseTime(vmanage, processId):
    """
    Update lease
    
    Parameters:
    processId	 (string):	Process Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/lock/{processId}"
    response = vmanage.client.apiCall(HttpMethods.PUT, endpoint)
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
    response = vmanage.client.apiCall(HttpMethods.DELETE, endpoint)
    return response
