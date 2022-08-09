def getVbranchNics(vmanage, deviceId):
    """
    Get vbranch vm lifecycle state (NIC)
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/vm/nics?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getCloudDockNics(vmanage, userGroup):
    """
    Get CloudDock vm lifecycle state
    
    Parameters:
    userGroup	 (string):	userGroup Name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/vm/notifications?userGroup={userGroup}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getVbranch(vmanage, deviceId):
    """
    Get vbranch vm lifecycle state
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/vm/oper/state?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getState(vmanage, deviceId):
    """
    Get vm lifecycle state
    
    Parameters:
    deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/vm/state?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
