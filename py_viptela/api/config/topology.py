def createFull(vmanage):
    """
    Create full topology
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/topology"
    response = vmanage.apiCall("GET", endpoint)
    return response

def createDevice(vmanage, deviceId):
    """
    Create device topology
    
    Parameters:
    deviceId	 (array):	Device Id list
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/topology/device?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def createPhysical(vmanage, deviceId):
    """
    Create pysical topology
    
    Parameters:
    deviceId	 (array):	Device Id list
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/topology/physical?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
