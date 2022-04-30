from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Deployer(object):
    """
    Deployment Mode API
    
    Implements GET POST DEL PUT methods for DeploymentMode endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def requestDNSSecActions(self, action):
        """
        Request DNS-Sec actions
        
        Parameters:
        action	 (string):	DNS-Sec action
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/fedramp/dnssec/actions?action={action}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def configureDNSSec(self, request):
        """
        Configure DNS-Sec
        
        Parameters:
        request:	DNS sec config request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/fedramp/dnssec/config"
        response = self.client.apiCall(HttpMethods.POST, endpoint, request)
        return response


    def getDNSSecStatus(self):
        """
        Get DNS-Sec status
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/fedramp/dnssec/status"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def configFedrampMode(self, mode):
        """
        Set network deployment mode
        
        Parameters:
        mode:	Network deployment mode
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/fedramp/status"
        response = self.client.apiCall(HttpMethods.POST, endpoint, mode)
        return response


    def requestWazuhActions(self, action):
        """
        Wazuh agent action
        
        Parameters:
        action	 (string):	Wazhuh Action
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/fedramp/wazuh/actions?action={action}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def configureWazuhClient(self, wazhuhConfig):
        """
        Configure Wazuh agent
        
        Parameters:
        wazhuhConfig:	Wazhuh configuration
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/fedramp/wazuh/config"
        response = self.client.apiCall(HttpMethods.POST, endpoint, wazhuhConfig)
        return response


    def getWazuhAgentStatus(self):
        """
        Get Wazuh agent status
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/fedramp/wazuh/status"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


