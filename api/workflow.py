from query_builder import Builder
import HttpMethods

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


    def saveWorkflow(self, requesttosavealreadycreatedworkflowwithgivenusercontext):
        """
        Saves the workflow
        
        Parameters:
        requesttosavealreadycreatedworkflowwithgivenusercontext:	Request to save already created workflow with given user context
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/workflow"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, requesttosavealreadycreatedworkflowwithgivenusercontext)
        return response


    def createWorkflow(self, requesttocreateworkflowwithgivenusercontext):
        """
        Creates a workflow in the system
        
        Parameters:
        requesttocreateworkflowwithgivenusercontext:	Request to create workflow with given user context
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/workflow"
        response = self.client.apiCall(HttpMethods.POST, endpoint, requesttocreateworkflowwithgivenusercontext)
        return response


    def deleteWorkflow(self, requesttodeletetheworkflow, id):
        """
        Deletes the workflow
        
        Parameters:
        requesttodeletetheworkflow:	Request to delete the workflow
		id	 (string):	Workflow id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/workflow?id={id}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint, requesttodeletetheworkflow)
        return response


