from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def findSoftwareImages(vmanage):
    """
    Get software images
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/software"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def createImageURL(vmanage, payload):
    """
    Create software image URL
    
    Parameters:
    payload:	Create software image request payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/software"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, payload)
    return response

def getImageProps(vmanage, versionId):
    """
    Get Image Properties
    
    Parameters:
    versionId	 (string):	Version
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/software/imageProperties/{versionId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def findImagesWithFilters(vmanage, imageType, vnfType):
    """
    Get software images
    
    Parameters:
    imageType	 (string):	Image type
	vnfType	 (string):	VNF type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/software/images?imageType={imageType}&vnfType={vnfType}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def getPnfProperties(vmanage, pnfType):
    """
    Get PNF Properties
    
    Parameters:
    pnfType	 (string):	PNF type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/software/pnfproperties/{pnfType}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def findVEdgeSoftwareVersion(vmanage):
    """
    Get vEdge software version
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/software/vedge/version"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def findSoftwareVersion(vmanage):
    """
    Get software version
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/software/version"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def getVnfProperties(vmanage, versionId):
    """
    Get VNF Properties
    
    Parameters:
    versionId	 (string):	Version
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/software/vnfproperties/{versionId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def findZtpSoftwareVersion(vmanage):
    """
    Get ZTP software version
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/software/ztp/version"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def updateImageURL(vmanage, payload, versionId):
    """
    Update software image URL
    
    Parameters:
    payload:	Update software image request payload
	versionId	 (string):	Version
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/software/{versionId}"
    response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, payload)
    return response

def deleteImageURL(vmanage, versionId):
    """
    Delete software image URL
    
    Parameters:
    versionId	 (string):	Version
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/action/software/{versionId}"
    response = vmanage.client.apiCall(HttpMethods.DELETE, endpoint)
    return response
