def generateVoiceTemplateList(vmanage):
    """
    Generate template list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/voice"
    response = vmanage.apiCall("GET", endpoint)
    return response

def createVoiceTemplate(vmanage, policytemplate):
    """
    Create Template
    
    Parameters:
    policytemplate:	Policy template
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/voice"
    response = vmanage.apiCall("POST", endpoint, policytemplate)
    return response

def getTemplateById(vmanage, policyId):
    """
    Get templates by policy Id
    
    Parameters:
    policyId	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/voice/definition/{policyId}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getVoicePolicyDeviceList(vmanage):
    """
    Get all device list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/voice/devices"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getDeviceListByPolicyId(vmanage, policyId):
    """
    Get device list by policy Id
    
    Parameters:
    policyId	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/voice/devices/{policyId}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def generateVoicePolicySummary(vmanage):
    """
    Get templates that map a device model
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/voice/summary"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getVoiceTemplatesForDevice(vmanage, deviceModel):
    """
    Get templates that map a device model
    
    Parameters:
    deviceModel:  Device Model
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/voice/{deviceModel}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def editVoiceTemplate(vmanage, policytemplate, policyId):
    """
    Edit Template
    
    Parameters:
    policytemplate:	Policy template
	policyId	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/voice/{policyId}"
    response = vmanage.apiCall("PUT", endpoint, policytemplate)
    return response

def deleteVoiceTemplate(vmanage, policyId):
    """
    Delete Template
    
    Parameters:
    policyId	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/voice/{policyId}"
    response = vmanage.apiCall("DELETE", endpoint)
    return response
