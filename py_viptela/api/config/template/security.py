from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def generateSecurityTemplateList(vmanage, mode):
    """
    Generate template list
    
    Parameters:
    mode	 (string):	Mode
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/security?mode={mode}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def createSecurityTemplate(vmanage, policytemplate):
    """
    Create Template
    
    Parameters:
    policytemplate:	Policy template
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/security"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, policytemplate)
    return response

def getSecurityTemplate(vmanage, policyId):
    """
    Get Template
    
    Parameters:
    policyId	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/security/definition/{policyId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def getSecurityPolicyDeviceList(vmanage):
    """
    Get device list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/security/devices"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def getDeviceListById(vmanage, policyId):
    """
    Get device list by Id
    
    Parameters:
    policyId	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/security/devices/{policyId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
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
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/security/staging/{policyId}"
    response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, policytemplate)
    return response

def generateSecurityPolicySummary(vmanage):
    """
    Generate security policy summary
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/security/summary"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def getSecurityTemplatesForDevice(vmanage, deviceModel):
    """
    Get templates that map a device model
    
    Parameters:
    Parameter Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/security/{deviceModel}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
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
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/security/{policyId}"
    response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, policytemplate)
    return response

def deleteSecurityTemplate(vmanage, policyId):
    """
    Delete Template
    
    Parameters:
    policyId	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/security/{policyId}"
    response = vmanage.client.apiCall(HttpMethods.DELETE, endpoint)
    return response
