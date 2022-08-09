from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def getGlobal(vmanage, templateId):
    """
    Get global template
    
    Parameters:
    templateId	 (string):	Template Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/networkdesign/global/template/{templateId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def editGlobal(vmanage, globaltemplate, templateId):
    """
    Edit global template
    
    Parameters:
    globaltemplate:	Global template
	templateId	 (string):	Template Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/networkdesign/global/template/{templateId}"
    response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, globaltemplate)
    return response

def getFeatureTempList(vmanage):
    """
    Generate device profile template list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/networkdesign/profile/feature"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def getProfileList(vmanage):
    """
    Generate profile template list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/networkdesign/profile/template"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def getDeviceProfile(vmanage, templateId):
    """
    Get device profile template
    
    Parameters:
    templateId	 (string):	Template Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/networkdesign/profile/template/{templateId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response

def editDeviceProfile(vmanage, globaltemplate, templateId):
    """
    Edit device profile template
    
    Parameters:
    globaltemplate:	Global template
	templateId	 (string):	Template Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/networkdesign/profile/template/{templateId}"
    response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, globaltemplate)
    return response
