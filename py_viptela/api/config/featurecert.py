from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def getDeviceCert(vmanage, deviceId):
    """
    Get feature cert from cEdge device        
    NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/featurecertificate/certificate?deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
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
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/featurecertificate/certificate"
    response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, certRequest)
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
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/featurecertificate/devicecsr?deviceId={deviceId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
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
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/featurecertificate/devicecsr"
    response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, csrRequest)
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
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/featurecertificate/revoke"
    response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, revokeReq)
    return response

def getFeatureCaState(vmanage):
    """
    Get Feature CA state        
    NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/featurecertificate/syslogconfig"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
