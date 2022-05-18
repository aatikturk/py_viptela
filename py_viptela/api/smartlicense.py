from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class License(object):
    """
    Smart License API
    
    Implements GET POST DEL PUT methods for SmartLicense endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def sleauthenticate(self, partner):
        """
        authenticate user for sle
        
        Parameters:
        partner:	Partner
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/smartLicensing/authenticate"
        response = self.client.apiCall(HttpMethods.POST, endpoint, partner)
        return response


    def fetchAccounts(self, partner, mode):
        """
        fetch sava for sle
        
        Parameters:
        partner:	Partner
		mode	 (string):	mode
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/smartLicensing/fetchAccounts?mode={mode}"
        response = self.client.apiCall(HttpMethods.GET, endpoint, partner)
        return response


    def fetchReports(self, partner):
        """
        fetch reports offline for sle
        
        Parameters:
        partner:	Partner
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/smartLicensing/fetchAllSa"
        response = self.client.apiCall(HttpMethods.GET, endpoint, partner)
        return response


    def fetchReports(self, partner, saDomain, saId):
        """
        fetch reports offline for sle
        
        Parameters:
        partner:	Partner
		saDomain	 (string):	saDomain
		saId	 (string):	saId
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/smartLicensing/fetchReportsForSa?saDomain={saDomain}&saId={saId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint, partner)
        return response


    def getUserSettings(self):
        """
        get settings
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/smartLicensing/getUserSettings"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def syncLicenses(self, partner):
        """
        get all licenses for sa/va
        
        Parameters:
        partner:	Partner
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/smartLicensing/removeSaVaSelection"
        response = self.client.apiCall(HttpMethods.POST, endpoint, partner)
        return response


    def syncLicenses(self, partner):
        """
        get all licenses for sa/va
        
        Parameters:
        partner:	Partner
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/smartLicensing/syncLicenses"
        response = self.client.apiCall(HttpMethods.POST, endpoint, partner)
        return response


    def uploadAck(self, partner):
        """
        upload ack file  for sa/va
        
        Parameters:
        partner:	Partner
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/smartLicensing/uploadAck"
        response = self.client.apiCall(HttpMethods.POST, endpoint, partner)
        return response


