from query_builder import Builder
import HttpMethods

class Cluster(object):
    """
    Cluster Management API
    
    Implements GET POST DEL PUT methods for ClusterManagement endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def checkIfClusterLocked(self):
        """
        Check whether cluster is locked
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/clusterManagement/clusterLocked"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getClusterWorkflowVersion(self):
        """
        List vManages in the cluster
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/clusterManagement/clusterworkflow/version"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def configureVmanage(self, vmanageserverconfig):
        """
        Configure vManage
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        vmanageserverconfig:	vManage server config
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/clusterManagement/configure"
        response = self.client.apiCall(HttpMethods.POST, endpoint, vmanageserverconfig)
        return response


    def getConnectedDevices(self, vmanageIP):
        """
        Get connected device for vManage
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        vmanageIP	 (string):	vManage IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/clusterManagement/connectedDevices/{vmanageIP}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def healthDetails(self):
        """
        Get cluster health check details
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/clusterManagement/health/details"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def healthStatusInfo(self):
        """
        Get cluster health check details
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/clusterManagement/health/status"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def healthSummary(self, isCached):
        """
        Get cluster health check summary
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        isCached	 (boolean):	Flag to enable cached result
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/clusterManagement/health/summary?isCached={isCached}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getConfiguredIPList(self, vmanageID):
        """
        Get configured IP addresses
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        vmanageID	 (string):	vManage Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/clusterManagement/iplist/{vmanageID}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def isClusterReady(self):
        """
        Is cluster ready
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/clusterManagement/isready"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def listVmanages(self):
        """
        List vManages in the cluster
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/clusterManagement/list"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def nodeProperties(self):
        """
        Get properties of vManage being added to  cluster
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/clusterManagement/nodeProperties"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def removeVmanage(self, vmanageserverinfo):
        """
        Remove vManage from cluster
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        vmanageserverinfo:	vManage server info
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/clusterManagement/remove"
        response = self.client.apiCall(HttpMethods.POST, endpoint, vmanageserverinfo)
        return response


    def performReplicationAndRebalanceOfKafkaPartitions(self):
        """
        Initiate replication and rebalance of kafka topics
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/clusterManagement/replicateAndRebalance"
        response = self.client.apiCall(HttpMethods.PUT, endpoint)
        return response


    def editVmanage(self, vmanageclusterconfig):
        """
        Update vManage cluster info
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        vmanageclusterconfig:	vManage cluster config
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/clusterManagement/setup"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, vmanageclusterconfig)
        return response


    def addVmanage(self, vmanageclusterconfig):
        """
        Add vManage to cluster
        
        Parameters:
        vmanageclusterconfig:	vManage cluster config
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/clusterManagement/setup"
        response = self.client.apiCall(HttpMethods.POST, endpoint, vmanageclusterconfig)
        return response


    def getTenancyMode(self):
        """
        Get vManage tenancy mode
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/clusterManagement/tenancy/mode"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def setTenancyMode(self, tenancymodesetting):
        """
        Update vManage tenancy mode
        
        Parameters:
        tenancymodesetting:	Tenancy mode setting
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/clusterManagement/tenancy/mode"
        response = self.client.apiCall(HttpMethods.POST, endpoint, tenancymodesetting)
        return response


    def getTenantsList(self):
        """
        Get tenant list
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/clusterManagement/tenantList"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def addOrUpdateUserCredentials(self, usercredential):
        """
        Add or update user credentials for cluster operations
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        usercredential:	User credential
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/clusterManagement/userCreds"
        response = self.client.apiCall(HttpMethods.POST, endpoint, usercredential)
        return response


    def getVManageDetails(self, vmanageIP):
        """
        Get vManage detail
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        vmanageIP	 (string):	vManage IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/clusterManagement/vManage/details/{vmanageIP}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getConnectedDevicesPerTenant(self, tenantId, vmanageIP):
        """
        Get connected device for vManage for a tenant
        NOTE: In a multitenant vManage system, this API is only available in the Provider view.
        
        Parameters:
        tenantId	 (string):	Tenant Id
		vmanageIP	 (string):	vManage IP
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/clusterManagement/{tenantId}/connectedDevices/{vmanageIP}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


