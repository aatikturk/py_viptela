def preview(vmanage, policyassembly):
    """
    Get policy assembly preview
    
    Parameters:
    policyassembly:	Policy assembly
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/assembly/vedge"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, policyassembly)
    return response

def previewById(vmanage, id):
    """
    Get policy assembly preview
    
    Parameters:
    id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/assembly/vedge/{id}"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
