def getDspActive(vmanage, deviceId):
    """
    Get DSPFarm Active DSP info from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/voice/dspActive?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getPhoneInfo(vmanage, deviceId):
    """
    Get phone registration info from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/voice/phoneInfo?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getDSPFarmProfiles(vmanage, deviceId):
    """
    Get DSPFarm Profiles info from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/voice/profiles?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getSccpCcmGroups(vmanage, deviceId):
    """
    Get DSPFarm SCCP CCM Groups info from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/voice/sccpCcmGroups?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getSccpConnections(vmanage, deviceId):
    """
    Get DSPFarm SCCP Connections info from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/voice/sccpConnections?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getVoiceCalls(vmanage, deviceId):
    """
    Get voice call info from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/voice/voiceCalls?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getVoipCalls(vmanage, deviceId):
    """
    Get VOIP call info from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/voice/voipCalls?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getIsdnStatus(vmanage, deviceId):
    """
    Retrieve Voice ISDN Status from device
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/voiceisdninfo/isdnstatus?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getControllerInfo(vmanage, deviceId):
    """
    Retrieve T1E1 controller last 15 min stats from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/voicet1e1controllerinfo/current15minstats?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getControllerStats(vmanage, deviceId):
    """
    Retrieve T1E1 controller total stats from device (Real Time)
    
    Parameters:
    deviceId	 (string):	Device Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/device/voicet1e1controllerinfo/totalstats?deviceId={deviceId}"
    response = vmanage.apiCall("GET", endpoint)
    return response
