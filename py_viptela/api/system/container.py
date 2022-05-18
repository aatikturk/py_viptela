from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Container(object):
    """
    System - Container API
    
    Implements GET POST DEL PUT methods for Container endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def activateContainerOnRemoteHost(self, containerName, url, hostIp, checksum):
        """
        Activate container on remote host
        
        Parameters:
        containerName	 (string):	Container name
		url	 (string):	Container image URL
		hostIp	 (string):	Container host IP
		checksum	 (string):	Container image checksum
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/container-manager/activate/{containerName}?url={url}&hostIp={hostIp}&checksum={checksum}"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def deActivateContainer(self, containerName, hostIp):
        """
        Deactivate container on remote host
        
        Parameters:
        containerName	 (string):	Container name
		hostIp	 (string):	Container host IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/container-manager/deactivate/{containerName}?hostIp={hostIp}"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def doesValidImageExist(self, containerName):
        """
        Get container image checksum
        
        Parameters:
        containerName	 (string):	Container name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/container-manager/doesValidImageExist/{containerName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getContainerInspectData(self, containerName, hostIp):
        """
        Get container inspect data
        
        Parameters:
        containerName	 (string):	Container name
		hostIp	 (string):	Container host IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/container-manager/inspect/{containerName}?hostIp={hostIp}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getContainerSettings(self, containerName, hostIp):
        """
        Get container settings
        
        Parameters:
        containerName	 (string):	Container name
		hostIp	 (string):	Container host IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/container-manager/settings/{containerName}?hostIp={hostIp}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getChecksum(self):
        """
        Get container image checksum
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sdavc/checksum"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCustomApp(self):
        """
        Displays the user-defined applications
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sdavc/customapps"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def activateContainer(self, containertaskconfig, taskId):
        """
        Activate container
        
        Parameters:
        containertaskconfig:	Container task config
		taskId	 (string):	Task Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sdavc/task/{taskId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, containertaskconfig)
        return response


    def testLoadBalancer(self):
        """
        Test SD_AVC load balancer
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/sdavc/test"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


