def pushMasterBootstrap(vmanage, bootstrapTemplate):
    """
    Attach bootstrap template to device
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    bootstrapTemplate:	Device template
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/config/attachBootStrap"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, bootstrapTemplate)
    return response

def pushCLITemplate(vmanage, devicetemplate):
    """
    Attach CLI device template
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    devicetemplate:	Device template
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/config/attachcli"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, devicetemplate)
    return response

def editCloudxConfig(vmanage, cloudxconfig):
    """
    Edit already enabled gateways, clients, dias
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    cloudxconfig:	CloudX config
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/config/attachcloudx"
    response = vmanage.client.apiCall(vmanage.PUT, endpoint, cloudxconfig)
    return response

def pushCloudxConfig(vmanage, cloudxconfig):
    """
    Enable gateways, clients, dias
    
    Parameters:
    cloudxconfig:	CloudX config
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/config/attachcloudx"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, cloudxconfig)
    return response

def getAttachedDeviceList(vmanage, masterTemplateId):
    """
    Get attached device list by master template Id
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    masterTemplateId	 (string):	Template Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/config/attached/{masterTemplateId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getAttachedConfigToDevice(vmanage, deviceId):
    """
    Get attached config to device
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    deviceId	 (string):	Device Model ID
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/config/attachedconfig?deviceId={deviceId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def pushMasterTemplate(vmanage, devicetemplate):
    """
    Attach feature device template
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    devicetemplate:	Device template
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/config/attachfeature"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, devicetemplate)
    return response

def attachDeviceTemplate(vmanage, devicetemplate):
    """
    Attach device template
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    devicetemplate:	Device template
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/config/attachment"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, devicetemplate)
    return response

def getDeviceListByMasterTemplateId(vmanage, masterTemplateId):
    """
    Get possible device list by master template Id
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    masterTemplateId	 (string):	Template Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/config/available/{masterTemplateId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def getDeviceConfigurationPreview(vmanage, devicetemplate):
    """
    Get device configuration
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    devicetemplate:	Device template
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/config/config"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, devicetemplate)
    return response

def detachDeviceTemplate(vmanage, devicetemplate):
    """
    Detach device template
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    devicetemplate:	Device template
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/config/detach"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, devicetemplate)
    return response

def detachSites(vmanage, cloudxconfig):
    """
    Disable enabled gateways, clients, dias
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    cloudxconfig:	CloudX config
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/config/detachcloudx"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, cloudxconfig)
    return response

def getDevicesWithDuplicateIP(vmanage, devicelist):
    """
    Detects duplicate system IP from a list of devices
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    devicelist:	Device list
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/config/duplicateip"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, devicelist)
    return response

def createInputWithoutDevice(vmanage, devicetemplate):
    """
    Export the device template to CSV format for given template id
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    devicetemplate:	Device template
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/config/exportcsv"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, devicetemplate)
    return response

def createDeviceInput(vmanage, templatedeviceinput):
    """
    Create device input
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    templatedeviceinput:	Template device input
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/config/input"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, templatedeviceinput)
    return response

def processInputCommaSepFile(vmanage, devicetemplate):
    """
    Process input comma separated file
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    devicetemplate:	Device template
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/config/process/input/file"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, devicetemplate)
    return response

def getQuickConnectVariables(vmanage, devicelist):
    """
    Get connection variables to be configured
    
    Parameters:
    devicelist:	Device List
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/config/quickconnectvariable"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, devicelist)
    return response

def checkVbond(vmanage):
    """
    Check if vBond is configured
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/config/vbond"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def validateTemplate(vmanage, payload):
    """
    Validate full template"
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    payload:	Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/device/config/verify"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, payload)
    return response
