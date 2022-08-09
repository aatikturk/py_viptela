from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def getConfig(vmanage, deviceId):
    """
    Retrieve MDP ConfigObject
    
    Parameters:
    Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/mdp/policies/mdpconfig/{deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
