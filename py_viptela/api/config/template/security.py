def generateSecurityTemplateList(vmanage, mode):
    """
    Generate template list
    
    Parameters:
    mode	 (string):	Mode
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/security?mode={mode}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def createSecurityTemplate(vmanage, policytemplate):
    """
    Create Template
    
    Parameters:
    policytemplate:	Policy template
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/security"
    response = vmanage.apiCall("POST", endpoint, policytemplate)
    return response

def getSecurityTemplate(vmanage, policyId):
    """
    Get Template
    
    Parameters:
    policyId	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/security/definition/{policyId}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getSecurityPolicyDeviceList(vmanage):
    """
    Get device list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/security/devices"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getDeviceListById(vmanage, policyId):
    """
    Get device list by Id
    
    Parameters:
    policyId	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/security/devices/{policyId}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def editTemplateWithLenientLock(vmanage, policytemplate, policyId):
    """
    Edit Template
    
    Parameters:
    policytemplate:	Policy template
	policyId	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/security/staging/{policyId}"
    response = vmanage.apiCall("PUT", endpoint, policytemplate)
    return response

def generateSecurityPolicySummary(vmanage):
    """
    Generate security policy summary
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/security/summary"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getSecurityTemplatesForDevice(vmanage, deviceModel):
    """
    Get templates that map a device model
    
    Parameters:
    Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/security/{deviceModel}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def editSecurityTemplate(vmanage, policytemplate, policyId):
    """
    Edit Template
    
    Parameters:
    policytemplate:	Policy template
	policyId	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/security/{policyId}"
    response = vmanage.apiCall("PUT", endpoint, policytemplate)
    return response

def deleteSecurityTemplate(vmanage, policyId):
    """
    Delete Template
    
    Parameters:
    policyId	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/template/policy/security/{policyId}"
    response = vmanage.apiCall("DELETE", endpoint)
    return response
