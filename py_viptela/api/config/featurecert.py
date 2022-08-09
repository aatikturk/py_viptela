def getDeviceCert(vmanage, deviceId):
    """
    Get feature cert from cEdge device        
    NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/featurecertificate/certificate?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def install(vmanage, certRequest):
    """
    Upload feature cert for cEdge device        
    NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
    
    Parameters:
    certRequest:	Install feature cert request for cEdge
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/featurecertificate/certificate"
    response = vmanage.apiCall("PUT", endpoint, certRequest)
    return response

def getDeviceCsr(vmanage, deviceId):
    """
    Get CSR from cEdge device        
    NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/featurecertificate/devicecsr?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def genDeviceCsr(vmanage, csrRequest):
    """
    Create CSR for cEdge device        
    NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
    
    Parameters:
    csrRequest:	CSR request for cEdge
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/featurecertificate/devicecsr"
    response = vmanage.apiCall("PUT", endpoint, csrRequest)
    return response

def revoke(vmanage, revokeReq):
    """
    Revoke feature cert from cEdge device        
    NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
    
    Parameters:
    revokeReq:	Revoking feature cert request for cEdge
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/featurecertificate/revoke"
    response = vmanage.apiCall("PUT", endpoint, revokeReq)
    return response

def getFeatureCaState(vmanage):
    """
    Get Feature CA state        
    NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/featurecertificate/syslogconfig"
    response = vmanage.apiCall("GET", endpoint)
    return response
