def preview(vmanage, policyassembly):
    """
    Get policy assembly preview
    
    Parameters:
    policyassembly:	Policy assembly
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/assembly/vsmart"
    response = vmanage.client.apiCall("POST", endpoint, policyassembly)
    return response


def previewById(vmanage, id):
    """
    Get policy assembly preview
    
    Parameters:
    id	 (string):	Policy Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/template/policy/assembly/vsmart/{id}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
    