def getSelfSignedCert(vmanage):
    """
    get self signed certificate
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/vmanage/selfsignedcert"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getProxyCertOfEdge(vmanage, deviceId):
    """
    Get edge proxy certificate
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sslproxy/certificate?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def updateCert(vmanage, cert):
    """
    Upload device certificate
    
    Parameters:
    cert:	Upload device certificate
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sslproxy/certificate"
    response = vmanage.client.apiCall("PUT", endpoint, cert)
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
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sslproxy/certificate/wanedge/{deviceId}"
    response = vmanage.client.apiCall("POST", endpoint, certstate)
    return response

def uploadCerts(vmanage, certFile):
    """
    Upload device certificates
    
    Parameters:
    certFile:	Certificate file
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sslproxy/certificates"
    response = vmanage.client.apiCall("POST", endpoint, certFile)
    return response

def getSslProxyCSR(vmanage, deviceId):
    """
    Get SSL proxy CSR
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sslproxy/csr?deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getAllDeviceCerts(vmanage, devicelist):
    """
    Get certificate for all cEdges
    
    Parameters:
    devicelist:	Device list
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sslproxy/devicecertificates"
    response = vmanage.client.apiCall("POST", endpoint, devicelist)
    return response

def getAllDeviceCSR(vmanage, devicelist):
    """
    Get CSR for all cEdges
    
    Parameters:
    devicelist:	Device list
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sslproxy/devicecsr"
    response = vmanage.client.apiCall("POST", endpoint, devicelist)
    return response

def generateSslProxyCSR(vmanage, csrRequest):
    """
    CSR request SSL proxy for edge
    
    Parameters:
    csrRequest:	CSR request for edge
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sslproxy/generate/csr/sslproxy"
    response = vmanage.client.apiCall("POST", endpoint, csrRequest)
    return response

def generateSSLProxyCSR(vmanage, csrRequest):
    """
    Generate CSR
    
    Parameters:
    csrRequest:	CSR request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sslproxy/generate/vmanage/csr"
    response = vmanage.client.apiCall("POST", endpoint, csrRequest)
    return response

def getSslProxyList(vmanage):
    """
    Get SSL proxy certificate list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sslproxy/list"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def renewCert(vmanage, certRequest):
    """
    Renew device certificate
    
    Parameters:
    certRequest:	Renew device certificate request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sslproxy/renew"
    response = vmanage.client.apiCall("POST", endpoint, certRequest)
    return response

def revokeCert(vmanage, certRequest):
    """
    Revoke device certificate
    
    Parameters:
    certRequest:	Revoke device certificate request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sslproxy/revoke"
    response = vmanage.client.apiCall("POST", endpoint, certRequest)
    return response

def revokeRenewCert(vmanage, certRequest):
    """
    Revoke and renew device certificate
    
    Parameters:
    certRequest:	Revoke device certificate request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sslproxy/revokerenew"
    response = vmanage.client.apiCall("POST", endpoint, certRequest)
    return response

def getCertState(vmanage):
    """
    Get certificate state
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sslproxy/settings/certificate"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getEntCert(vmanage):
    """
    Get enterprise certificate
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sslproxy/settings/enterprise/certificate"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def setEntCert(vmanage, certRequest):
    """
    Configure enterprise certificate
    
    Parameters:
    certRequest:	Config enterprise certificate request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sslproxy/settings/enterprise/certificate"
    response = vmanage.client.apiCall("POST", endpoint, certRequest)
    return response

def getVManageEntRootCert(vmanage):
    """
    Get vManage enterprise root certificate
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sslproxy/settings/enterprise/rootca"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def setEntRootCaCert(vmanage, certRequest):
    """
    Set vManage enterprise root certificate
    
    Parameters:
    setenterpriserootcarequest:	Set enterprise root CA request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sslproxy/settings/enterprise/rootca"
    response = vmanage.client.apiCall("POST", endpoint, certRequest)
    return response

def getvManageCert(vmanage):
    """
    Get vManage intermediate certificate
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sslproxy/settings/vmanage/certificate"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def setvManageintermediateCert(vmanage, certRequest):
    """
    Set vManage root certificate
    
    Parameters:
    certRequest:	Set vManage intermediate CA request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sslproxy/settings/vmanage/certificate"
    response = vmanage.client.apiCall("POST", endpoint, certRequest)
    return response

def getvManageCSR(vmanage):
    """
    Get vManage CSR
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sslproxy/settings/vmanage/csr"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getvManageRootCA(vmanage):
    """
    Get vManage root certificate
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sslproxy/settings/vmanage/rootca"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def setvManageRootCA(vmanage, certRequest):
    """
    Set vManage root certificate
    
    Parameters:
    certRequest:	Set vManage root CA request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/sslproxy/settings/vmanage/rootca"
    response = vmanage.client.apiCall("POST", endpoint, certRequest)
    return response
