from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def getsupportedLocales(vmanage):
    """
    Get Supported locales
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/localization/supportedLocales"
    response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
    return response
