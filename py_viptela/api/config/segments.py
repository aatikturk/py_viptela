def getSegments(vmanage):
    """
    Get network segments
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/segment"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def createSegment(vmanage, segmen):
    """
    Create network segment
    
    Parameters:
    segmen:	Network segment
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/segment"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, segmen)
    return response

def getSegment(vmanage, id):
    """
    Get network segment
    
    Parameters:
    id	 (string):	Segment Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/segment/{id}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def editSegment(vmanage, segmen, id):
    """
    Edit network segment
    
    Parameters:
    segmen:	Network segment
	id	 (string):	Segment Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/segment/{id}"
    response = vmanage.client.apiCall(vmanage.PUT, endpoint, segmen)
    return response

def deleteSegment(vmanage, id):
    """
    Delete network segment
    
    Parameters:
    id	 (string):	Segment Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/segment/{id}"
    response = vmanage.client.apiCall(vmanage.DELETE, endpoint)
    return response
