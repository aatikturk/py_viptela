from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def getIf(vmanage, deviceId):
    """
    Get VRRP interface list from device
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/vrrp?deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
