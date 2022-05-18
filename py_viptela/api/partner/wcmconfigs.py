from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class WCM(object):
    """
    Partner - WCM Configs API
    
    Implements GET POST DEL PUT methods for WCM Configs endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def pushConfigs(self, config, nmsId):
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


