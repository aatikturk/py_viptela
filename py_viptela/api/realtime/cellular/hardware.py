from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class Hardware(object):
    """
    Real-Time Monitoring - Cellular EIOLTE Hardware Service  API
    
    Implements GET POST DEL PUT methods for CellularEIOLTEHardwareService endpoints

    """

    def __init__(vmanage, session, host, port):
        vmanage.host = host
        vmanage.port = port
        vmanage.client = HttpMethods.HttpClient(session=session)
    
    
    def getHardwareInfo(vmanage, deviceId):
        """
        Get cellular hardware info from device
        
        Parameters:
        deviceId	 (string):	Device Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/device/cellularEiolte/hardware?deviceId={deviceId}"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


