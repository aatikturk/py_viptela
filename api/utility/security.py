from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Security(object):
    """
    Utility - Security API
    
    Implements GET POST DEL PUT methods for Security endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def checkGivenIpList(self, devicedetail):
        """
        Block IP based on list
        
        Parameters:
        devicedetail:	Device detail
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/software/compliance/ip/origin/check"
        response = self.client.apiCall(HttpMethods.POST, endpoint, devicedetail)
        return response


