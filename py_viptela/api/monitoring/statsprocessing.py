def getStatisticType(vmanage):
    """
    Get statistics types
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics"
    response = vmanage.apiCall("GET", endpoint)
    return response
def startStatsCollection(vmanage):
    """
    Start stats collect
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/collect"
    response = vmanage.apiCall("GET", endpoint)
    return response
def generateStatsCollectThreadReport(vmanage):
    """
    Get stats collect thread report
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/collect/thread/status"
    response = vmanage.apiCall("GET", endpoint)
    return response
def resetStatsCollection(vmanage, processQueue):
    """
    Reset stats collect thread report
    
    Parameters:
    processQueue	 (integer):	Process queue
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/collection/reset/{processQueue}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def enableStatsDemo(vmanage, enable):
    """
    Enable statistic demo mode
    
    Parameters:
    enable	 (boolean):	Demo mode flag
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/demomode?enable={enable}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def processStatsData(vmanage):
    """
    Process stats data
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/process"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getStatsProcessingCounters(vmanage):
    """
    Get statistics processing counters
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/process/counters"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getStatsProcessReport(vmanage, processQueue):
    """
    Get stats process report
    
    Parameters:
    processQueue	 (integer):	Process queue
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/process/status?processQueue={processQueue}"
    response = vmanage.apiCall("GET", endpoint)
    return response
def getStatsProcessThreadReport(vmanage):
    """
    Get stats process thread report
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/statistics/process/thread/status"
    response = vmanage.apiCall("GET", endpoint)
    return response
