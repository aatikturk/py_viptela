from py_viptela.query_builder import Builder
from py_viptela import HttpMethods


def getVmanageConnList(vmanage):
    """
    Create device vManage connection list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/messaging/device/vmanage"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
