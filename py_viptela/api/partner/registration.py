from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def getPartners(vmanage):
    """
    Get all NMS partners
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/partner"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getVPNList(vmanage):
    """
    Get all VPNs
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/partner/vpn"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def getPartnersByType(vmanage, partnerType):
    """
    Get NMS partners by partner type
    
    Parameters:
    partnerType	 (string):	Partner type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/partner/{partnerType}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def registerPartner(vmanage, partner, partnerType):
    """
    Register NMS partner
    
    Parameters:
    partner:	Partner
	partnerType	 (string):	Partner type
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/partner/{partnerType}"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, partner)
    return response
def getPartnerDevices(vmanage, partnerType, nmsId):
    """
    List mapped devices for the partner
    
    Parameters:
    partnerType     (string):   Partner type
	nmsId	        (string):	NMS Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/partner/{partnerType}/map/{nmsId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def mapDevices(vmanage, listofdevices, partnerType, nmsId):
    """
    Map devices for the partner
    
    Parameters:
    listofdevices:	            List of devices
	partnerType	    (string):	Partner type
	nmsId	        (string):	NMS Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/partner/{partnerType}/map/{nmsId}"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, listofdevices)
    return response
def unmapDevices(vmanage, partnerType, nmsId):
    """
    Unmap all devices for the partner
    
    Parameters:
    partnerType     (string):   Partner type
	nmsId	        (string):	NMS Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/partner/{partnerType}/map/{nmsId}"
    response = vmanage.client.apiCall(HttpMethods.DELETE, endpoint)
    return response
def deleteDeviceMapping(vmanage, listofdevices, partnerType, nmsId):
    """
    Unmap a set of devices for the partner
    
    Parameters:
    listofdevices:	List of devices
	partnerType	 (string):	Partner type
	nmsId	 (string):	NMS Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/partner/{partnerType}/unmap/{nmsId}"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, listofdevices)
    return response
def getPartner(vmanage, partnerType, nmsId):
    """
    Get NMS partners by partner type and Id
    
    Parameters:
    partnerType	 (string):	Partner type
	nmsId	 (string):	NMS Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/partner/{partnerType}/{nmsId}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def updatePartner(vmanage, partner, partnerType, nmsId):
    """
    Update NMS partner details
    
    Parameters:
    partner:	                Partner
	partnerType	    (string):	Partner type
	nmsId	        (string):	NMS Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/partner/{partnerType}/{nmsId}"
    response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, partner)
    return response
def deletePartner(vmanage, partnerType, nmsId):
    """
    Delete NMS partner
    
    Parameters:
    partnerType	    (string):	Partner type
	nmsId	        (string):	NMS Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/partner/{partnerType}/{nmsId}"
    response = vmanage.client.apiCall(HttpMethods.DELETE, endpoint)
    return response
def getDataChangeInfo(vmanage, partnerId, event_id, eventNames, wait_time):
    """
    Retrieve registration change information
    
    Parameters:
    partnerId	 (string):	Partner Id
	event_id	 (string):	Continuation token of ongoing event-polling session
	eventNames	 (array):	Names of type of events to filter on
	wait_time	 (integer):	Maximum polling wait time in seconds
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/serverlongpoll/event/poll/{partnerId}?event_id={event_id}&eventNames={eventNames}&wait_time={wait_time}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
