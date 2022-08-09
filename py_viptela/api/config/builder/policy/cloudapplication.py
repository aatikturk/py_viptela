from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def getCloudDiscoveredApps(vmanage):
    """
    Get all cloud discovered applications
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/clouddiscoveredapp"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
