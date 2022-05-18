from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Backup(object):
    """
    Scheduled Backup Restore API
    
    Implements GET POST DEL PUT methods for ScheduledBackupRestore endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def deleteSchduledBackup(self, taskId, backupInfoId):
        """
        Delete all or a specific backup file stored in vManage
        
        Parameters:
        taskId	 (string):	task id
		backupInfoId	 (string):	Local Backup Info Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/backup/backupinfo?taskId={taskId}&backupInfoId={backupInfoId}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def getLocalBackupInfo(self, localBackupInfoId):
        """
        Get a localBackupInfo record by localBackupInfoId
        
        Parameters:
        localBackupInfoId	 (string):	localBackupInfo Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/backup/backupinfo/{localBackupInfoId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def downloadBackupFile(self, path):
        """
        Download a Backup File that is already stored in vManage
        
        Parameters:
        path	 (string):	File path
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/backup/download/{path}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def exportBackup(self, request):
        """
        Trigger a backup of configuration database and statstics database and store it in vManage
        
        Parameters:
        request:	backup request information
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/backup/export"
        response = self.client.apiCall(HttpMethods.POST, endpoint, request)
        return response


    def listBackup(self, size):
        """
        List all backup files of a tenant stored in vManage
        
        Parameters:
        size	 (string):	size
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/backup/list?size={size}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def importScheduledBackup(self):
        """
        Submit a previously backed up file and import the data and apply it to the configuraion database
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/restore/import"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def remoteImportBackup(self, payload):
        """
        Remote import backup from a remote URL and import the data and apply it to the configuraion database
        
        Parameters:
        payload:	Request Payload
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/restore/remoteimport"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def scheduleBackup(self, requestInfo):
        """
        create  backup scheduler config-db and statstics database with startDateTime and persist to config-db
        
        Parameters:
        requestInfo:	schedule request information
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/schedule/create"
        response = self.client.apiCall(HttpMethods.POST, endpoint, requestInfo)
        return response


    def listSchedules(self, limit):
        """
        Get a schedule record for backup by scheduler id
        
        Parameters:
        limit	 (integer):	size
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/schedule/list?limit={limit}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getScheduleRecordForBackup(self, schedulerId):
        """
        Get a schedule record for backup by scheduler id
        
        Parameters:
        schedulerId	 (string):	scheduler id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/schedule/{schedulerId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def deleteSchedule(self, schedulerId):
        """
        Delete a schedule record for backup in vManage by scheduler id
        
        Parameters:
        schedulerId	 (string):	scheduler id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/schedule/{schedulerId}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


