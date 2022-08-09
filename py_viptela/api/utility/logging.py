def listLogFileDetails(vmanage):
    """
    Lists content of log file. This API accepts content type as text/plain. It is mandatory to provide response content type.  Any other content type would result in empty response.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    vmanage.client.session.headers['Content-Type'] = "text/plain"
    endpoint = f"dataservice/util/logfile/appserver"
    response = vmanage.apiCall("GET", endpoint)
    return response
def listVManageServerLogLastNLines(vmanage, lines):
    """
    List last N lines of log file. This API accepts content type as text/plain. It is mandatory to provide response content type.  Any other content type would result in empty response.
    
    Parameters:
    lines	 (integer):	Number of lines
    
    Returns
    response    (dict)
    
    
    """
    
    vmanage.client.session.headers['Content-Type'] = "text/plain"
    endpoint = f"dataservice/util/logfile/appserver/lastnlines?lines={lines}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def debugLog(vmanage, payload):
    """
    Test whether logging works
    
    Parameters:
    payload:	Request Payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/util/logging/debuglog"
    response = vmanage.apiCall("POST", endpoint, payload)
    return response
def setLogLevel(vmanage, payload):
    """
    Set log level for logger
    
    Parameters:
    payload:	Request Payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/util/logging/level"
    response = vmanage.apiCall("POST", endpoint, payload)
    return response
def listLoggers(vmanage):
    """
    List loggers
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/util/logging/loggers"
    response = vmanage.apiCall("GET", endpoint)
    return response
