from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class NetworkDesign(object):
    """
    Configuration - Network Design API
    
    Implements GET POST DEL PUT methods for Network Design endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getNetworkDesign(self):
        """
        Get existing network design
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def editNetworkDesign(self, payload, id):
        """
        Edit network segment
        
        Parameters:
        payload:	Network design payload
		id	 (string):	Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign?id={id}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, payload)
        return response


    def createNetworkDesign(self, payload):
        """
        Create network design
        
        Parameters:
        payload:	Network design payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def pushNetworkDesign(self, devicetemplate):
        """
        Attach network design
        
        Parameters:
        devicetemplate:	Device template
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign/attachment"
        response = self.client.apiCall(HttpMethods.POST, endpoint, devicetemplate)
        return response


    def getGlobalParams(self):
        """
        Get global parameter templates
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign/global/parameters"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def acquireEditLock(self):
        """
        Acquire edit lock
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign/lock/edit"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def runMyTest(self, name):
        """
        Get all device templates for this feature template
        
        Parameters:
        name	 (string):	Test bane
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign/mytest/{name}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def pushDeviceProfileTemplate(self, devicetemplate, profileId):
        """
        Attach to device profile
        
        Parameters:
        devicetemplate:	Device template
		profileId	 (string):	Device profile Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign/profile/attachment/{profileId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, devicetemplate)
        return response


    def acquireAttachLock(self, profileId):
        """
        Get the service profile config for a given device profile id
        
        Parameters:
        profileId	 (string):	Device profile Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign/profile/lock/{profileId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getConfigStatus(self):
        """
        Get device profile configuration status
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign/profile/status"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getConfigStatusById(self, profileId):
        """
        Get device profile configuration status by profile Id
        
        Parameters:
        profileId	 (string):	Device profile Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign/profile/status/{profileId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTaskCount(self):
        """
        Get device profile configuration task count
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign/profile/task/count"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTaskStatus(self):
        """
        Get device profile configuration task status
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign/profile/task/status"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getTaskStatusById(self, profileId):
        """
        Get device profile configuration status by profile Id
        
        Parameters:
        profileId	 (string):	Device profile Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign/profile/task/status/{profileId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getServiceProfileConfig(self, profileId, deviceModel):
        """
        Get the service profile config for a given device profile id
        
        Parameters:
        profileId	 (string):	Device profile Id
		deviceModel	 (string):	Device model
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/networkdesign/serviceProfileConfig/{profileId}?deviceModel={deviceModel}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


