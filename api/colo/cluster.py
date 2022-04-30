from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Cluster(object):
    """
    Colocation - Cluster API
    
    Implements GET POST DEL PUT methods for Cluster endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getDetail(self, clusterName):
        """
        Get details of all existing Clusters
        
        Parameters:
        clusterName	 (string):	Cluster name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/cluster?clusterName={clusterName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def update(self, clusterconfig):
        """
        Update a existing cluster
        
        Parameters:
        clusterconfig:	Cluster config
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/cluster"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, clusterconfig)
        return response


    def create(self, clusterconfig):
        """
        Add a new cluster
        
        Parameters:
        clusterconfig:	Cluster config
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/cluster"
        response = self.client.apiCall(HttpMethods.POST, endpoint, clusterconfig)
        return response


    def acitvate(self, clusterName):
        """
        Activate a cluster
        
        Parameters:
        clusterName	 (string):	Cluster name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/cluster/activate?clusterName={clusterName}"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def dummyccm(self, clusterName):
        """
        Activate dummp cluster
        
        Parameters:
        clusterName	 (string):	Cluster name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/cluster/activateClusterDummy?clusterName={clusterName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def dummycspState(self, clusterName, state):
        """
        Activate cluster in a state
        
        Parameters:
        clusterName	 (string):	Cluster name
		state	 (string):	Cluster state
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/cluster/activateClusterDummyState?clusterName={clusterName}&state={state}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateCspToCluster(self, cspconfig):
        """
        Update attached csp to cluster
        
        Parameters:
        cspconfig:	CSP config
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/cluster/attached/csp"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, cspconfig)
        return response


    def preview(self, serialNumber):
        """
        Clouddock cluster preview
        
        Parameters:
        serialNumber	 (string):	Serial number
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/cluster/config?serialNumber={serialNumber}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def deAcitvate(self, clusterId):
        """
        Deactivate clouddock cluster
        
        Parameters:
        clusterId	 (string):	Cluster Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/cluster/deactivate?clusterId={clusterId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getDetailById(self, clusterId):
        """
        Get cluster by Id
        
        Parameters:
        clusterId	 (string):	Cluster Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/cluster/id?clusterId={clusterId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def rmaCloudDockCsp(self, bodyParameter, clusterName):
        """
        RMA operation for CSP device
        
        Parameters:
        bodyParameter:	Description
		clusterName	 (string):	Cluster name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/cluster/rma?clusterName={clusterName}"
        response = self.client.apiCall(HttpMethods.POST, endpoint, bodyParameter)
        return response


    def deleteByName(self, clustername):
        """
        Delete cluster by name
        
        Parameters:
        clustername	 (string):	Cluster name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/cluster/{clustername}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


