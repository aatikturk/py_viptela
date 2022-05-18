from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Colo(object):
    """
    Monitoring - Colocation Cluster API
    
    Implements GET POST DEL PUT methods for ColocationCluster endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def getDetailById(self, clusterId):
        """
        Provide details of ids of existing clusters
        
        Parameters:
        clusterId	 (string):	Cluster Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/monitor/cluster?clusterId={clusterId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getConfigById(self, clusterId):
        """
        Provide details of devices of clusters
        
        Parameters:
        clusterId	 (string):	Cluster Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/monitor/cluster/config?clusterId={clusterId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getPortMappingById(self, clusterId):
        """
        Provide details of port mappings in the cluster
        
        Parameters:
        clusterId	 (string):	Cluster Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/monitor/cluster/portView?clusterId={clusterId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDeviceDetailById(self, deviceId):
        """
        List details for Device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/monitor/device?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getSystemStatusById(self, deviceId):
        """
        List all connected VNF to a device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/monitor/device/system?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getvnfById(self, deviceId):
        """
        List all VNF attached with Device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/monitor/device/vnf?deviceId={deviceId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def listNetworkFunctionMap(self):
        """
        Retrieve network function listing
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/monitor/networkfunction/listmap"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getpnfDetails(self, clusterId):
        """
        List all PNF by cluster Id
        
        Parameters:
        clusterId	 (string):	Cluster Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/monitor/pnf?clusterId={clusterId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getPNFConfig(self, pnfSerialNumber, clusterId):
        """
        List configuration of PNF
        
        Parameters:
        pnfSerialNumber	 (string):	PNF serial number
		clusterId	 (string):	Cluster Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/monitor/pnf/configuration?pnfSerialNumber={pnfSerialNumber}&clusterId={clusterId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getServiceChainDetails(self, clusterId, userGroupName):
        """
        List all service chain or service chains by Id
        
        Parameters:
        clusterId	 (string):	Cluster Id
		userGroupName	 (string):	UserGroup Name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/monitor/servicechain?clusterId={clusterId}&userGroupName={userGroupName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getServiceGroupById(self, clusterId):
        """
        List all attached serviceGroups to cluster
        
        Parameters:
        clusterId	 (string):	Cluster Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/monitor/servicegroup?clusterId={clusterId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getvnfDetails(self, clusterId, userGroupName):
        """
        Provide details of all existing VNF
        
        Parameters:
        clusterId	 (string):	Cluster Id
		userGroupName	 (string):	UserGroup Name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/monitor/vnf?clusterId={clusterId}&userGroupName={userGroupName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def vnfActions(self, vmName, deviceId, action):
        """
        VNF action
        
        Parameters:
        vmName	 (string):	VM Name
		deviceId	 (string):	Device Id
		action	 (string):	Action
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/monitor/vnf/action?vmName={vmName}&deviceId={deviceId}&action={action}"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getVNFEventsCountDetail(self, user_group):
        """
        Get event detail of VNF
        
        Parameters:
        user_group	 (string):	user group name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/monitor/vnf/alarms?user_group={user_group}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getVNFAlarmCount(self, user_group):
        """
        Get event detail of VNF
        
        Parameters:
        user_group	 (string):	user group name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/monitor/vnf/alarms/count?user_group={user_group}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getVNFEventsDetail(self, vnfName):
        """
        Get event detail of VNF
        
        Parameters:
        vnfName	 (string):	VNF name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/monitor/vnf/events?vnfName={vnfName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getVNFInterfaceDetail(self, vnfName, deviceIp, deviceClass):
        """
        Get interface detail of VNF
        
        Parameters:
        vnfName	 (string):	VNF name
		deviceIp	 (string):	Device IP
		deviceClass	 (string):	Device class
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/colocation/monitor/vnf/interface?vnfName={vnfName}&deviceIp={deviceIp}&deviceClass={deviceClass}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


