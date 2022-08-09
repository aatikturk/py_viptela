def getFileContents(vmanage, uuid):
    """
    Get bootstrap file contents
    
    Parameters:
    uuid	 (string):	File uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/action/software/package/custom/file/{uuid}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def editConfigFile(vmanage, bootstrapfile, uuid):
    """
    Edit bootstrap file
    
    Parameters:
    bootstrapfile:	Bootstrap file
	uuid	 (string):	File uuid
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/action/software/package/custom/file/{uuid}"
    response = vmanage.apiCall("PUT", endpoint, bootstrapfile)
    return response

def uploadImageFile(vmanage, type):
    """
    Upload virtual image/bootstrap file
    
    Parameters:
    type	 (string):	Upload file type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/action/software/package/custom/uploads/{type}"
    response = vmanage.apiCall("POST", endpoint)
    return response

def createVnfPackage(vmanage, custompackage):
    """
    Create VNF custom package
    
    Parameters:
    custompackage:	Custom package
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/action/software/package/custom/vnfPackage"
    response = vmanage.apiCall("POST", endpoint, custompackage)
    return response
