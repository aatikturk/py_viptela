def getAccessTokenforDevice(vmanage):
    """
    getAccessTokenforDevice Description
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/cloudservices/accesstoken"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getAzureToken(vmanage, bodyParameter):
    """
    Get Azure token
    
    Parameters:
    bodyParameter:	Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/cloudservices/authtoken"
    response = vmanage.client.apiCall("POST", endpoint, bodyParameter)
    return response
def connect(vmanage):
    """
    Telemetry Opt In
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/cloudservices/connect"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getCloudCreds(vmanage):
    """
    Get cloud service credentials
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/cloudservices/credentials"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def addCloudCreds(vmanage, bodyParameter):
    """
    Get cloud service settings
    
    Parameters:
    bodyParameter:	Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/cloudservices/credentials"
    response = vmanage.client.apiCall("POST", endpoint, bodyParameter)
    return response
def getDeviceCode(vmanage):
    """
    Get Azure device code
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/cloudservices/devicecode"
    response = vmanage.client.apiCall("POST", endpoint)
    return response
def isStaging(vmanage):
    """
    Check if testbed or production
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/cloudservices/staging"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getTelemetryState(vmanage):
    """
    Get Telemetry state
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/cloudservices/telemetry"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def optIn(vmanage, bodyParameter):
    """
    Telemetry Opt In
    
    Parameters:
    bodyParameter:	Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/cloudservices/telemetry/optin"
    response = vmanage.client.apiCall("PUT", endpoint, bodyParameter)
    return response
def optOut(vmanage, bodyParameter):
    """
    Telemetry Opt Out
    
    Parameters:
    bodyParameter:	Description
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/cloudservices/telemetry/optout"
    response = vmanage.client.apiCall("DELETE", endpoint, bodyParameter)
    return response
def getCloudSettings(vmanage):
    """
    Get cloud service settings
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/dca/cloudservices"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getOTP(vmanage):
    """
    Get cloud service OTP value
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/dca/cloudservices/otp"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def updatetOTP(vmanage, cloudserviceotpvalue):
    """
    Update cloud service OTP value
    
    Parameters:
    cloudserviceotpvalue:	Cloud service OTP value
    
    Returns
    response    (dict)
    
    
    """
    
    vmanage.client.session.headers['Content-Type'] = "application/octet-stream"
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/dca/cloudservices/otp"
    response = vmanage.client.apiCall("PUT", endpoint, cloudserviceotpvalue)
    return response
def listEntityOwnerInfo(vmanage):
    """
    List all entity ownership info
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/entityownership/list"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def entityOwnerInfo(vmanage):
    """
    Entity ownership info grouped by buckets
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/entityownership/tree"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
