def installPkg(vmanage):
    """
    Install software package
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/action/software/package"
    response = vmanage.apiCall("POST", endpoint)
    return response

def getUploadImagesCount(vmanage, imageType):
    """
    Number of software image presented in vManage repository
    
    Parameters:
    imageType	 (array):	Image type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/action/software/package/imageCount?imageType={imageType}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def downloadPkgFile(vmanage, fileName, imageType):
    """
    Download software package file
    
    Parameters:
    fileName	 (string):	Pakcage file name
	imageType	 (string):	Image type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/action/software/package/{fileName}?imageType={imageType}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def processSoftwareImage(vmanage, imageType):
    """
    Install software image package
    
    Parameters:
    imageType	 (string):	Image type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/action/software/package/{imageType}"
    response = vmanage.apiCall("POST", endpoint)
    return response

def getImgMeta(vmanage, versionId):
    """
    Update Package Metadata
    
    Parameters:
    versionId	 (string):	Image ID
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/action/software/package/{versionId}/metadata"
    response = vmanage.apiCall("GET", endpoint)
    return response

def editImgMeta(vmanage, imageData, versionId):
    """
    Update Package Metadata
    
    Parameters:
    imageData:	Image Meta Data
	versionId	 (string):	Image ID
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/action/software/package/{versionId}/metadata"
    response = vmanage.apiCall("PUT", endpoint, imageData)
    return response
