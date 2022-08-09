def activate(vmanage):
    """
    Activate cluster to start working as primary
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/activate"
    response = vmanage.apiCall("POST", endpoint)
    return response

def getClusterInfo(vmanage):
    """
    Get disaster recovery cluster info
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/clusterInfo"
    response = vmanage.apiCall("GET", endpoint)
    return response

def restoreConfigDb(vmanage, payload):
    """
    Signal vManage to initiate configuration-db restore operation
    
    Parameters:
    payload:	Config-db meta payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/dbrestore"
    response = vmanage.apiCall("POST", endpoint, payload)
    return response

def getConfigDBRestoreStatus(vmanage):
    """
    Config-db restore status
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/dbrestorestatus"
    response = vmanage.apiCall("GET", endpoint)
    return response

def deleteLocalDC(vmanage):
    """
    Delete local data center
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/deleteLocalDataCenter"
    response = vmanage.apiCall("POST", endpoint)
    return response

def deleteDC(vmanage):
    """
    Delete data center
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/deleteRemoteDataCenter"
    response = vmanage.apiCall("POST", endpoint)
    return response

def delete(vmanage):
    """
    Delete disaster recovery
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/deregister"
    response = vmanage.apiCall("POST", endpoint)
    return response

def getDetails(vmanage):
    """
    Get disaster recovery details
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/details"
    response = vmanage.apiCall("GET", endpoint)
    return response

def download(vmanage, token):
    """
    Downloading stats file
    
    Parameters:
    token	 (string):	Token
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/download/backup/{token}/db_bkp.tar.gz"
    response = vmanage.apiCall("GET", endpoint)
    return response

def downloadReplicationData(vmanage, token, fileName):
    """
    Download replication data
    
    Parameters:
    token	 (string):	Token
	fileName	 (string):	File name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/download/{token}/{fileName}"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getDRStatus(vmanage):
    """
    Disaster recovery status
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/drstatus"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getHistory(vmanage):
    """
    Get disaster recovery switchover history
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/history"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getLocalHistory(vmanage):
    """
    Get disaster recovery local switchover history
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/localLatestHistory"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getLocalDCState(vmanage):
    """
    Get local data center details
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/localdc"
    response = vmanage.apiCall("GET", endpoint)
    return response

def pauseDR(vmanage):
    """
    Pause DR
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/pause"
    response = vmanage.apiCall("POST", endpoint)
    return response

def pauseLocalArbitrator(vmanage):
    """
    Pause DR for Local Arbitrator
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/pauseLocalArbitrator"
    response = vmanage.apiCall("POST", endpoint)
    return response

def pauseLocalDCForDR(vmanage):
    """
    Pause DR for Local datacenter
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/pauseLocalDC"
    response = vmanage.apiCall("POST", endpoint)
    return response

def pauseLocalDCReplication(vmanage):
    """
    Pause DR replication for Local datacenter
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/pauseLocalReplication"
    response = vmanage.apiCall("POST", endpoint)
    return response

def DRPauseReplication(vmanage):
    """
    Pause DR data replication
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/pausereplication"
    response = vmanage.apiCall("POST", endpoint)
    return response

def update(vmanage, request):
    """
    Update data centers for disaster recovery
    
    Parameters:
    request:	Datacenter registration request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/register"
    response = vmanage.apiCall("PUT", endpoint, request)
    return response

def register(vmanage, request):
    """
    Register data centers for disaster recovery
    
    Parameters:
    request:	Datacenter registration request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/register"
    response = vmanage.apiCall("POST", endpoint, request)
    return response

def getRemoteDCMembersState(vmanage):
    """
    Gets remote data center member state
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/remoteDcState"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getRemoteDataCenterState(vmanage):
    """
    Get remote data center details
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/remotedc"
    response = vmanage.apiCall("GET", endpoint)
    return response

def updateDRState(vmanage, dcReg):
    """
    Update complete disaster recovery information to remote data center
    
    Parameters:
    dcReg:	Datacenter registration
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/remotedc"
    response = vmanage.apiCall("POST", endpoint, dcReg)
    return response

def getRemoteDCVersion(vmanage):
    """
    Get remote data center vManage version
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/remotedc/swversion"
    response = vmanage.apiCall("GET", endpoint)
    return response

def DRReplicationRequest(vmanage, drrequest):
    """
    Replication Request message sent from primary
    
    Parameters:
    drrequest:	DR request
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/requestimport"
    response = vmanage.apiCall("POST", endpoint, drrequest)
    return response

def restartDC(vmanage, dcReg):
    """
    Restart data center
    
    Parameters:
    dcReg:	Datacenter registration
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/restartDataCenter"
    response = vmanage.apiCall("POST", endpoint, dcReg)
    return response

def getDRLocalReplicationSchedule(vmanage):
    """
    Get disaster recovery local replication schedule
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/schedule"
    response = vmanage.apiCall("GET", endpoint)
    return response

def getdrStatus(vmanage):
    """
    Get disaster recovery status
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/status"
    response = vmanage.apiCall("GET", endpoint)
    return response

def unpauseDR(vmanage):
    """
    Unpause DR
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/unpause"
    response = vmanage.apiCall("POST", endpoint)
    return response

def unpauseLocalArbitrator(vmanage):
    """
    Unpause DR for Local Arbitrator
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/unpauseLocalArbitrator"
    response = vmanage.apiCall("POST", endpoint)
    return response

def unpauseLocalDCForDR(vmanage):
    """
    Unpause DR for Local datacenter
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/unpauseLocalDC"
    response = vmanage.apiCall("POST", endpoint)
    return response

def unpauseLocalDCReplication(vmanage):
    """
    Unpause DR replication for local datacenter
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/unpauseLocalReplication"
    response = vmanage.apiCall("POST", endpoint)
    return response

def DRUnPauseReplication(vmanage):
    """
    Un-Pause DR data replication
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/unpausereplication"
    response = vmanage.apiCall("POST", endpoint)
    return response

def updateDrState(vmanage):
    """
    Update arbitrator with primary and secondary states cluster
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/updateDRConfigOnArbitrator"
    response = vmanage.apiCall("POST", endpoint)
    return response

def updateReplication(vmanage, replicationstatus):
    """
    Update DR replication status
    
    Parameters:
    replicationstatus:	Replication status
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/updateReplication"
    response = vmanage.apiCall("POST", endpoint, replicationstatus)
    return response

def getReachabilityInfo(vmanage, nodelist):
    """
    Validate a list of nodes
    
    Parameters:
    nodelist:	Node list
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/disasterrecovery/validateNodes"
    response = vmanage.apiCall("POST", endpoint, nodelist)
    return response
