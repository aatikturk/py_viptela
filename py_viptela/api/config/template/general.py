def getFeatureTemplateList(vmanage, summary, offset, limit):
    """
    Get feature template list
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    summary	 (boolean):	Flag to include template definition
	offset	 (integer):	Pagination offset
	limit	 (integer):	Pagination limit on templateId
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/feature?summary={summary}&offset={offset}&limit={limit}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def createFeatureTemplate(vmanage, featuretemplate):
    """
    Create feature template
    
    Parameters:
    featuretemplate:	Feature template
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/feature"
    response = vmanage.client.apiCall("POST", endpoint, featuretemplate)
    return response

def cloneTemplate(vmanage, id, name, desc):
    """
    Clone a feature template
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    id	 (string):	Template Id to clone from
	name	 (string):	Name for the cloned template
	desc	 (string):	Description for the cloned template
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/feature/clone?id={id}&name={name}&desc={desc}"
    response = vmanage.client.apiCall("POST", endpoint)
    return response

def getNetworkInterface(vmanage, deviceModel):
    """
    Get default network interface
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    deviceModel	 (string):	Device model
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/feature/default/networkinterface?deviceModel={deviceModel}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getDefaultNetworks(vmanage, deviceModel):
    """
    Get default networks
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    deviceModel	 (string):	Device model
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/feature/default/networks?deviceModel={deviceModel}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getTemplateDefinition(vmanage, templateId):
    """
    Get the configured template definition for given template Id
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    templateId	 (string):	Template Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/feature/definition/{templateId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getDeviceTemplatesAttachedToFeature(vmanage, templateId):
    """
    Get all device templates for this feature template
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    templateId	 (string):	Feature template Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/feature/devicetemplates/{templateId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def listLITemplate(vmanage):
    """
    Get LI feature template
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/feature/li"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def createLITemplate(vmanage, litemplate):
    """
    Create LI feature template
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    litemplate:	LI template
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/feature/li"
    response = vmanage.client.apiCall("POST", endpoint, litemplate)
    return response

def editLITemplate(vmanage, litemplate, templateId):
    """
    Update LI feature template
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    litemplate:	LI template
	templateId	 (string):	Template Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/feature/li/{templateId}"
    response = vmanage.client.apiCall("PUT", endpoint, litemplate)
    return response

def getMasterTemplateDefinition(vmanage, type_name):
    """
    Generate template type definition by device type
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    type_name	 (string):	Device type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/feature/master/{type_name}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getTemplateForMigration(vmanage):
    """
    Generate a list of templates which require migration
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/feature/migration"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getGeneralTemplate(vmanage, templateId):
    """
    Get template object definition for given template Id
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    templateId	 (string):	Template Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/feature/object/{templateId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def changeTemplateResourceGroup(vmanage, templateId, resourceGroupName):
    """
    Change template resource group
    
    Parameters:
    templateId	 (string):	Template Id
	resourceGroupName	 (string):	Resrouce group name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/feature/resource-group/{resourceGroupName}/{templateId}"
    response = vmanage.client.apiCall("POST", endpoint)
    return response

def getTemplateTypes(vmanage, type):
    """
    Generate template types
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    type	 (string):	Device type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/feature/types?type={type}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getTemplateTypeDefinition(vmanage, type_name, version):
    """
    Generate template type definition
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    type_name	 (string):	Device type
	version	 (string):	Version
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/feature/types/definition/{type_name}/{version}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getTemplateByDeviceType(vmanage, deviceType):
    """
    Generate template based on device
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    deviceType	 (string):	Device type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/feature/{deviceType}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def editFeatureTemplate(vmanage, template, templateId):
    """
    Update feature template
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    template:	Template
	templateId	 (string):	Template Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/feature/{templateId}"
    response = vmanage.client.apiCall("PUT", endpoint, template)
    return response

def deleteGeneralTemplate(vmanage, templateId):
    """
    Delete feature template
    
    Parameters:
    templateId	 (string):	Template Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/feature/{templateId}"
    response = vmanage.client.apiCall("DELETE", endpoint)
    return response

def getEncryptedString(vmanage, type6encryption):
    """
    Get Type 6 Encryptedd String for a given value
    
    Parameters:
    type6encryption:	Type6 Encryption
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/security/encryptText/encrypt"
    response = vmanage.client.apiCall("POST", endpoint, type6encryption)
    return response
