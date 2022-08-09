
def getACIDefinitions(vmanage):
    """
    Get ACI definitions
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/partner/aci/policy"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getDscpMappings(vmanage, partnerId):
    """
    Get DSCP policy
    
    Parameters:
    partnerId	 (string):	Partner Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/partner/aci/policy/dscpmapping/{partnerId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def createDscpMappings(vmanage, acidefinition, partnerId):
    """
    Create an ACI definition entry
    
    Parameters:
    acidefinition:	ACI definition
	partnerId	 (string):	Partner Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/partner/aci/policy/dscpmapping/{partnerId}"
    response = vmanage.client.apiCall("POST", endpoint, acidefinition)
    return response
def deleteDscpMappings(vmanage, partnerId):
    """
    Delete DSCP mapping
    
    Parameters:
    partnerId	 (string):	Partner Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/partner/aci/policy/dscpmapping/{partnerId}"
    response = vmanage.client.apiCall("DELETE", endpoint)
    return response
def getEvents(vmanage, partnerId, starttime, endtime):
    """
    Get ACI events
    
    Parameters:
    partnerId	 (string):	Partner Id
	starttime	 (integer):	Start time
	endtime	 (integer):	End time
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/partner/aci/policy/events/{partnerId}?starttime={starttime}&endtime={endtime}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getDataPrefixMappings(vmanage, partnerId):
    """
    Get prefix mapping
    
    Parameters:
    partnerId	 (string):	Partner Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/partner/aci/policy/prefixmapping/{partnerId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def setDataPrefixMappings(vmanage, prefixdefinition, partnerId):
    """
    Create data prefix mapping
    
    Parameters:
    prefixdefinition:	Prefix definition
	partnerId	 (string):	Partner Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/partner/aci/policy/prefixmapping/{partnerId}"
    response = vmanage.client.apiCall("POST", endpoint, prefixdefinition)
    return response
def getDataPrefixSequences(vmanage):
    """
    Get data prefix sequence
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/partner/aci/policy/sequences"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
