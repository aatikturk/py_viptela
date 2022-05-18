from requests import Session
import json
import urllib3

class Vmanage(object):
    
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.session = Session()
        self.session.headers['Content-Type'] = 'application/x-www-form-urlencoded'
        self.session.verify = False
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        #login
        self.login_url = f"https://{host}:{port}/j_security_check"
        login_data = {
            "j_username":self.username,
            "j_password":self.password
        }
        self.session.post(url=self.login_url, data=login_data)

        #get token
        response = self.session.get(url=f"https://{host}:{port}/dataservice/client/token")
        token = response.text

        # configure headers for further use
        self.session.headers['Content-Type'] = 'application/json'
        self.session.headers['X-XSRF-TOKEN'] = token
        