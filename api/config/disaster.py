from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Disaster(object):
    """
    Configuration - Disaster Recovery API
    
    Implements GET POST DEL PUT methods for Disaster Recovery endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def activate(self):
        """
        Activate cluster to start working as primary
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/activate"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getClusterInfo(self):
        """
        Get disaster recovery cluster info
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/clusterInfo"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def restoreConfigDb(self, payload):
        """
        Signal vManage to initiate configuration-db restore operation
        
        Parameters:
        payload:	Config-db meta payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/dbrestore"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def getConfigDBRestoreStatus(self):
        """
        Config-db restore status
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/dbrestorestatus"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def deleteLocalDC(self):
        """
        Delete local data center
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/deleteLocalDataCenter"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def deleteDC(self):
        """
        Delete data center
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/deleteRemoteDataCenter"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def delete(self):
        """
        Delete disaster recovery
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/deregister"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def getDetails(self):
        """
        Get disaster recovery details
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/details"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def download(self, token):
        """
        Downloading stats file
        
        Parameters:
        token	 (string):	Token
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/download/backup/{token}/db_bkp.tar.gz"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def downloadReplicationData(self, token, fileName):
        """
        Download replication data
        
        Parameters:
        token	 (string):	Token
		fileName	 (string):	File name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/download/{token}/{fileName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getDRStatus(self):
        """
        Disaster recovery status
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/drstatus"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getHistory(self):
        """
        Get disaster recovery switchover history
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/history"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getLocalHistory(self):
        """
        Get disaster recovery local switchover history
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/localLatestHistory"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getLocalDCState(self):
        """
        Get local data center details
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/localdc"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def pauseDR(self):
        """
        Pause DR
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/pause"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def pauseLocalArbitrator(self):
        """
        Pause DR for Local Arbitrator
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/pauseLocalArbitrator"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def pauseLocalDCForDR(self):
        """
        Pause DR for Local datacenter
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/pauseLocalDC"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def pauseLocalDCReplication(self):
        """
        Pause DR replication for Local datacenter
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/pauseLocalReplication"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def DRPauseReplication(self):
        """
        Pause DR data replication
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/pausereplication"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def update(self, request):
        """
        Update data centers for disaster recovery
        
        Parameters:
        request:	Datacenter registration request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/register"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, request)
        return response


    def register(self, request):
        """
        Register data centers for disaster recovery
        
        Parameters:
        request:	Datacenter registration request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/register"
        response = self.client.apiCall(HttpMethods.POST, endpoint, request)
        return response


    def getRemoteDCMembersState(self):
        """
        Gets remote data center member state
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/remoteDcState"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getRemoteDataCenterState(self):
        """
        Get remote data center details
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/remotedc"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateDRState(self, dcReg):
        """
        Update complete disaster recovery information to remote data center
        
        Parameters:
        dcReg:	Datacenter registration
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/remotedc"
        response = self.client.apiCall(HttpMethods.POST, endpoint, dcReg)
        return response


    def getRemoteDCVersion(self):
        """
        Get remote data center vManage version
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/remotedc/swversion"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def DRReplicationRequest(self, drrequest):
        """
        Replication Request message sent from primary
        
        Parameters:
        drrequest:	DR request
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/requestimport"
        response = self.client.apiCall(HttpMethods.POST, endpoint, drrequest)
        return response


    def restartDC(self, dcReg):
        """
        Restart data center
        
        Parameters:
        dcReg:	Datacenter registration
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/restartDataCenter"
        response = self.client.apiCall(HttpMethods.POST, endpoint, dcReg)
        return response


    def getDRLocalReplicationSchedule(self):
        """
        Get disaster recovery local replication schedule
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/schedule"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getdrStatus(self):
        """
        Get disaster recovery status
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/status"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def unpauseDR(self):
        """
        Unpause DR
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/unpause"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def unpauseLocalArbitrator(self):
        """
        Unpause DR for Local Arbitrator
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/unpauseLocalArbitrator"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def unpauseLocalDCForDR(self):
        """
        Unpause DR for Local datacenter
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/unpauseLocalDC"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def unpauseLocalDCReplication(self):
        """
        Unpause DR replication for local datacenter
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/unpauseLocalReplication"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def DRUnPauseReplication(self):
        """
        Un-Pause DR data replication
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/unpausereplication"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def updateDrState(self):
        """
        Update arbitrator with primary and secondary states cluster
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/updateDRConfigOnArbitrator"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def updateReplication(self, replicationstatus):
        """
        Update DR replication status
        
        Parameters:
        replicationstatus:	Replication status
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/updateReplication"
        response = self.client.apiCall(HttpMethods.POST, endpoint, replicationstatus)
        return response


    def getReachabilityInfo(self, nodelist):
        """
        Validate a list of nodes
        
        Parameters:
        nodelist:	Node list
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/disasterrecovery/validateNodes"
        response = self.client.apiCall(HttpMethods.POST, endpoint, nodelist)
        return response


