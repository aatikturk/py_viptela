def getsupportedLocales(vmanage):
    """
    Get Supported locales
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/localization/supportedLocales"
    response = vmanage.apiCall("GET", endpoint)
    return response
