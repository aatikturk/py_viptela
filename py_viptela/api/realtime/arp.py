from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def getInterface(vmanage, deviceId):
    """
    Get ARP interfaces from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/arp?deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
