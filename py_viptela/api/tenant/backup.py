def deleteBkp(vmanage, fileName):
    """
    Delete all or a specific backup file stored in vManage
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    fileName	 (string):	File name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/tenantbackup/delete?fileName={fileName}"
    response = vmanage.client.apiCall(vmanage.DELETE, endpoint)
    return response
def downloadBkpFile(vmanage, path):
    """
    Download a Backup File that is already stored in vManage
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
    path	 (string):	File path
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/tenantbackup/download/{path}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def exportBkp(vmanage):
    """
    Trigger a backup of configuration database and store it in vManage
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/tenantbackup/export"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
def importBkp(vmanage):
    """
    Submit a previously backed up file and import the data and apply it to the configuraion database
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/tenantbackup/import"
    response = vmanage.client.apiCall(vmanage.POST, endpoint)
    return response
def listBkp(vmanage):
    """
    List all backup files of a tenant stored in vManage
    NOTE: In a multitenant vManage system, this API is only available in the Provider view.
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/tenantbackup/list"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
