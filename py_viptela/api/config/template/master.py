def getMasterTemplateList(vmanage, feature):
    """
    Generate template list
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    feature	 (string):	Feature
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device?feature={feature}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def createCLITemplate(vmanage, createtemplaterequest):
    """
    Create CLI template
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    createtemplaterequest:	Create template request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/cli"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, createtemplaterequest)
    return response

def createMasterTemplate(vmanage, request):
    """
    Create a device template from feature templates and sub templates
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    request:	Create template request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/feature"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, request)
    return response

def isMigrationRequired(vmanage):
    """
    Check if any device templates need migration
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/is_migration_required"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getTemplateForMigration(vmanage, hasAAA):
    """
    Generate a list of templates which require migration
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    hasAAA	 (boolean):	Return only those uses AAA
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/migration?hasAAA={hasAAA}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def migrateTemplates(vmanage, id, prefix, includeAll):
    """
    Migrate the device templates given the template Ids
    
    Parameters:
    id	 (array):	Template Id
	prefix	 (string):	Prefix
	includeAll	 (boolean):	Include all flag
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/migration?id={id}&prefix={prefix}&includeAll={includeAll}"
    response = vmanage.client.apiCall(vmanage.POST, endpoint)
    return response

def migrationInfo(vmanage):
    """
    Returns the mapping between old and migrated templates
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/migration_info"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getMasterTemplateDefinition(vmanage, templateId):
    """
    Generate template by Id
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    templateId	 (string):	Template Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/object/{templateId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def changeTemplateResourceGroup(vmanage, templateId, resourceGroupName):
    """
    Change template resource group
    
    Parameters:
    templateId	 (string):	Template Id
	resourceGroupName	 (string):	Resource group name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/resource-group/{resourceGroupName}/{templateId}"
    response = vmanage.client.apiCall(vmanage.POST, endpoint)
    return response

def getOutOfSyncTemplates(vmanage):
    """
    Get template sync status
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/syncstatus"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getOutOfSyncDevices(vmanage, templateId):
    """
    Get out of sync devices
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    templateId	 (string):	Template Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/syncstatus/{templateId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def editMasterTemplate(vmanage, template, templateId):
    """
    Edit template
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    template:	Template
	templateId	 (string):	Template Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/{templateId}"
    response = vmanage.client.apiCall(vmanage.PUT, endpoint, template)
    return response

def deleteMasterTemplate(vmanage, templateId):
    """
    Delete template
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    templateId	 (string):	Template Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/{templateId}"
    response = vmanage.client.apiCall(vmanage.DELETE, endpoint)
    return response
