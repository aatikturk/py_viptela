from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def getSigDataCenterList(vmanage, type):
    """
    Get list of data centers for zscaler or umbrella
    
    Parameters:
    type	 (string):	Provider type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sig/datacenters/{type}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
