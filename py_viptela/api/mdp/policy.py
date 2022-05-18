from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Policy(object):
    """
    MDP - Policy Management API
    
    Implements GET POST DEL PUT methods for Policy Management endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def getPolicies(self, nmsId):
        """
        Retrieve MDP policies
        
        Parameters:
        nmsId:  NMS server ID
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/mdp/policies/{nmsId}"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updatePolicyStatus(self, policylist, nmsId):
        """
        update policy status
        
        Parameters:
        policylist:	policyList
		nmsId:  NMS server ID
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/mdp/policies/{nmsId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, policylist)
        return response


