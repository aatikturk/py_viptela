def attach(vmanage, request):
    """
    Attach service chain to cluster
    
    Parameters:
    request:	Attach service chain request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/servicechain/attach"
    response = vmanage.apiCall("POST", endpoint, request)
    return response

def autoAttach(vmanage, request):
    """
    Attach service chain to cluster
    
    Parameters:
    request:	Attach service chain request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/servicechain/autoattach"
    response = vmanage.apiCall("POST", endpoint, request)
    return response

def detach(vmanage, request):
    """
    Detach service chain
    
    Parameters:
    request:	Detach service chain request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/servicechain/detach"
    response = vmanage.apiCall("PUT", endpoint, request)
    return response

def getEdgeDevices(vmanage):
    """
    Get edge devices
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/servicechain/edge/devices"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getpnfDevices(vmanage, pnfDeviceType):
    """
    Get PNF edge devices
    
    Parameters:
    pnfDeviceType	 (string):	PNF device type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/colocation/servicechain/edge/pnfdevices?pnfDeviceType={pnfDeviceType}"
    response = vmanage.apiCall("GET", endpoint)
    return response
