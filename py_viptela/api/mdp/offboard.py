from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def disconnect(vmanage, nmsId):
    """
    disconnect from mpd controller
    
    Parameters:
    Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/mdp/disconnect/{nmsId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def offboard(vmanage, nmsId):
    """
    offboard the mdp application
    
    Parameters:
    Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/mdp/onboard/{nmsId}"
    response = vmanage.client.apiCall(HttpMethods.DELETE, endpoint)
    return response
