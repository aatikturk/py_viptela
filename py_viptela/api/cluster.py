def checkIfClusterLocked(vmanage):
    """
    Check whether cluster is locked
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/clusterManagement/clusterLocked"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getClusterWorkflowVersion(vmanage):
    """
    List vManages in the cluster
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/clusterManagement/clusterworkflow/version"
    response = vmanage.apiCall("GET", endpoint)
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
    
    endpoint = f"dataservice/clusterManagement/configure"
    response = vmanage.apiCall("POST", endpoint, vmanageConfig)
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
    
    endpoint = f"dataservice/clusterManagement/connectedDevices/{vmanageIP}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def healthDetails(vmanage):
    """
    Get cluster health check details
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/clusterManagement/health/details"
    response = vmanage.apiCall("GET", endpoint)
    return response
def healthStatusInfo(vmanage):
    """
    Get cluster health check details
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/clusterManagement/health/status"
    response = vmanage.apiCall("GET", endpoint)
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
    
    endpoint = f"dataservice/clusterManagement/health/summary?isCached={isCached}"
    response = vmanage.apiCall("GET", endpoint)
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
    
    endpoint = f"dataservice/clusterManagement/iplist/{vmanageID}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def isClusterReady(vmanage):
    """
    Is cluster ready
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/clusterManagement/isready"
    response = vmanage.apiCall("GET", endpoint)
    return response
def listVmanages(vmanage):
    """
    List vManages in the cluster
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/clusterManagement/list"
    response = vmanage.apiCall("GET", endpoint)
    return response
def nodeProperties(vmanage):
    """
    Get properties of vManage being added to  cluster
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/clusterManagement/nodeProperties"
    response = vmanage.apiCall("GET", endpoint)
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
    
    endpoint = f"dataservice/clusterManagement/remove"
    response = vmanage.apiCall("POST", endpoint, vmanageInfo)
    return response
def performReplicationAndRebalanceOfKafkaPartitions(vmanage):
    """
    Initiate replication and rebalance of kafka topics
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/clusterManagement/replicateAndRebalance"
    response = vmanage.apiCall("PUT", endpoint)
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
    
    endpoint = f"dataservice/clusterManagement/setup"
    response = vmanage.apiCall("PUT", endpoint, clusterConfig)
    return response
def addVmanage(vmanage, clusterConfig):
    """
    Add vManage to cluster
    
    Parameters:
    clusterConfig:	vManage cluster config
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/clusterManagement/setup"
    response = vmanage.apiCall("POST", endpoint, clusterConfig)
    return response
def getTenancyMode(vmanage):
    """
    Get vManage tenancy mode
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/clusterManagement/tenancy/mode"
    response = vmanage.apiCall("GET", endpoint)
    return response
def setTenancyMode(vmanage, tenancySetting):
    """
    Update vManage tenancy mode
    
    Parameters:
    tenancySetting:	Tenancy mode setting
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/clusterManagement/tenancy/mode"
    response = vmanage.apiCall("POST", endpoint, tenancySetting)
    return response
def getTenantsList(vmanage):
    """
    Get tenant list
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/clusterManagement/tenantList"
    response = vmanage.apiCall("GET", endpoint)
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
    
    endpoint = f"dataservice/clusterManagement/userCreds"
    response = vmanage.apiCall("POST", endpoint, creds)
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
    
    endpoint = f"dataservice/clusterManagement/vManage/details/{vmanageIP}"
    response = vmanage.apiCall("GET", endpoint)
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
    
    endpoint = f"dataservice/clusterManagement/{tenantId}/connectedDevices/{vmanageIP}"
    response = vmanage.apiCall("GET", endpoint)
    return response
