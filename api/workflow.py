from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Workflow(object):
    """
    Workflow - Management API
    
    Implements GET POST DEL PUT methods for Management endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getWorkflows(self, type, id):
        """
        List all workflows for the given tenant
        
        Parameters:
        type	 (string):	Workflow type
		id	 (string):	Workflow id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/workflow?type={type}&id={id}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def saveWorkflow(self, payload):
        """
        Saves the workflow
        
        Parameters:
        payload:	Request to save already created workflow with given user context
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/workflow"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, payload)
        return response


    def createWorkflow(self, payload):
        """
        Creates a workflow in the system
        
        Parameters:
        payload:	Request to create workflow with given user context
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/workflow"
        response = self.client.apiCall(HttpMethods.POST, endpoint, payload)
        return response


    def deleteWorkflow(self, payload, id):
        """
        Deletes the workflow
        
        Parameters:
        payload:	Request to delete the workflow
		id	 (string):	Workflow id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/workflow?id={id}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint, payload)
        return response


