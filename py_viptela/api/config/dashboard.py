from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Dashboard(object):
    """
    Configuration - Dashboard Status API
    
    Implements GET POST DEL PUT methods for DashboardStatus endpoints

    """

    def __init__(self, session, host, port):
        self.client = HttpMethods.HttpClient(session=session)
        self.host = host
        self.port = port
    
    
    def cancelPending(self, processId):
        """
        Bulk cancel task status
        
        Parameters:
        processId	 (string):	Process Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/status/cancel/{processId}"
        response = self.client.apiCall(HttpMethods.POST, endpoint)
        return response


    def cleanStatus(self, cleanStatus):
        """
        Delete task and status vertex
        
        Parameters:
        cleanStatus	 (boolean):	Clear status flag
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/status/clean?cleanStatus={cleanStatus}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def deleteStatus(self, processId):
        """
        Delete status of action
        
        Parameters:
        processId	 (string):	Process Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/status/clear?processId={processId}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def findRunning(self):
        """
        Find running tasks
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/status/tasks"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getActiveCount(self):
        """
        Get active task count
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/status/tasks/activeCount"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCleanStatus(self, processId):
        """
        Delete task and status vertex
        
        Parameters:
        processId	 (string):	Process Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/status/tasks/clean?processId={processId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def findStatus(self, actionName):
        """
        Find status of action
        
        Parameters:
        actionName	 (string):	Action name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/device/action/status/{actionName}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


