import requests
from py_viptela.response_parser import parse_response


class RestClient:
    """
    TODO: methods for this class will be implemented last
    """

    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.session.verify = False
        self.headers = {'Content-Type':'application/json'}
        self.baseurl = f"https://{self.host}:{self.port}"

    def apiCall(self, method, endpoint, payload=None):
        methods = {
            "GET":self.session.get,
            "POST": self.session.post,
            "PUT": self.session.put,
            "DELETE": self.session.delete
        }
        url = f"{self.baseurl}/{endpoint}"

        try:
            response = methods[method](url=url, headers=self.headers, data=payload)
        except requests.exceptions.SSLError:
            return{'error': 'SSL Error'}
        except requests.exceptions.ConnectTimeout:
            return{'error': 'Connection Timeout'}
        except requests.exceptions.ConnectionError:
            return {'error': 'Connection Failed'}
        except requests.exceptions.Timeout:
            return {'error': 'Timeout'}
        else:
            return parse_response(response)