from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def get(vmanage, deviceId):
    """
    Get on-demand remote (Real Time)
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/ondemand/remote?deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
