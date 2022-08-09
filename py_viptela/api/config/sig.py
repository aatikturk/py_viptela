from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def getSigTunnelList(vmanage, deviceId):
    """
    Get Secure Internet Gateway Tunnel List
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/cloudx/sig_tunnels?deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
