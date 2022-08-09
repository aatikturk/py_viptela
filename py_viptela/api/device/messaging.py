def getVmanageConnList(vmanage):
    """
    Create device vManage connection list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/messaging/device/vmanage"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
