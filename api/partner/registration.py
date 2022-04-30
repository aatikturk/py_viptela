from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Registration(object):
    """
    Partner - Registration API
    
    Implements GET POST DEL PUT methods for Registration endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getPartners(self):
        """
        Get all NMS partners
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getVPNList(self):
        """
        Get all VPNs
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner/vpn"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getPartnersByType(self, partnerType):
        """
        Get NMS partners by partner type
        
        Parameters:
        partnerType	 (string):	Partner type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner/{partnerType}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def registerPartner(self, partner, partnerType):
        """
        Register NMS partner
        
        Parameters:
        partner:	Partner
		partnerType	 (string):	Partner type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner/{partnerType}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, partner)
        return response


    def getPartnerDevices(self, partnerType, nmsId):
        """
        List mapped devices for the partner
        
        Parameters:
        partnerType     (string):   Partner type
		nmsId	        (string):	NMS Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner/{partnerType}/map/{nmsId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def mapDevices(self, listofdevices, partnerType, nmsId):
        """
        Map devices for the partner
        
        Parameters:
        listofdevices:	            List of devices
		partnerType	    (string):	Partner type
		nmsId	        (string):	NMS Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner/{partnerType}/map/{nmsId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, listofdevices)
        return response


    def unmapDevices(self, partnerType, nmsId):
        """
        Unmap all devices for the partner
        
        Parameters:
        partnerType     (string):   Partner type
		nmsId	        (string):	NMS Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner/{partnerType}/map/{nmsId}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def deleteDeviceMapping(self, listofdevices, partnerType, nmsId):
        """
        Unmap a set of devices for the partner
        
        Parameters:
        listofdevices:	List of devices
		partnerType	 (string):	Partner type
		nmsId	 (string):	NMS Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner/{partnerType}/unmap/{nmsId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, listofdevices)
        return response


    def getPartner(self, partnerType, nmsId):
        """
        Get NMS partners by partner type and Id
        
        Parameters:
        partnerType	 (string):	Partner type
		nmsId	 (string):	NMS Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner/{partnerType}/{nmsId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updatePartner(self, partner, partnerType, nmsId):
        """
        Update NMS partner details
        
        Parameters:
        partner:	                Partner
		partnerType	    (string):	Partner type
		nmsId	        (string):	NMS Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner/{partnerType}/{nmsId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, partner)
        return response


    def deletePartner(self, partnerType, nmsId):
        """
        Delete NMS partner
        
        Parameters:
        partnerType	    (string):	Partner type
		nmsId	        (string):	NMS Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner/{partnerType}/{nmsId}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def getDataChangeInfo(self, partnerId, event_id, eventNames, wait_time):
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
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/serverlongpoll/event/poll/{partnerId}?event_id={event_id}&eventNames={eventNames}&wait_time={wait_time}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


