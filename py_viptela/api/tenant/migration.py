def downloadData(vmanage, path):
    """
    Download tenant data
    
    Parameters:
    path	 (string):	File path
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/tenantmigration/download/{path}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def exportData(vmanage, bodyParameter):
    """
    Export tenant data
    
    Parameters:
    bodyParameter:	Description
    
    bodyParameter  example
    param = {
        "desc": "string",
        "getvBondAddress": "string",
        "idpMetadata": "string",
        "mode": "string",
        "name": "string",
        "oldIdpMetadata": "string",
        "orgName": "string",
        "spMetadata": "string",
        "subDomain": "string",
        "wanEdgeForecast": "string"
    }
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/tenantmigration/export"
    response = vmanage.apiCall("POST", endpoint, bodyParameter)
    return response
def importData(vmanage):
    """
    Import tenant data
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/tenantmigration/import"
    response = vmanage.apiCall("POST", endpoint)
    return response
def getToken(vmanage, migrationId):
    """
    Get migration token
    
    Parameters:
    migrationId	 (string):	Migration Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/tenantmigration/migrationToken?migrationId={migrationId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def reTrigger(vmanage):
    """
    Re-trigger network migration
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/tenantmigration/networkMigration"
    response = vmanage.apiCall("GET", endpoint)
    return response
def migrate(vmanage, networkMigration):
    """
    Migrate network
    
    Parameters:
    networkMigration:	Network migration
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/tenantmigration/networkMigration"
    response = vmanage.apiCall("POST", endpoint, networkMigration)
    return response
