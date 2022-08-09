from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def getDeviceInfo(vmanage, deviceId):
    """
    Get device container from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/csp/containers/container?deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
