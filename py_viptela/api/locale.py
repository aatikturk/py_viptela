def getsupportedLocales(vmanage):
    """
    Get Supported locales
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/localization/supportedLocales"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response
