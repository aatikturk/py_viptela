from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Network(object):
    """
    Device - Network API
    
    Implements GET POST DEL PUT methods for Network endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getVmanageControlStatus(self, isCached, vpnId):
        """
        Retrieve vManage control status
        
        Parameters:
        isCached	 (boolean):	Is cached flag
		vpnId	 (array):	VPN Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/network/connectionssummary?isCached={isCached}&vpnId={vpnId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getRebootCount(self, isCached):
        """
        Retrieve reboot count
        
        Parameters:
        isCached	 (boolean):	Is cached flag
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/network/issues/rebootcount?isCached={isCached}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getNetworkIssuesSummary(self):
        """
        Retrieve network issues summary
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/network/issues/summary"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getNetworkStatusSummary(self):
        """
        Retrieve network status summary
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/network/status"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


