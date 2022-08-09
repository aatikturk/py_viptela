from py_viptela.query_builder import Builder
from py_viptela import HttpMethods
    
def attach(vmanage, request):
    """
    Attach service chain to cluster
    
    Parameters:
    request:	Attach service chain request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/colocation/servicechain/attach"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, request)
    return response

def autoAttach(vmanage, request):
    """
    Attach service chain to cluster
    
    Parameters:
    request:	Attach service chain request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/colocation/servicechain/autoattach"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, request)
    return response

def detach(vmanage, request):
    """
    Detach service chain
    
    Parameters:
    request:	Detach service chain request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/colocation/servicechain/detach"
    response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, request)
    return response

def getEdgeDevices(vmanage):
    """
    Get edge devices
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/colocation/servicechain/edge/devices"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def getpnfDevices(vmanage, pnfDeviceType):
    """
    Get PNF edge devices
    
    Parameters:
    pnfDeviceType	 (string):	PNF device type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/colocation/servicechain/edge/pnfdevices?pnfDeviceType={pnfDeviceType}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
