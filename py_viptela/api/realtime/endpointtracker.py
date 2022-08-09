from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def getInfo(vmanage, deviceId):
    """
    Get endpoint tracker info from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/endpointTracker?deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
