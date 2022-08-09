



def getColoGroups(vmanage):
    """
    Get COLO groups
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/cologroup"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def createColoGroup(vmanage, colocationgroup):
    """
    Add COLO group
    
    Parameters:
    colocationgroup:	Colocation group
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/cologroup"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, colocationgroup)
    return response

def editColoGroup(vmanage, colocationgroup, id):
    """
    Update COLO group
    
    Parameters:
    colocationgroup:	Colocation group
	id	 (string):	Colocation group Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/cologroup/{id}"
    response = vmanage.client.apiCall(vmanage.PUT, endpoint, colocationgroup)
    return response

def deleteColoGroup(vmanage, id):
    """
    Delete COLO group
    
    Parameters:
    id	 (string):	Colocation group Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/cologroup/{id}"
    response = vmanage.client.apiCall(vmanage.DELETE, endpoint)
    return response

def getResourceGroups(vmanage):
    """
    Get all groups
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/resourcegroup"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def createResourceGroup(vmanage, createagroup):
    """
    Create a group
    
    Parameters:
    createagroup:	Create a group
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/resourcegroup"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, createagroup)
    return response

def switchView(vmanage, groupView):
    """
    Global netadmin switches to a different resource group view
    
    Parameters:
    groupView:	Global netadmin switches to a different resource group view
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/resourcegroup/switch"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, groupView)
    return response

def editResourceGroup(vmanage, updategroupdescription, groupId):
    """
    Update a group
    
    Parameters:
    groupdesc:  (string)	Update group description
	groupId:    (string)    Resource group Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/resourcegroup/{groupId}"
    response = vmanage.client.apiCall(vmanage.PUT, endpoint, updategroupdescription)
    return response

def deleteResourceGroup(vmanage, groupId):
    """
    Delete a group
    
    Parameters:
    groupId:    (string)    Resource group Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/resourcegroup/{groupId}"
    response = vmanage.client.apiCall(vmanage.DELETE, endpoint)
    return response

def findUsers(vmanage):
    """
    Get all users
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/user"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def createUser(vmanage, user):
    """
    Create a user
    
    Parameters:
    user:	User
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/user"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, user)
    return response

def getActiveSessions(vmanage):
    """
    Get active sessions
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/user/activeSessions"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def updateAdminPassword(vmanage, user):
    """
    Update admin default password
    
    Parameters:
    user:	User
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/user/admin/password"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, user)
    return response

def validatePassword(vmanage, userpassword):
    """
    Validate user password
    
    Parameters:
    userpassword:	User password
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/user/password/validate"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, userpassword)
    return response

def updatePassword(vmanage, user, userName):
    """
    Update user password
    
    Parameters:
    user:	User
	userName	 (string):	User name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/user/password/{userName}"
    response = vmanage.client.apiCall(vmanage.PUT, endpoint, user)
    return response

def updateProfileLocale(vmanage, user):
    """
    Update profile locale
    
    Parameters:
    user:	User
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/user/profile/locale"
    response = vmanage.client.apiCall(vmanage.PUT, endpoint, user)
    return response

def updateProfilePassword(vmanage, user):
    """
    Update profile password
    
    Parameters:
    user:	User
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/user/profile/password"
    response = vmanage.client.apiCall(vmanage.PUT, endpoint, user)
    return response

def removeSessions(vmanage, user):
    """
    Remove sessions
    
    Parameters:
    user:	User
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/user/removeSessions"
    response = vmanage.client.apiCall(vmanage.DELETE, endpoint, user)
    return response

def resetUser(vmanage, user):
    """
    Unlock a user
    
    Parameters:
    user:	User
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/user/reset"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, user)
    return response

def resourceGroupName(vmanage):
    """
    Get the name of the resource group associated with the current logged in user
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/user/resourceGroupName"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def findUserRole(vmanage):
    """
    Check whether a user has admin role
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/user/role"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def findUserAuthType(vmanage):
    """
    Find user authentication type, whether it is SAML enabled
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/user/userAuthType"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def updateUser(vmanage, user, userName):
    """
    Update user
    
    Parameters:
    user:	                User
	userName	 (string):	User name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/user/{userName}"
    response = vmanage.client.apiCall(vmanage.PUT, endpoint, user)
    return response

def deleteUser(vmanage, userName):
    """
    Delete user
    
    Parameters:
    userName	 (string):	User name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/user/{userName}"
    response = vmanage.client.apiCall(vmanage.DELETE, endpoint)
    return response

def findUserGroups(vmanage):
    """
    Get all user groups
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/usergroup"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def createUserGroup(vmanage, usergroup):
    """
    Create user group
    
    Parameters:
    usergroup:	User group
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/usergroup"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, usergroup)
    return response

def createGroupGridColumns(vmanage):
    """
    Get user groups in a grid table
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/usergroup/definition"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def findUserGroupsAsKeyValue(vmanage):
    """
    Get user groups as key value map
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/usergroup/keyvalue"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def updateUserGroup(vmanage, usergroup, userGroupId):
    """
    Update user group
    
    Parameters:
    usergroup:	            User group
	userGroupId	 (string):	User group Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/usergroup/{userGroupId}"
    response = vmanage.client.apiCall(vmanage.PUT, endpoint, usergroup)
    return response

def deleteUserGroup(vmanage, userGroupId):
    """
    Delete user group
    
    Parameters:
    userGroupId	 (string):	User group Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/usergroup/{userGroupId}"
    response = vmanage.client.apiCall(vmanage.DELETE, endpoint)
    return response

def getVpnGroups(vmanage):
    """
    Get VPN groups
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/vpngroup"
    response = vmanage.client.apiCall(vmanage.GET, endpoint)
    return response

def createVpnGroup(vmanage, vpngroup):
    """
    Add VPN group
    
    Parameters:
    vpngroup:	VPN group
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/vpngroup"
    response = vmanage.client.apiCall(vmanage.POST, endpoint, vpngroup)
    return response

def editVpnGroup(vmanage, vpngroup, id):
    """
    Update VPN group
    
    Parameters:
    vpngroup:	VPN group
	id	 (string):	VPN group Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/vpngroup/{id}"
    response = vmanage.client.apiCall(vmanage.PUT, endpoint, vpngroup)
    return response

def deleteVpnGroup(vmanage, id):
    """
    Delete VPN group
    
    Parameters:
    id	 (string):	VPN group Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"https://{vmanage.host}:{vmanage.port}/dataservice/admin/vpngroup/{id}"
    response = vmanage.client.apiCall(vmanage.DELETE, endpoint)
    return response


