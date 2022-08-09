from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def createFull(vmanage):
    """
    Create full topology
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/topology"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def createDevice(vmanage, deviceId):
    """
    Create device topology
    
    Parameters:
    deviceId	 (array):	Device Id list
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/topology/device?deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def createPhysical(vmanage, deviceId):
    """
    Create pysical topology
    
    Parameters:
    deviceId	 (array):	Device Id list
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/topology/physical?deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
