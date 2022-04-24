from query_builder import Builder
import HttpMethods

class Design(object):
    """
    Configuration - Network Design Templates API
    
    Implements GET POST DEL PUT methods for NetworkDesignTemplates endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getGlobalTemplate(self, templateId):
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


    def editGlobalTemplate(self, globaltemplate, templateId):
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


    def getDeviceProfileFeatureTemplateList(self):
        """
        Generate device profile template list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign/profile/feature"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def generateProfileTemplateList(self):
        """
        Generate profile template list
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign/profile/template"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDeviceProfileTemplate(self, templateId):
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


    def editDeviceProfileTemplate(self, globaltemplate, templateId):
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


