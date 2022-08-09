def pushConfigs(vmanage, config, nmsId):
    """
    Push device configs
    
    Parameters:
    config:	            Netconf configuration
	nmsId	 (string):	NMS Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/partner/wcm/netconf/{nmsId}"
    response = vmanage.apiCall("POST", endpoint, config)
    return response
