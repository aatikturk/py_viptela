from query_builder import Builder
import HttpMethods

class WCM(object):
    """
    Partner - WCM Configs API
    
    Implements GET POST DEL PUT methods for WCMConfigs endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def pushNetconfConfigs(self, config, nmsId):
        """
        Push device configs
        
        Parameters:
        config:	            Netconf configuration
		nmsId	 (string):	NMS Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/partner/wcm/netconf/{nmsId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, config)
        return response


