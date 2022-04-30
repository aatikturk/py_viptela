from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Package(object):
    """
    Configuration - Device Software Package API
    
    Implements GET POST DEL PUT methods for DeviceSoftwarePackage endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getFileContents(self, uuid):
        """
        Get bootstrap file contents
        
        Parameters:
        uuid	 (string):	File uuid
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/software/package/custom/file/{uuid}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def editConfigFile(self, bootstrapfile, uuid):
        """
        Edit bootstrap file
        
        Parameters:
        bootstrapfile:	Bootstrap file
		uuid	 (string):	File uuid
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/software/package/custom/file/{uuid}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, bootstrapfile)
        return response


    def uploadImageFile(self, type):
        """
        Upload virtual image/bootstrap file
        
        Parameters:
        type	 (string):	Upload file type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/software/package/custom/uploads/{type}"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def createVnfPackage(self, custompackage):
        """
        Create VNF custom package
        
        Parameters:
        custompackage:	Custom package
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/software/package/custom/vnfPackage"
        response = self.client.apiCall(HttpMethods.POST, endpoint, custompackage)
        return response


