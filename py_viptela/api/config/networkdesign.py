def getNetworkDesign(vmanage):
    """
    Get existing network design
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/networkdesign"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def editNetworkDesign(vmanage, payload, id):
    """
    Edit network segment
    
    Parameters:
    payload:	Network design payload
	id	 (string):	Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/networkdesign?id={id}"
    response = vmanage.client.apiCall("PUT", endpoint, payload)
    return response

def createNetworkDesign(vmanage, payload):
    """
    Create network design
    
    Parameters:
    payload:	Network design payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/networkdesign"
    response = vmanage.client.apiCall("POST", endpoint, payload)
    return response

def pushNetworkDesign(vmanage, devicetemplate):
    """
    Attach network design
    
    Parameters:
    devicetemplate:	Device template
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/networkdesign/attachment"
    response = vmanage.client.apiCall("POST", endpoint, devicetemplate)
    return response

def getGlobalParams(vmanage):
    """
    Get global parameter templates
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/networkdesign/global/parameters"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def acquireEditLock(vmanage):
    """
    Acquire edit lock
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/networkdesign/lock/edit"
    response = vmanage.client.apiCall("POST", endpoint)
    return response

def runMyTest(vmanage, name):
    """
    Get all device templates for this feature template
    
    Parameters:
    name	 (string):	Test bane
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/networkdesign/mytest/{name}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def pushDeviceProfileTemplate(vmanage, devicetemplate, profileId):
    """
    Attach to device profile
    
    Parameters:
    devicetemplate:	Device template
	profileId	 (string):	Device profile Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/networkdesign/profile/attachment/{profileId}"
    response = vmanage.client.apiCall("POST", endpoint, devicetemplate)
    return response

def acquireAttachLock(vmanage, profileId):
    """
    Get the service profile config for a given device profile id
    
    Parameters:
    profileId	 (string):	Device profile Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/networkdesign/profile/lock/{profileId}"
    response = vmanage.client.apiCall("POST", endpoint)
    return response

def getConfigStatus(vmanage):
    """
    Get device profile configuration status
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/networkdesign/profile/status"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getConfigStatusById(vmanage, profileId):
    """
    Get device profile configuration status by profile Id
    
    Parameters:
    profileId	 (string):	Device profile Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/networkdesign/profile/status/{profileId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getTaskCount(vmanage):
    """
    Get device profile configuration task count
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/networkdesign/profile/task/count"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getTaskStatus(vmanage):
    """
    Get device profile configuration task status
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/networkdesign/profile/task/status"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getTaskStatusById(vmanage, profileId):
    """
    Get device profile configuration status by profile Id
    
    Parameters:
    profileId	 (string):	Device profile Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/networkdesign/profile/task/status/{profileId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getServiceProfileConfig(vmanage, profileId, deviceModel):
    """
    Get the service profile config for a given device profile id
    
    Parameters:
    profileId	 (string):	Device profile Id
	deviceModel	 (string):	Device model
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/networkdesign/serviceProfileConfig/{profileId}?deviceModel={deviceModel}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
