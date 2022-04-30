from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Onboard(object):
    """
    MDP - Onboarding API
    
    Implements GET POST DEL PUT methods for Onboarding endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    
    def onboardMDP(self, onboard):
        """
        Start MDP onboarding operation
        
        Parameters:
        onboard:	Onboard
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/mdp/onboard"
        response = self.client.apiCall(HttpMethods.POST, endpoint, onboard)
        return response


    def getOnboardStatus(self):
        """
        Get MDP onboarding status
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/mdp/onboard/status"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateOnboardingPayload(self, onboard, nmsId):
        """
        update MDP onboarding document
        
        Parameters:
        onboard:	Onboard
		Parameter Description
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/mdp/onboard/{nmsId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, onboard)
        return response


