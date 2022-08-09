from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def preview(vmanage, policyassembly):
    """
    Get policy assembly preview
    
    Parameters:
    policyassembly:	Policy assembly
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/assembly/voice"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, policyassembly)
    return response


def previewById(vmanage, id):
    """
    Get policy assembly preview
    
    Parameters:
    id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/assembly/voice/{id}"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
