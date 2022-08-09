def getVSmartPolicyTemplateList(vmanage):
    """
    Get all template vsmart policy list
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/vsmart"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def createVSmartTemplate(vmanage, templatepolicy):
    """
    Create template for given policy
    
    Parameters:
    templatepolicy:	Template policy
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/vsmart"
    response = vmanage.client.apiCall("POST", endpoint, templatepolicy)
    return response

def activatePolicyForCloudServices(vmanage, templatepolicy, policyId):
    """
    Activate vsmart policy for a given policy id
    
    Parameters:
    templatepolicy:	Template policy
	policyId	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/vsmart/activate/central/{policyId}"
    response = vmanage.client.apiCall("POST", endpoint, templatepolicy)
    return response

def activatePolicy(vmanage, templatepolicy, policyId):
    """
    Activate vsmart policy for a given policy id
    
    Parameters:
    templatepolicy:	Template policy
	policyId	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/vsmart/activate/{policyId}"
    response = vmanage.client.apiCall("POST", endpoint, templatepolicy)
    return response

def editTemplateWithoutLockChecks(vmanage, templatepolicy, policyId):
    """
    Edit template for given policy id to allow for multiple component edits
    
    Parameters:
    templatepolicy:	Template policy
	policyId	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/vsmart/central/{policyId}"
    response = vmanage.client.apiCall("PUT", endpoint, templatepolicy)
    return response

def checkVSmartConnectivityStatus(vmanage):
    """
    Check VSmart Connectivity Status
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/vsmart/connectivity/status"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def deActivatePolicy(vmanage, policyId):
    """
    Deactivate vsmart policy for a given policy id
    
    Parameters:
    policyId	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/vsmart/deactivate/{policyId}"
    response = vmanage.client.apiCall("POST", endpoint)
    return response

def getTemplateByPolicyId(vmanage, policyId):
    """
    Get template policy definition by policy id
    
    Parameters:
    policyId	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/vsmart/definition/{policyId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def QosmosNbarMigrationWarning(vmanage):
    """
    Qosmos Nbar migration
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/vsmart/qosmos_nbar_migration_warning"
    response = vmanage.client.apiCall("GET", endpoint)
    return response

def editVSmartTemplate(vmanage, templatepolicy, policyId):
    """
    Edit template for given policy id
    
    Parameters:
    templatepolicy:	Template policy
	policyId	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/vsmart/{policyId}"
    response = vmanage.client.apiCall("PUT", endpoint, templatepolicy)
    return response

def deleteVSmartTemplate(vmanage, policyId):
    """
    Delete template for a given policy id
    
    Parameters:
    policyId	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/vsmart/{policyId}"
    response = vmanage.client.apiCall("DELETE", endpoint)
    return response
