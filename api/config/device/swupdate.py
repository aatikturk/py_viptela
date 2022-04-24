from query_builder import Builder
import HttpMethods

class Software(object):
    """
    Configuration - Device Software Update API
    
    Implements GET POST DEL PUT methods for DeviceSoftwareUpdate endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def installPkg(self):
        """
        Install software package
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/software/package"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getUploadImagesCount(self, imageType):
        """
        Number of software image presented in vManage repository
        
        Parameters:
        imageType	 (array):	Image type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/software/package/imageCount?imageType={imageType}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def downloadPackageFile(self, fileName, imageType):
        """
        Download software package file
        
        Parameters:
        fileName	 (string):	Pakcage file name
		imageType	 (string):	Image type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/software/package/{fileName}?imageType={imageType}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def processSoftwareImage(self, imageType):
        """
        Install software image package
        
        Parameters:
        imageType	 (string):	Image type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/software/package/{imageType}"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getImageMetadata(self, versionId):
        """
        Update Package Metadata
        
        Parameters:
        versionId	 (string):	Image ID
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/software/package/{versionId}/metadata"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def editImageMetadata(self, bodyParameter, versionId):
        """
        Update Package Metadata
        
        Parameters:
        bodyParameter:	Description
		versionId	 (string):	Image ID
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/software/package/{versionId}/metadata"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, bodyParameter)
        return response


