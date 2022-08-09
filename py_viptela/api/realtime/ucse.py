def createUcseStats(vmanage, remote_tloc_address, remote_tloc_color, local_tloc_color, deviceId):
    """
    Get  UCSE stats entry from device
    
    Parameters:
    remote_tloc_address	 (string):	Remote TLOC address
	remote_tloc_color	 (string):	Remote tloc color
	local_tloc_color	 (string):	Local tloc color
	deviceId	 (string):	Device IP
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/ucse/stats?remote-tloc-address={remote_tloc_address}&remote-tloc-color={remote_tloc_color}&local-tloc-color={local_tloc_color}&deviceId={deviceId}"
    response = vmanage.client.apiCall("GET", endpoint)
    return response
