from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def generateVoiceTemplateList(vmanage):
    """
    Generate template list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/voice"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def createVoiceTemplate(vmanage, policytemplate):
    """
    Create Template
    
    Parameters:
    policytemplate:	Policy template
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/voice"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, policytemplate)
    return response

def getTemplateById(vmanage, policyId):
    """
    Get templates by policy Id
    
    Parameters:
    policyId	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/voice/definition/{policyId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def getVoicePolicyDeviceList(vmanage):
    """
    Get all device list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/voice/devices"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def getDeviceListByPolicyId(vmanage, policyId):
    """
    Get device list by policy Id
    
    Parameters:
    policyId	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/voice/devices/{policyId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def generateVoicePolicySummary(vmanage):
    """
    Get templates that map a device model
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/voice/summary"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def getVoiceTemplatesForDevice(vmanage, deviceModel):
    """
    Get templates that map a device model
    
    Parameters:
    deviceModel:  Device Model
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/voice/{deviceModel}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
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
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/voice/{policyId}"
    response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, policytemplate)
    return response

def deleteVoiceTemplate(vmanage, policyId):
    """
    Delete Template
    
    Parameters:
    policyId	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/voice/{policyId}"
    response = vmanage.client.apiCall(HttpMethods.DELETE, endpoint)
    return response
