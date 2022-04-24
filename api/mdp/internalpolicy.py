from query_builder import Builder
import HttpMethods

class Policy(object):
    """
    MDP - Internal Policy Management API
    
    Implements GET POST DEL PUT methods for InternalPolicyManagement endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def addInternalPolicy(self, addinternalpolicy):
        """
        Add internal policy from vmanage
        
        Parameters:
        addinternalpolicy:	addInternalPolicy
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/mdp/policies/mdpconfig"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, addinternalpolicy)
        return response


