from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Group(object):
    """
    Colocation - Service Group API
    
    Implements GET POST DEL PUT methods for ServiceGroup endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getServiceChain(self, serviceGroupName):
        """
        Get service chain by name
        
        Parameters:
        serviceGroupName	 (string):	Service group name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/servicegroup?serviceGroupName={serviceGroupName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def update(self, servicegroup):
        """
        Update service group
        
        Parameters:
        servicegroup:	Service group
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/servicegroup"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, servicegroup)
        return response


    def create(self, servicegroup):
        """
        Add new service group
        
        Parameters:
        servicegroup:	Service group
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/servicegroup"
        response = self.client.apiCall(HttpMethods.POST, endpoint, servicegroup)
        return response


    def getGroupInCluster(self, ClusterId, UserGroupName):
        """
        Get service chains in cluster
        
        Parameters:
        ClusterId	 (string):	Cluster Id
		UserGroupName	 (string):	UserGroup Name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/servicegroup/attached?ClusterId={ClusterId}&UserGroupName={UserGroupName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDefaultChain(self):
        """
        Get default service chains
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/servicegroup/servicechain/default"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getAvailableChains(self):
        """
        Get all service chains
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/servicegroup/servicechains"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def delete(self, name):
        """
        Delete service group
        
        Parameters:
        name	 (string):	Service group name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/servicegroup/{name}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


