from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Messaging(object):
    """
    Device - Messaging API
    
    Implements GET POST DEL PUT methods for Messaging endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getVmanageConnList(self):
        """
        Create device vManage connection list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/messaging/device/vmanage"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


