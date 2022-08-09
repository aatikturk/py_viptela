from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def editDeviceWithLicense(vmanage, license):
    """
    Update device subscription
    
    Parameters:
    license:	Subscription and license
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/msla/assignLicense"
    response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, license)
    return response
def createDeviceWithLicense(vmanage, license):
    """
    Create device subscription
    
    Parameters:
    license:	Subscription and license
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/msla/assignLicense"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, license)
    return response
def getMSLADevices(vmanage):
    """
    Retrieve devices subscription
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/msla/devices"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getDeviceDistributionOverview(vmanage):
    """
    Get device distribution 
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/msla/devices/assignmentdistribution"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getLicenseandDeviceOverview(vmanage):
    """
    Get license device overview 
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/msla/devices/licenseanddeviceoverviewtable"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getLicenseDistributionOverview(vmanage):
    """
    Get license distribution 
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/msla/devices/licensedistribution"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getSubscriptionOverview(vmanage):
    """
    Get subscription overview 
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/msla/devices/subscriptiondistribution"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getSubscriptions(vmanage, payload):
    """
    Retrieve MSLA subscription/licenses
    
    Parameters:
    payload:	Request Payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/msla/licenses/subscription"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, payload)
    return response
def syncLicenses(vmanage, synclicense):
    """
    Retrieve MSLA subscription/licenses
    
    Parameters:
    synclicense:	Sync license
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/msla/licenses/sync"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, synclicense)
    return response
def getlicensedDeviceCount(vmanage):
    """
    get license and device count
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/msla/monitoring/licensedDeviceCount"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getLicensedDistributionDetails(vmanage):
    """
    get license and device count
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/msla/monitoring/licensedDistributionDetails"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getpackagingDistributionDetails(vmanage):
    """
    get packaging distribution details
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/msla/monitoring/packagingDistributionDetails"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getSubscriptions(vmanage):
    """
    Retrieve subscriptions
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/msla/subscriptions"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getAllTemplate(vmanage):
    """
    Retrieve all MSLA template
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/msla/template"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getSubscriptions(vmanage, payload):
    """
    Retrieve MSLA subscription/licenses
    
    Parameters:
    payload:	Request Payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/msla/template/licenses"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, payload)
    return response
def getSubscriptions(vmanage, payload):
    """
    Retrieve MSLA subscription/licenses
    
    Parameters:
    payload:	Request Payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/msla/va/License"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, payload)
    return response
