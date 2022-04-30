from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Ucse(object):
    """
    Real-Time Monitoring - Ucse API
    
    Implements GET POST DEL PUT methods for Ucse endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def createUcseStats(self, remote_tloc_address, remote_tloc_color, local_tloc_color, deviceId):
        """
        Get  UCSE stats entry from device
        
        Parameters:
        remote_tloc_address	 (string):	Remote TLOC address
		remote_tloc_color	 (string):	Remote tloc color
		local_tloc_color	 (string):	Local tloc color
		deviceId	 (string):	Device IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/ucse/stats?remote-tloc-address={remote_tloc_address}&remote-tloc-color={remote_tloc_color}&local-tloc-color={local_tloc_color}&deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


