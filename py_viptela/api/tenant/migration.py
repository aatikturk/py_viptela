def downloadData(vmanage, path):
    """
    Download tenant data
    
    Parameters:
    path	 (string):	File path
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/tenantmigration/download/{path}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
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
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/tenantmigration/export"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, bodyParameter)
    return response
def importData(vmanage):
    """
    Import tenant data
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/tenantmigration/import"
    response = vmanage.client.apiCall(vmanage.POST, endpoint)
    return response
def getToken(vmanage, migrationId):
    """
    Get migration token
    
    Parameters:
    migrationId	 (string):	Migration Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/tenantmigration/migrationToken?migrationId={migrationId}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def reTrigger(vmanage):
    """
    Re-trigger network migration
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/tenantmigration/networkMigration"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def migrate(vmanage, networkMigration):
    """
    Migrate network
    
    Parameters:
    networkMigration:	Network migration
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/tenantmigration/networkMigration"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, networkMigration)
    return response
