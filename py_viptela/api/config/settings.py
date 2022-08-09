def getBanner(vmanage):
    """
    Retrieve banner
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/settings/banner"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getSessionTimout(vmanage):
    """
    Get client session timeout
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/settings/clientSessionTimeout"
    response = vmanage.apiCall("GET", endpoint)
    return response

def createAnalyticsDataFile(vmanage):
    """
    Create analytics data file
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/settings/configuration/analytics/dca"
    response = vmanage.apiCall("POST", endpoint)
    return response

def getCertConfig(vmanage, settingType):
    """
    Retrieve certificate configuration value by settingType
    
    Parameters:
    settingType	 (string):	Setting type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/settings/configuration/certificate/{settingType}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def editCertConfig(vmanage, certConfig, settingType):
    """
    Update certificate configuration
    
    Parameters:
    certConfig:	Certificate config
	settingType	 (string):	Setting type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/settings/configuration/certificate/{settingType}"
    response = vmanage.apiCall("PUT", endpoint, certConfig)
    return response

def newCertConfig(vmanage, certConfig, settingType):
    """
    Add new certificate configuration
    
    Parameters:
    certConfig:	Certificate config
	settingType	 (string):	Setting type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/settings/configuration/certificate/{settingType}"
    response = vmanage.apiCall("POST", endpoint, certConfig)
    return response

def getGoogleMapKey(vmanage):
    """
    Retrieve Google map key
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/settings/configuration/googleMapKey"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getMaintenanceWindow(vmanage):
    """
    Retrieve maintenance window
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/settings/configuration/maintenanceWindow"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getConfigBySettingType(vmanage, settingType):
    """
    Retrieve configuration value by settingType
    
    Parameters:
    settingType	 (string):	Setting type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/settings/configuration/{settingType}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def editConfig(vmanage, configSetting, settingType):
    """
    Update configuration setting
    
    Parameters:
    configSetting:	Configuration setting
	settingType	 (string):	Setting type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/settings/configuration/{settingType}"
    response = vmanage.apiCall("PUT", endpoint, configSetting)
    return response

def newConfig(vmanage, configSetting, settingType):
    """
    Add new configuration
    
    Parameters:
    configSetting:	Configuration setting
	settingType	 (string):	Setting type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/settings/configuration/{settingType}"
    response = vmanage.apiCall("POST", endpoint, configSetting)
    return response
