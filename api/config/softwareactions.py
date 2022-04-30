from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class SoftwareActions(object):
    """
    Configuration - Software Actions API
    
    Implements GET POST DEL PUT methods for Software Actions endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def findSoftwareImages(self):
        """
        Get software images
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/software"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createImageURL(self, payload):
        """
        Create software image URL
        
        Parameters:
        payload:	Create software image request payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/software"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def getImageProps(self, versionId):
        """
        Get Image Properties
        
        Parameters:
        versionId	 (string):	Version
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/software/imageProperties/{versionId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def findImagesWithFilters(self, imageType, vnfType):
        """
        Get software images
        
        Parameters:
        imageType	 (string):	Image type
		vnfType	 (string):	VNF type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/software/images?imageType={imageType}&vnfType={vnfType}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getPnfProperties(self, pnfType):
        """
        Get PNF Properties
        
        Parameters:
        pnfType	 (string):	PNF type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/software/pnfproperties/{pnfType}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def findVEdgeSoftwareVersion(self):
        """
        Get vEdge software version
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/software/vedge/version"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def findSoftwareVersion(self):
        """
        Get software version
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/software/version"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getVnfProperties(self, versionId):
        """
        Get VNF Properties
        
        Parameters:
        versionId	 (string):	Version
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/software/vnfproperties/{versionId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def findZtpSoftwareVersion(self):
        """
        Get ZTP software version
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/software/ztp/version"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateImageURL(self, payload, versionId):
        """
        Update software image URL
        
        Parameters:
        payload:	Update software image request payload
		versionId	 (string):	Version
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/software/{versionId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, payload)
        return response


    def deleteImageURL(self, versionId):
        """
        Delete software image URL
        
        Parameters:
        versionId	 (string):	Version
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/software/{versionId}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


