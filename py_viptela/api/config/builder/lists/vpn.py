from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class VPN(object):
    """
    Configuration - Policy VPN List Builder API
    
    Implements GET POST DEL PUT methods for PolicyVPNListBuilder endpoints

    """

    def __init__(vmanage, session, host, port):
        vmanage.host = host
        vmanage.port = port
        vmanage.client = HttpMethods.HttpClient(session=session)
    
    
    def get(vmanage):
        """
        Get policy lists
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/vpn"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def create(vmanage, policylist):
        """
        Create policy list
        
        Parameters:
        policylist:	Policy list
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/vpn"
        response = vmanage.client.apiCall(HttpMethods.POST, endpoint, policylist)
        return response


    def preview(vmanage, policylist):
        """
        Preview a policy list based on the policy list type
        
        Parameters:
        policylist:	Policy list
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/vpn/preview"
        response = vmanage.client.apiCall(HttpMethods.POST, endpoint, policylist)
        return response


    def previewById(vmanage, id):
        """
        Preview a specific policy list entry based on id provided
        
        Parameters:
        id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/vpn/preview/{id}"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getListsById(vmanage, id):
        """
        Get a specific policy list based on the id
        
        Parameters:
        id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/vpn/{id}"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def edit(vmanage, policylist, id):
        """
        Edit policy list entries for a specific type of policy list
        
        Parameters:
        policylist:	Policy list
		id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/vpn/{id}"
        response = vmanage.client.apiCall(HttpMethods.PUT, endpoint, policylist)
        return response


    def delete(vmanage, id):
        """
        Delete policy list entry for a specific type of policy list
        
        Parameters:
        id	 (string):	Policy Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/list/vpn/{id}"
        response = vmanage.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


