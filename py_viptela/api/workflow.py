from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

    
def getWorkflows(vmanage, type, id):
    """
    List all workflows for the given tenant
    
    Parameters:
    type	 (string):	Workflow type
	id	 (string):	Workflow id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/workflow?type={type}&id={id}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
def saveWorkflow(vmanage, payload):
    """
    Saves the workflow
    
    Parameters:
    payload:	Request to save already created workflow with given user context
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/workflow"
    response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, payload)
    return response
def createWorkflow(vmanage, payload):
    """
    Creates a workflow in the system
    
    Parameters:
    payload:	Request to create workflow with given user context
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/workflow"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, payload)
    return response
def deleteWorkflow(vmanage, payload, id):
    """
    Deletes the workflow
    
    Parameters:
    payload:	Request to delete the workflow
	id	 (string):	Workflow id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/workflow?id={id}"
    response = vmanage.client.apiCall(HttpMethods.DELETE, endpoint, payload)
    return response
