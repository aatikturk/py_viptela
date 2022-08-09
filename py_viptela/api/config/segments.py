def getSegments(vmanage):
    """
    Get network segments
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/segment"
    response = vmanage.apiCall("GET", endpoint)
    return response

def createSegment(vmanage, segmen):
    """
    Create network segment
    
    Parameters:
    segmen:	Network segment
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/segment"
    response = vmanage.apiCall("POST", endpoint, segmen)
    return response

def getSegment(vmanage, id):
    """
    Get network segment
    
    Parameters:
    id	 (string):	Segment Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/segment/{id}"
    response = vmanage.apiCall("GET", endpoint)
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
    
    endpoint = f"dataservice/segment/{id}"
    response = vmanage.apiCall("PUT", endpoint, segmen)
    return response

def deleteSegment(vmanage, id):
    """
    Delete network segment
    
    Parameters:
    id	 (string):	Segment Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/segment/{id}"
    response = vmanage.apiCall("DELETE", endpoint)
    return response
