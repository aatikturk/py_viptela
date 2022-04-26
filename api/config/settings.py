from query_builder import Builder
import HttpMethods

class Settings(object):
    """
    Configuration - Settings API
    
    Implements GET POST DEL PUT methods for Settings endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getBanner(self):
        """
        Retrieve banner
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/settings/banner"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSessionTimout(self):
        """
        Get client session timeout
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/settings/clientSessionTimeout"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createAnalyticsDataFile(self):
        """
        Create analytics data file
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/settings/configuration/analytics/dca"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getCertConfiguration(self, settingType):
        """
        Retrieve certificate configuration value by settingType
        
        Parameters:
        settingType	 (string):	Setting type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/settings/configuration/certificate/{settingType}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def editCertConfiguration(self, certConfig, settingType):
        """
        Update certificate configuration
        
        Parameters:
        certConfig:	Certificate config
		settingType	 (string):	Setting type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/settings/configuration/certificate/{settingType}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, certConfig)
        return response


    def newCertConfiguration(self, certConfig, settingType):
        """
        Add new certificate configuration
        
        Parameters:
        certConfig:	Certificate config
		settingType	 (string):	Setting type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/settings/configuration/certificate/{settingType}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, certConfig)
        return response


    def getGoogleMapKey(self):
        """
        Retrieve Google map key
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/settings/configuration/googleMapKey"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getMaintenanceWindow(self):
        """
        Retrieve maintenance window
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/settings/configuration/maintenanceWindow"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getConfigurationBySettingType(self, settingType):
        """
        Retrieve configuration value by settingType
        
        Parameters:
        settingType	 (string):	Setting type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/settings/configuration/{settingType}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def editConfiguration(self, configSetting, settingType):
        """
        Update configuration setting
        
        Parameters:
        configSetting:	Configuration setting
		settingType	 (string):	Setting type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/settings/configuration/{settingType}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, configSetting)
        return response


    def newConfiguration(self, configSetting, settingType):
        """
        Add new configuration
        
        Parameters:
        configSetting:	Configuration setting
		settingType	 (string):	Setting type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/settings/configuration/{settingType}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, configSetting)
        return response


