def getVmanageConnList(vmanage):
    """
    Create device vManage connection list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/messaging/device/vmanage"
    response = vmanage.apiCall("GET", endpoint)
    return response
