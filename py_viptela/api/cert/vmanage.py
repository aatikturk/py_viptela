def showInfo(vmanage):
    """
    Retrieves Certificate Signing Request information
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/setting/configuration/webserver/certificate"
    response = vmanage.apiCall("GET", endpoint)
    return response

def importCert(vmanage, signedCert):
    """
    Import a signed web server certificate
    
    Parameters:
    signedCert:	Singed certificate
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/setting/configuration/webserver/certificate"
    response = vmanage.apiCall("PUT", endpoint, signedCert)
    return response

def getCSR(vmanage, csrRequest):
    """
    Generate Certificate Signing Request
    
    Parameters:
    csrRequest:	CSR signing request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/setting/configuration/webserver/certificate"
    response = vmanage.apiCall("POST", endpoint, csrRequest)
    return response

def dumpCert(vmanage, type):
    """
    Get certificate with alias name
    
    Parameters:
    type	 (string):	Key alias
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/setting/configuration/webserver/certificate/certificate?type={type}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getCert(vmanage):
    """
    Get certificate for alias server
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/setting/configuration/webserver/certificate/getcertificate"
    response = vmanage.apiCall("GET", endpoint)
    return response

def rollback(vmanage, type):
    """
    Rollback certificate with alias name
    
    Parameters:
    type	 (string):	Key alias
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/setting/configuration/webserver/certificate/rollback?type={type}"
    response = vmanage.apiCall("GET", endpoint)
    return response
