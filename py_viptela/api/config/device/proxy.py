def getSelfSignedCert(vmanage):
    """
    get self signed certificate
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/certificate/vmanage/selfsignedcert"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getProxyCertOfEdge(vmanage, deviceId):
    """
    Get edge proxy certificate
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sslproxy/certificate?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def updateCert(vmanage, cert):
    """
    Upload device certificate
    
    Parameters:
    cert:	Upload device certificate
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sslproxy/certificate"
    response = vmanage.apiCall("PUT", endpoint, cert)
    return response

def addWANEdge(vmanage, certstate, deviceId):
    """
    Add SSL proxy wan edge
    
    Parameters:
    certstate:	Cert state
	deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sslproxy/certificate/wanedge/{deviceId}"
    response = vmanage.apiCall("POST", endpoint, certstate)
    return response

def uploadCerts(vmanage, certFile):
    """
    Upload device certificates
    
    Parameters:
    certFile:	Certificate file
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sslproxy/certificates"
    response = vmanage.apiCall("POST", endpoint, certFile)
    return response

def getSslProxyCSR(vmanage, deviceId):
    """
    Get SSL proxy CSR
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sslproxy/csr?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getAllDeviceCerts(vmanage, devicelist):
    """
    Get certificate for all cEdges
    
    Parameters:
    devicelist:	Device list
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sslproxy/devicecertificates"
    response = vmanage.apiCall("POST", endpoint, devicelist)
    return response

def getAllDeviceCSR(vmanage, devicelist):
    """
    Get CSR for all cEdges
    
    Parameters:
    devicelist:	Device list
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sslproxy/devicecsr"
    response = vmanage.apiCall("POST", endpoint, devicelist)
    return response

def generateSslProxyCSR(vmanage, csrRequest):
    """
    CSR request SSL proxy for edge
    
    Parameters:
    csrRequest:	CSR request for edge
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sslproxy/generate/csr/sslproxy"
    response = vmanage.apiCall("POST", endpoint, csrRequest)
    return response

def generateSSLProxyCSR(vmanage, csrRequest):
    """
    Generate CSR
    
    Parameters:
    csrRequest:	CSR request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sslproxy/generate/vmanage/csr"
    response = vmanage.apiCall("POST", endpoint, csrRequest)
    return response

def getSslProxyList(vmanage):
    """
    Get SSL proxy certificate list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sslproxy/list"
    response = vmanage.apiCall("GET", endpoint)
    return response

def renewCert(vmanage, certRequest):
    """
    Renew device certificate
    
    Parameters:
    certRequest:	Renew device certificate request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sslproxy/renew"
    response = vmanage.apiCall("POST", endpoint, certRequest)
    return response

def revokeCert(vmanage, certRequest):
    """
    Revoke device certificate
    
    Parameters:
    certRequest:	Revoke device certificate request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sslproxy/revoke"
    response = vmanage.apiCall("POST", endpoint, certRequest)
    return response

def revokeRenewCert(vmanage, certRequest):
    """
    Revoke and renew device certificate
    
    Parameters:
    certRequest:	Revoke device certificate request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sslproxy/revokerenew"
    response = vmanage.apiCall("POST", endpoint, certRequest)
    return response

def getCertState(vmanage):
    """
    Get certificate state
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sslproxy/settings/certificate"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getEntCert(vmanage):
    """
    Get enterprise certificate
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sslproxy/settings/enterprise/certificate"
    response = vmanage.apiCall("GET", endpoint)
    return response

def setEntCert(vmanage, certRequest):
    """
    Configure enterprise certificate
    
    Parameters:
    certRequest:	Config enterprise certificate request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sslproxy/settings/enterprise/certificate"
    response = vmanage.apiCall("POST", endpoint, certRequest)
    return response

def getVManageEntRootCert(vmanage):
    """
    Get vManage enterprise root certificate
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sslproxy/settings/enterprise/rootca"
    response = vmanage.apiCall("GET", endpoint)
    return response

def setEntRootCaCert(vmanage, certRequest):
    """
    Set vManage enterprise root certificate
    
    Parameters:
    setenterpriserootcarequest:	Set enterprise root CA request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sslproxy/settings/enterprise/rootca"
    response = vmanage.apiCall("POST", endpoint, certRequest)
    return response

def getvManageCert(vmanage):
    """
    Get vManage intermediate certificate
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sslproxy/settings/vmanage/certificate"
    response = vmanage.apiCall("GET", endpoint)
    return response

def setvManageintermediateCert(vmanage, certRequest):
    """
    Set vManage root certificate
    
    Parameters:
    certRequest:	Set vManage intermediate CA request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sslproxy/settings/vmanage/certificate"
    response = vmanage.apiCall("POST", endpoint, certRequest)
    return response

def getvManageCSR(vmanage):
    """
    Get vManage CSR
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sslproxy/settings/vmanage/csr"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getvManageRootCA(vmanage):
    """
    Get vManage root certificate
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sslproxy/settings/vmanage/rootca"
    response = vmanage.apiCall("GET", endpoint)
    return response

def setvManageRootCA(vmanage, certRequest):
    """
    Set vManage root certificate
    
    Parameters:
    certRequest:	Set vManage root CA request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/sslproxy/settings/vmanage/rootca"
    response = vmanage.apiCall("POST", endpoint, certRequest)
    return response
