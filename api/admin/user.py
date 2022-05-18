from py_viptela.query_builder import Builder
from py_viptela import HttpMethods

class User(object):
    """
    Administration - User and Group API
    
    Implements GET POST DEL PUT methods for UserandGroup endpoints

    """

    def __init__(self, session, host, port):
        self.host = host
        self.port = port
        self.client = HttpMethods.HttpClient(session=session)
    
    def getColoGroups(self):
        """
        Get COLO groups
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/cologroup"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createColoGroup(self, colocationgroup):
        """
        Add COLO group
        
        Parameters:
        colocationgroup:	Colocation group
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/cologroup"
        response = self.client.apiCall(HttpMethods.POST, endpoint, colocationgroup)
        return response


    def editColoGroup(self, colocationgroup, id):
        """
        Update COLO group
        
        Parameters:
        colocationgroup:	Colocation group
		id	 (string):	Colocation group Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/cologroup/{id}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, colocationgroup)
        return response


    def deleteColoGroup(self, id):
        """
        Delete COLO group
        
        Parameters:
        id	 (string):	Colocation group Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/cologroup/{id}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def getResourceGroups(self):
        """
        Get all groups
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/resourcegroup"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createResourceGroup(self, createagroup):
        """
        Create a group
        
        Parameters:
        createagroup:	Create a group
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/resourcegroup"
        response = self.client.apiCall(HttpMethods.POST, endpoint, createagroup)
        return response


    def switchView(self, groupView):
        """
        Global netadmin switches to a different resource group view
        
        Parameters:
        groupView:	Global netadmin switches to a different resource group view
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/resourcegroup/switch"
        response = self.client.apiCall(HttpMethods.POST, endpoint, groupView)
        return response


    def editResourceGroup(self, updategroupdescription, groupId):
        """
        Update a group
        
        Parameters:
        groupdesc:  (string)	Update group description
		groupId:    (string)    Resource group Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/resourcegroup/{groupId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, updategroupdescription)
        return response


    def deleteResourceGroup(self, groupId):
        """
        Delete a group
        
        Parameters:
        groupId:    (string)    Resource group Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/resourcegroup/{groupId}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def findUsers(self):
        """
        Get all users
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/user"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createUser(self, user):
        """
        Create a user
        
        Parameters:
        user:	User
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/user"
        response = self.client.apiCall(HttpMethods.POST, endpoint, user)
        return response


    def getActiveSessions(self):
        """
        Get active sessions
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/user/activeSessions"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateAdminPassword(self, user):
        """
        Update admin default password
        
        Parameters:
        user:	User
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/user/admin/password"
        response = self.client.apiCall(HttpMethods.POST, endpoint, user)
        return response


    def validatePassword(self, userpassword):
        """
        Validate user password
        
        Parameters:
        userpassword:	User password
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/user/password/validate"
        response = self.client.apiCall(HttpMethods.POST, endpoint, userpassword)
        return response


    def updatePassword(self, user, userName):
        """
        Update user password
        
        Parameters:
        user:	User
		userName	 (string):	User name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/user/password/{userName}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, user)
        return response


    def updateProfileLocale(self, user):
        """
        Update profile locale
        
        Parameters:
        user:	User
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/user/profile/locale"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, user)
        return response


    def updateProfilePassword(self, user):
        """
        Update profile password
        
        Parameters:
        user:	User
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/user/profile/password"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, user)
        return response


    def removeSessions(self, user):
        """
        Remove sessions
        
        Parameters:
        user:	User
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/user/removeSessions"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint, user)
        return response


    def resetUser(self, user):
        """
        Unlock a user
        
        Parameters:
        user:	User
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/user/reset"
        response = self.client.apiCall(HttpMethods.POST, endpoint, user)
        return response


    def resourceGroupName(self):
        """
        Get the name of the resource group associated with the current logged in user
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/user/resourceGroupName"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def findUserRole(self):
        """
        Check whether a user has admin role
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/user/role"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def findUserAuthType(self):
        """
        Find user authentication type, whether it is SAML enabled
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/user/userAuthType"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateUser(self, user, userName):
        """
        Update user
        
        Parameters:
        user:	                User
		userName	 (string):	User name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/user/{userName}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, user)
        return response


    def deleteUser(self, userName):
        """
        Delete user
        
        Parameters:
        userName	 (string):	User name
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/user/{userName}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def findUserGroups(self):
        """
        Get all user groups
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/usergroup"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createUserGroup(self, usergroup):
        """
        Create user group
        
        Parameters:
        usergroup:	User group
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/usergroup"
        response = self.client.apiCall(HttpMethods.POST, endpoint, usergroup)
        return response


    def createGroupGridColumns(self):
        """
        Get user groups in a grid table
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/usergroup/definition"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def findUserGroupsAsKeyValue(self):
        """
        Get user groups as key value map
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/usergroup/keyvalue"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def updateUserGroup(self, usergroup, userGroupId):
        """
        Update user group
        
        Parameters:
        usergroup:	            User group
		userGroupId	 (string):	User group Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/usergroup/{userGroupId}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, usergroup)
        return response


    def deleteUserGroup(self, userGroupId):
        """
        Delete user group
        
        Parameters:
        userGroupId	 (string):	User group Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/usergroup/{userGroupId}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


    def getVpnGroups(self):
        """
        Get VPN groups
        
        Parameters:
                
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/vpngroup"
        response = self.client.apiCall(HttpMethods.GET, endpoint)
        return response


    def createVpnGroup(self, vpngroup):
        """
        Add VPN group
        
        Parameters:
        vpngroup:	VPN group
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/vpngroup"
        response = self.client.apiCall(HttpMethods.POST, endpoint, vpngroup)
        return response


    def editVpnGroup(self, vpngroup, id):
        """
        Update VPN group
        
        Parameters:
        vpngroup:	VPN group
		id	 (string):	VPN group Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/vpngroup/{id}"
        response = self.client.apiCall(HttpMethods.PUT, endpoint, vpngroup)
        return response


    def deleteVpnGroup(self, id):
        """
        Delete VPN group
        
        Parameters:
        id	 (string):	VPN group Id
        
        Returns
        response    (dict)
        
        
        """
        
        endpoint = f"https://{self.host}:{self.port}/dataservice/admin/vpngroup/{id}"
        response = self.client.apiCall(HttpMethods.DELETE, endpoint)
        return response


