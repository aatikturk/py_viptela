def deleteSchduledBackup(vmanage, taskId, backupInfoId):
    """
    Delete all or a specific backup file stored in vManage
    
    Parameters:
    taskId	 (string):	task id
	backupInfoId	 (string):	Local Backup Info Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/backup/backupinfo?taskId={taskId}&backupInfoId={backupInfoId}"
    response = vmanage.client.apiCall("DELETE", endpoint)
    return response
def getLocalBackupInfo(vmanage, localBackupInfoId):
    """
    Get a localBackupInfo record by localBackupInfoId
    
    Parameters:
    localBackupInfoId	 (string):	localBackupInfo Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/backup/backupinfo/{localBackupInfoId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def downloadBackupFile(vmanage, path):
    """
    Download a Backup File that is already stored in vManage
    
    Parameters:
    path	 (string):	File path
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/backup/download/{path}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def exportBackup(vmanage, request):
    """
    Trigger a backup of configuration database and statstics database and store it in vManage
    
    Parameters:
    request:	backup request information
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/backup/export"
    response = vmanage.client.apiCall("POST", endpoint, request)
    return response
def listBackup(vmanage, size):
    """
    List all backup files of a tenant stored in vManage
    
    Parameters:
    size	 (string):	size
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/backup/list?size={size}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def importScheduledBackup(vmanage):
    """
    Submit a previously backed up file and import the data and apply it to the configuraion database
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/restore/import"
    response = vmanage.client.apiCall("POST", endpoint)
    return response
def remoteImportBackup(vmanage, payload):
    """
    Remote import backup from a remote URL and import the data and apply it to the configuraion database
    
    Parameters:
    payload:	Request Payload
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/restore/remoteimport"
    response = vmanage.client.apiCall("POST", endpoint, payload)
    return response
def scheduleBackup(vmanage, requestInfo):
    """
    create  backup scheduler config-db and statstics database with startDateTime and persist to config-db
    
    Parameters:
    requestInfo:	schedule request information
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/schedule/create"
    response = vmanage.client.apiCall("POST", endpoint, requestInfo)
    return response
def listSchedules(vmanage, limit):
    """
    Get a schedule record for backup by scheduler id
    
    Parameters:
    limit	 (integer):	size
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/schedule/list?limit={limit}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def getScheduleRecordForBackup(vmanage, schedulerId):
    """
    Get a schedule record for backup by scheduler id
    
    Parameters:
    schedulerId	 (string):	scheduler id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/schedule/{schedulerId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
def deleteSchedule(vmanage, schedulerId):
    """
    Delete a schedule record for backup in vManage by scheduler id
    
    Parameters:
    schedulerId	 (string):	scheduler id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/schedule/{schedulerId}"
    response = vmanage.client.apiCall("DELETE", endpoint)
    return response
