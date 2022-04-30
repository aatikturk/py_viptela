from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Locale(object):
    """
    Locale API
    
    Implements GET POST DEL PUT methods for Locale endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getsupportedLocales(self):
        """
        Get Supported locales
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/localization/supportedLocales"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


