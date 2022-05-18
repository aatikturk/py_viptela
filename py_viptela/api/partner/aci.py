from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class ACIPolicyBuilder(object):
    """
    Partner - ACI Policy Builder API
    
    Implements GET POST DEL PUT methods for ACI Policy Builder endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getACIDefinitions(self):
        """
        Get ACI definitions
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner/aci/policy"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDscpMappings(self, partnerId):
        """
        Get DSCP policy
        
        Parameters:
        partnerId	 (string):	Partner Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner/aci/policy/dscpmapping/{partnerId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createDscpMappings(self, acidefinition, partnerId):
        """
        Create an ACI definition entry
        
        Parameters:
        acidefinition:	ACI definition
		partnerId	 (string):	Partner Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner/aci/policy/dscpmapping/{partnerId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, acidefinition)
        return response


    def deleteDscpMappings(self, partnerId):
        """
        Delete DSCP mapping
        
        Parameters:
        partnerId	 (string):	Partner Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner/aci/policy/dscpmapping/{partnerId}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def getEvents(self, partnerId, starttime, endtime):
        """
        Get ACI events
        
        Parameters:
        partnerId	 (string):	Partner Id
		starttime	 (integer):	Start time
		endtime	 (integer):	End time
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner/aci/policy/events/{partnerId}?starttime={starttime}&endtime={endtime}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDataPrefixMappings(self, partnerId):
        """
        Get prefix mapping
        
        Parameters:
        partnerId	 (string):	Partner Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner/aci/policy/prefixmapping/{partnerId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def setDataPrefixMappings(self, prefixdefinition, partnerId):
        """
        Create data prefix mapping
        
        Parameters:
        prefixdefinition:	Prefix definition
		partnerId	 (string):	Partner Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner/aci/policy/prefixmapping/{partnerId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, prefixdefinition)
        return response


    def getDataPrefixSequences(self):
        """
        Get data prefix sequence
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner/aci/policy/sequences"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


