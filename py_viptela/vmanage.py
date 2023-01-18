from py_viptela.restclient import RestClient
from py_viptela.query_builder import Builder

class Vmanage(RestClient):
    def __init__(self, host, port, username, password):
        super().__init__(host, port, username, password)
        self.builder = Builder()


    #login
    def get_jsessionid(self,):
        payload = {"j_username":self.username,"j_password":self.password }
        res = self.session.post(f"{self.baseurl}/j_security_check", data=payload)
        if res.cookies:
            return True
        else:
            return False

    def login(self,):
        if self.get_jsessionid():
            res = self.session.get(f"{self.baseurl}/dataservice/client/token", headers=self.headers)
            self.headers['X-XSRF-TOKEN'] = res.text
            return True, "Authentication Successful."
        else:
            return False, "Authentication Failed."

    def logout(self,):
        res = self.session.get(f"{self.baseurl}/logout", headers=self.headers)
        if res.status_code == 200:
            return True, "Logout Successful"
        else:
            return False, "Logout Failed"