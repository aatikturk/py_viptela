def sleauthenticate(vmanage, partner):
    """
    authenticate user for sle
    
    Parameters:
    partner:	Partner
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/smartLicensing/authenticate"
    response = vmanage.apiCall("POST", endpoint, partner)
    return response
def fetchAccounts(vmanage, partner, mode):
    """
    fetch sava for sle
    
    Parameters:
    partner:	Partner
	mode	 (string):	mode
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/smartLicensing/fetchAccounts?mode={mode}"
    response = vmanage.apiCall("GET", endpoint, partner)
    return response
def fetchReports(vmanage, partner):
    """
    fetch reports offline for sle
    
    Parameters:
    partner:	Partner
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/smartLicensing/fetchAllSa"
    response = vmanage.apiCall("GET", endpoint, partner)
    return response
def fetchReports(vmanage, partner, saDomain, saId):
    """
    fetch reports offline for sle
    
    Parameters:
    partner:	Partner
	saDomain	 (string):	saDomain
	saId	 (string):	saId
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/smartLicensing/fetchReportsForSa?saDomain={saDomain}&saId={saId}"
    response = vmanage.apiCall("GET", endpoint, partner)
    return response
def getUserSettings(vmanage):
    """
    get settings
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/smartLicensing/getUserSettings"
    response = vmanage.apiCall("GET", endpoint)
    return response
def syncLicenses(vmanage, partner):
    """
    get all licenses for sa/va
    
    Parameters:
    partner:	Partner
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/smartLicensing/removeSaVaSelection"
    response = vmanage.apiCall("POST", endpoint, partner)
    return response
def syncLicenses(vmanage, partner):
    """
    get all licenses for sa/va
    
    Parameters:
    partner:	Partner
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/smartLicensing/syncLicenses"
    response = vmanage.apiCall("POST", endpoint, partner)
    return response
def uploadAck(vmanage, partner):
    """
    upload ack file  for sa/va
    
    Parameters:
    partner:	Partner
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/smartLicensing/uploadAck"
    response = vmanage.apiCall("POST", endpoint, partner)
    return response
