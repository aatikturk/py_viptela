[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/aatikturk/py-viptela)

# py-viptela
### A Python SDK for Cisco SD-WAN vManage API(20.6.2)

This is supposed to be a wrapper around Cisco's vManage API. There's a similar solution provided by Cisco and can be accessed [from DevNet website](https://developer.cisco.com/codeexchange/github/repo/CiscoDevNet/python-viptela/)

Also from [github](https://github.com/CiscoDevNet/python-viptela)

* #### Why another solution?
    It's a great way to learn new things by building things.

* #### Is it completed or a work-in-progress project?
    This started as a hobby project and still in progress. 
   
* #### How can I use this?
    A How-To document will be available after phase-1, which is implementing all the API endpoints, is completed.

* #### Contributions?
    Highly appreciated and welcome.
    

All Endpoints in vManage API are implemented using the vmanage.json file available through vmanage/apidocs page as a reference

## How to Use

* Clone this repo into your computer.
```
git clone https://github.com/aatikturk/py-viptela
```

* Change directory to "py-viptela"
```
cd py-viptela
```

* Import vmanage module and initiate an instance, and import any api module
  Required parameters are as follows:
    host:       Ip address of the vManage
    port:       port to access vmanage
    username:   vManage username
    password:   vManage password

```
>>>from vmanage import Vmanage
>>>from api.admin.user import User
>>>
>>>vmanage = Vmanage(host='198.18.1.10', port=443, username='admin', password='testpassword')
>>>
```

You're ready to make requests using api endpoints. 

Example:  Get all users from the vManage

```
>>>user_api = User(session=vmanage.session, host=vmanage.host, port=vmanage.port)
>>>
>>>users = user_api.findUsers()
>>>
>>>users
[{'userName': 'admin', 'locale': 'en_US', 'group': []},
 {'userName': 'dclouddemo',
  'description': 'Administrator',
  'locale': 'en_US',
  'resGroupName': 'global',
  'group': ['netadmin']}]
```
