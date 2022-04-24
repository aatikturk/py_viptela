from query_builder import Builder
import HttpMethods

class Firmware(object):
    """
    Configuration - Device Firmware Update API
    
    Implements GET POST DEL PUT methods for DeviceFirmwareUpdate endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getFirmwareImages(self):
        """
        Get list of firmware images in the repository
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/firmware"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def processFirmwareImage(self):
        """
        Upload firmware image package
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/firmware"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def activateFirmwareImage(self, bodyParameter):
        """
        Activate firmware on device
        
        Parameters:
        bodyParameter:	Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/firmware/activate"
        response = self.client.apiCall(HttpMethods.POST, endpoint, bodyParameter)
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


    def installFirmwareImage(self, bodyParameter):
        """
        Install firmware on device
        
        Parameters:
        bodyParameter:	Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/firmware/install"
        response = self.client.apiCall(HttpMethods.POST, endpoint, bodyParameter)
        return response


    def removeFirmwareImage(self, bodyParameter):
        """
        Remove firmware on device
        
        Parameters:
        bodyParameter:	Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/firmware/remove"
        response = self.client.apiCall(HttpMethods.POST, endpoint, bodyParameter)
        return response


    def getFirmwareImageDetails(self, versionId):
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


    def deleteFirmwareImage(self, versionId):
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


