from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

def pushConfigs(vmanage, config, nmsId):
    """
    Push device configs
    
    Parameters:
    config:	            Netconf configuration
	nmsId	 (string):	NMS Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/partner/wcm/netconf/{nmsId}"
    response = vmanage.client.apiCall(HttpMethods.POST, endpoint, config)
    return response
