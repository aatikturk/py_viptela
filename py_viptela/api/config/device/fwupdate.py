from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Firmware(object):
    """
    Configuration - Device Firmware Update API
    
    Implements GET POST DEL PUT methods for DeviceFirmwareUpdate endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def get(self):
        """
        Get list of firmware images in the repository
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/firmware"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def process(self):
        """
        Upload firmware image package
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/firmware"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def activate(self, fwInfo):
        """
        Activate firmware on device
        
        Parameters:
        fwInfo:    Firmware Info
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/firmware/activate"
        response = self.client.apiCall(HttpMethods.POST, endpoint, fwInfo)
        return response


    def getDevicesFWUpgrade(self):
        """
        Get list of devices that support firmware upgrade
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/firmware/devices"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def install(self, fwInfo):
        """
        Install firmware on device
        
        Parameters:
        fwInfo:    Firmware Info
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/firmware/install"
        response = self.client.apiCall(HttpMethods.POST, endpoint, fwInfo)
        return response


    def remove(self, fwInfo):
        """
        Remove firmware on device
        
        Parameters:
        fwInfo:    Firmware Info
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/firmware/remove"
        response = self.client.apiCall(HttpMethods.POST, endpoint, fwInfo)
        return response


    def getDetails(self, versionId):
        """
        Get firmware image details for a given version
        
        Parameters:
        versionId	 (string):	Firmware image version
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/firmware/{versionId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def delete(self, versionId):
        """
        Delete firmware image package
        
        Parameters:
        versionId	 (string):	Firmware image version
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/firmware/{versionId}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


