def editDeviceWithLicense(vmanage, license):
    """
    Update device subscription
    
    Parameters:
    license:	Subscription and license
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/msla/assignLicense"
    response = vmanage.apiCall("PUT", endpoint, license)
    return response
def createDeviceWithLicense(vmanage, license):
    """
    Create device subscription
    
    Parameters:
    license:	Subscription and license
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/msla/assignLicense"
    response = vmanage.apiCall("POST", endpoint, license)
    return response
def getMSLADevices(vmanage):
    """
    Retrieve devices subscription
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/msla/devices"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getDeviceDistributionOverview(vmanage):
    """
    Get device distribution 
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/msla/devices/assignmentdistribution"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getLicenseandDeviceOverview(vmanage):
    """
    Get license device overview 
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/msla/devices/licenseanddeviceoverviewtable"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getLicenseDistributionOverview(vmanage):
    """
    Get license distribution 
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/msla/devices/licensedistribution"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getSubscriptionOverview(vmanage):
    """
    Get subscription overview 
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/msla/devices/subscriptiondistribution"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getLicenseSubscriptions(vmanage, payload):
    """
    Retrieve MSLA subscription/licenses
    
    Parameters:
    payload:	Request Payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/msla/licenses/subscription"
    response = vmanage.apiCall("POST", endpoint, payload)
    return response
def syncLicenses(vmanage, synclicense):
    """
    Retrieve MSLA subscription/licenses
    
    Parameters:
    synclicense:	Sync license
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/msla/licenses/sync"
    response = vmanage.apiCall("POST", endpoint, synclicense)
    return response
def getlicensedDeviceCount(vmanage):
    """
    get license and device count
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/msla/monitoring/licensedDeviceCount"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getLicensedDistributionDetails(vmanage):
    """
    get license and device count
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/msla/monitoring/licensedDistributionDetails"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getpackagingDistributionDetails(vmanage):
    """
    get packaging distribution details
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/msla/monitoring/packagingDistributionDetails"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getSubscriptions(vmanage):
    """
    Retrieve subscriptions
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/msla/subscriptions"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getAllTemplate(vmanage):
    """
    Retrieve all MSLA template
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/msla/template"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getTempLicenseSubscriptions(vmanage, payload):
    """
    Retrieve MSLA subscription/licenses
    
    Parameters:
    payload:	Request Payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/msla/template/licenses"
    response = vmanage.apiCall("POST", endpoint, payload)
    return response
def getVaLicenseSubscriptions(vmanage, payload):
    """
    Retrieve MSLA subscription/licenses
    
    Parameters:
    payload:	Request Payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/msla/va/License"
    response = vmanage.apiCall("POST", endpoint, payload)
    return response
