from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def getStats(vmanage, deviceId):
    """
    Get tcp proxy statistics from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/tcpproxy/statistics?deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getStatus(vmanage, deviceId):
    """
    Get tcp proxy status from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/tcpproxy/status?deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
