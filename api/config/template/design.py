from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Design(object):
    """
    Configuration - Network Design Templates API
    
    Implements GET POST DEL PUT methods for NetworkDesignTemplates endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getGlobal(self, templateId):
        """
        Get global template
        
        Parameters:
        templateId	 (string):	Template Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign/global/template/{templateId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def editGlobal(self, globaltemplate, templateId):
        """
        Edit global template
        
        Parameters:
        globaltemplate:	Global template
		templateId	 (string):	Template Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign/global/template/{templateId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, globaltemplate)
        return response


    def getFeatureTempList(self):
        """
        Generate device profile template list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign/profile/feature"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getProfileList(self):
        """
        Generate profile template list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign/profile/template"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDeviceProfile(self, templateId):
        """
        Get device profile template
        
        Parameters:
        templateId	 (string):	Template Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign/profile/template/{templateId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def editDeviceProfile(self, globaltemplate, templateId):
        """
        Edit device profile template
        
        Parameters:
        globaltemplate:	Global template
		templateId	 (string):	Template Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign/profile/template/{templateId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, globaltemplate)
        return response


