from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class SigDC(object):
    """
    Configuration - Policy Secure internet gateway data centers Builder API
    
    Implements GET POST DEL PUT methods for PolicySecureinternetgatewaydatacentersBuilder endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getSigDataCenterList(self, type):
        """
        Get list of data centers for zscaler or umbrella
        
        Parameters:
        type	 (string):	Provider type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sig/datacenters/{type}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


