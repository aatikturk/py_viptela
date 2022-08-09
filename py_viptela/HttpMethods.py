from py_viptela.response_parser import parse_response
import requests

# CONSTANTS
GET = "GET"
POST = "POST"
PUT = "PUT"
DELETE = "DELETE"

class HttpClient(object):
    
    """
    TODO: methods for this class will be implemented last
    """
    def __init__(self, session):
        self.session = session

    def apiCall(self, method, url, body=None):
        methods = {
            "GET":self.session.get,
            "POST": self.session.post,
            "PUT": self.session.put,
            "DELETE": self.session.delete
        }
        
        try:
            response = methods[method](url=url, data=body)

        except requests.exceptions.ConnectTimeout:
            return{'error': 'Connection Timeout'}

        except requests.exceptions.ConnectionError:
            return {'error': 'Connection Failed'}
            
        except requests.exceptions.Timeout:
            return {'error': 'Timeout'}

        else:
            return parse_response(response)