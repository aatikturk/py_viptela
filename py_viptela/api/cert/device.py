def getCertDetails(vmanage, parsecert):
    """
    Get cert details
    
    Parameters:
    parsecert:	parse cert
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/certdetails"
    response = vmanage.client.apiCall("POST", endpoint, parsecert)
    return response

def getCSRViewRightMenus(vmanage):
    """
    Get CSR detail view
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/csr/details"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getDeviceViewRightMenus(vmanage):
    """
    Get device detail view
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/device/details"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getDevicesList(vmanage):
    """
    Get vEdge list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/device/list"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def forceSyncRootCert(vmanage, singedcertificate):
    """
    Force sync root certificate
    NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
    
    Parameters:
    singedcertificate:	Singed certificate
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/forcesync/rootCert"
    response = vmanage.client.apiCall("POST", endpoint, singedcertificate)
    return response

def generateCSR(vmanage, csrRequest):
    """
    Generate CSR
    NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
    
    Parameters:
    csrRequest:	CSR request for device
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/generate/csr"
    response = vmanage.client.apiCall("POST", endpoint, csrRequest)
    return response

def generateEntCSR(vmanage, csrRequest):
    """
    Generate CSR
    NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
    
    Parameters:
    csrRequest:	CSR request for device
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/generate/enterprise/csr/vedge"
    response = vmanage.client.apiCall("POST", endpoint, csrRequest)
    return response

def generateVedgeEntCSR(vmanage, csrRequest):
    """
    Generate CSR
    NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
    
    Parameters:
    csrRequest:	CSR request for device
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/generate/wanedge/csr"
    response = vmanage.client.apiCall("POST", endpoint, csrRequest)
    return response

def installCertificate(vmanage, singedCert):
    """
    Install singed certificate
    NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
    
    Parameters:
    singedCert:	Singed certificate
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/install/signedCert"
    response = vmanage.client.apiCall("POST", endpoint, singedCert)
    return response

def updateJks(vmanage, updatejks):
    """
    update JKS
    NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
    
    Parameters:
    updatejks:	Update JKS
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/jks"
    response = vmanage.client.apiCall("PUT", endpoint, updatejks)
    return response

def getListStatus(vmanage):
    """
    get certificate
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/list/status"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getCertificateData(vmanage):
    """
    Get certificate chain
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/record"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def resetRSA(vmanage, csrRequest):
    """
    Register CSR
    NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
    
    Parameters:
    csrRequest:	CSR request for vEdge
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/reset/rsa"
    response = vmanage.client.apiCall("POST", endpoint, csrRequest)
    return response

def decommissionEnterpriseCSRForVedge(vmanage, revokingcsrforhardwarevedge):
    """
    Revoking enterprise CSR for hardware vEdge
    NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
    
    Parameters:
    revokingcsrforhardwarevedge:	Revoking CSR for hardware vEdge
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/revoke/enterprise/certificate"
    response = vmanage.client.apiCall("POST", endpoint, revokingcsrforhardwarevedge)
    return response

def getRootCertChains(vmanage, action):
    """
    Get root cert chain
    
    Parameters:
    action	 (string):	Action
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/rootcertchains?action={action}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def saveRootCertChain(vmanage, rootChain):
    """
    Save root cert chain
    NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
    
    Parameters:
    rootChain:	Save root cert chain
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/rootcertchains"
    response = vmanage.client.apiCall("PUT", endpoint, rootChain)
    return response

def getRootCertificate(vmanage):
    """
    Get device root certificate detail view
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/rootcertificate"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def saveVEdgeList(vmanage, deviceList):
    """
    Save vEdge device list
    
    Parameters:
    deviceList:	vEdge device list
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/save/vedge/list"
    response = vmanage.client.apiCall("POST", endpoint, deviceList)
    return response

def getCertificateDetail(vmanage):
    """
    Get certificate detail
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/stats/detail"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getCertificateStats(vmanage):
    """
    Get certificate expiration status
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/stats/summary"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def syncvBond(vmanage):
    """
    sync vManage UUID to all vBond
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/syncvbond"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getcEdgeList(vmanage):
    """
    Get cEdge list with tokengenerated list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/tokengeneratedlist"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getInstalledCert(vmanage):
    """
    Get Installed Certificate
    NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/vedge"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getvEdgeCSR(vmanage):
    """
    Get vEdge CSR Certificate
    NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/vedge/csr"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getvEdgeList(vmanage, model, state):
    """
    Get vEdge list
    
    Parameters:
    model	 (string):	Device model
	state	 (array):	Device state
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/vedge/list?model={model}&state={state}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def setvEdgeList(vmanage, deviceList):
    """
    Save vEdge list
    
    Parameters:
    deviceList:	vEdge device list
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/vedge/list"
    response = vmanage.client.apiCall("POST", endpoint, deviceList)
    return response

def getView(vmanage):
    """
    Get certificate UI view
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/view"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def getvSmartList(vmanage):
    """
    Get vSmart list
    NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/vsmart/list"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def setvSmartList(vmanage):
    """
    Save vSmart list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/vsmart/list"
    response = vmanage.client.apiCall("POST", endpoint)
    return response

def deleteConfig(vmanage, uuid, replaceController, deviceId):
    """
    Invalidate device
    NOTE: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.
    
    Parameters:
    uuid	                (string):	Device uuid
	replaceController	    (boolean):	Replace a vSmart in Multi-tenant setup with a new vSmart
	deviceId	            (string):	uuid of new vSmart
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/certificate/{uuid}?replaceController={replaceController}&deviceId={deviceId}"
    response = vmanage.client.apiCall("DELETE", endpoint)
    return response
