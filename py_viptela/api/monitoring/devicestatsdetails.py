from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class DeviceStatisticsDetails(object):
    """
    Monitoring - Device Statistics Details API
    
    Implements GET POST DEL PUT methods for DeviceStatisticsDetails endpoints

    """

    def __init__(vmanage, session, host, port):
        vmanage.client = HttpMethods.HttpClient(session=session)
        vmanage.host = host
        vmanage.port = port
    
    
    def getStatisticsType(vmanage):
        """
        Get statistics types
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/data/device/statistics"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getActiveAlarms(vmanage, scrollId, startDate, endDate, count, timeZone):
        """
        Get active alarms
        
        Parameters:
        scrollId	 (string):	SrollId
		startDate	 (string):	Start date
		endDate	 (string):	End date
		count	 (integer):	count
		timeZone	 (string):	Time zone
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/data/device/statistics/alarm/active?scrollId={scrollId}&startDate={startDate}&endDate={endDate}&count={count}&timeZone={timeZone}"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getStatsData(vmanage, state_data_type, scrollId, startDate, endDate, count, timeZone):
        """
        Get device statistics data
        
        Parameters:
        state_data_type	 (string):	State data type
		scrollId	 (string):	Scroll Id
		startDate	 (string):	Start date
		endDate	 (string):	End date
		Parameter Description
		timeZone	 (string):	Time zone
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/data/device/statistics/{state_data_type}?scrollId={scrollId}&startDate={startDate}&endDate={endDate}&count={count}&timeZone={timeZone}"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getCountWithStateDataType(vmanage, state_data_type, startDate, endDate, timeZone):
        """
        Get response count of a query
        
        Parameters:
        state_data_type	 (string):	State data type
		startDate	 (string):	Start date
		endDate	 (string):	End date
		timeZone	 (string):	Time zone
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/data/device/statistics/{state_data_type}/doccount?startDate={startDate}&endDate={endDate}&timeZone={timeZone}"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def getFieldsByType(vmanage, state_data_type):
        """
        Get statistics fields and types
        
        Parameters:
        state_data_type	 (string):	State data type
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/data/device/statistics/{state_data_type}/fields"
        response = vmanage.client.apiCall(HttpMethods.GET, endpoint)
        return response


