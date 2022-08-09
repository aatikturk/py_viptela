from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def getGlobalDropStats(vmanage, deviceId):
    """
    Get SD-WAN global drop statistics detail from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/sdwan-global-drop-statistics?deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getStats(vmanage, deviceId):
    """
    Get SD-WAN statistics detail from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/sdwan-stats?deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
