def checkIfClusterLocked(vmanage):
    """
    Check whether cluster is locked
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/clusterManagement/clusterLocked"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getClusterWorkflowVersion(vmanage):
    """
    List vManages in the cluster
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/clusterManagement/clusterworkflow/version"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def configureVmanage(vmanage, vmanageConfig):
    """
    Configure vManage
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    vmanageConfig:	vManage server config
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/clusterManagement/configure"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, vmanageConfig)
    return response
def getConnectedDevices(vmanage, vmanageIP):
    """
    Get connected device for vManage
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    vmanageIP	 (string):	vManage IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/clusterManagement/connectedDevices/{vmanageIP}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def healthDetails(vmanage):
    """
    Get cluster health check details
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/clusterManagement/health/details"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def healthStatusInfo(vmanage):
    """
    Get cluster health check details
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/clusterManagement/health/status"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def healthSummary(vmanage, isCached):
    """
    Get cluster health check summary
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    isCached	 (boolean):	Flag to enable cached result
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/clusterManagement/health/summary?isCached={isCached}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getConfiguredIPList(vmanage, vmanageID):
    """
    Get configured IP addresses
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    vmanageID	 (string):	vManage Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/clusterManagement/iplist/{vmanageID}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def isClusterReady(vmanage):
    """
    Is cluster ready
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/clusterManagement/isready"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def listVmanages(vmanage):
    """
    List vManages in the cluster
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/clusterManagement/list"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def nodeProperties(vmanage):
    """
    Get properties of vManage being added to  cluster
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/clusterManagement/nodeProperties"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def removeVmanage(vmanage, vmanageInfo):
    """
    Remove vManage from cluster
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    vmanageInfo:	vManage server info
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/clusterManagement/remove"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, vmanageInfo)
    return response
def performReplicationAndRebalanceOfKafkaPartitions(vmanage):
    """
    Initiate replication and rebalance of kafka topics
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/clusterManagement/replicateAndRebalance"
    response = vmanage.client.apiCall(vmanage.PUT, endpoint)
    return response
def editVmanage(vmanage, clusterConfig):
    """
    Update vManage cluster info
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    clusterConfig:	vManage cluster config
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/clusterManagement/setup"
    response = vmanage.client.apiCall(vmanage.PUT, endpoint, clusterConfig)
    return response
def addVmanage(vmanage, clusterConfig):
    """
    Add vManage to cluster
    
    Parameters:
    clusterConfig:	vManage cluster config
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/clusterManagement/setup"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, clusterConfig)
    return response
def getTenancyMode(vmanage):
    """
    Get vManage tenancy mode
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/clusterManagement/tenancy/mode"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def setTenancyMode(vmanage, tenancySetting):
    """
    Update vManage tenancy mode
    
    Parameters:
    tenancySetting:	Tenancy mode setting
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/clusterManagement/tenancy/mode"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, tenancySetting)
    return response
def getTenantsList(vmanage):
    """
    Get tenant list
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/clusterManagement/tenantList"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def addOrUpdateUserCredentials(vmanage, creds):
    """
    Add or update user credentials for cluster operations
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    creds:	User credential
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/clusterManagement/userCreds"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, creds)
    return response
def getVManageDetails(vmanage, vmanageIP):
    """
    Get vManage detail
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    vmanageIP	 (string):	vManage IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/clusterManagement/vManage/details/{vmanageIP}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def getConnectedDevicesPerTenant(vmanage, tenantId, vmanageIP):
    """
    Get connected device for vManage for a tenant
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    tenantId	 (string):	Tenant Id
	vmanageIP	 (string):	vManage IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/clusterManagement/{tenantId}/connectedDevices/{vmanageIP}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
