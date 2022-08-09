



def getColoGroups(vmanage):
    """
    Get COLO groups
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/cologroup"
    response = vmanage.apiCall("GET", endpoint)
    return response

def createColoGroup(vmanage, colocationgroup):
    """
    Add COLO group
    
    Parameters:
    colocationgroup:	Colocation group
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/cologroup"
    response = vmanage.apiCall("POST", endpoint, colocationgroup)
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
    
    endpoint = f"dataservice/admin/cologroup/{id}"
    response = vmanage.apiCall("PUT", endpoint, colocationgroup)
    return response

def deleteColoGroup(vmanage, id):
    """
    Delete COLO group
    
    Parameters:
    id	 (string):	Colocation group Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/cologroup/{id}"
    response = vmanage.apiCall("DELETE", endpoint)
    return response

def getResourceGroups(vmanage):
    """
    Get all groups
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/resourcegroup"
    response = vmanage.apiCall("GET", endpoint)
    return response

def createResourceGroup(vmanage, createagroup):
    """
    Create a group
    
    Parameters:
    createagroup:	Create a group
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/resourcegroup"
    response = vmanage.apiCall("POST", endpoint, createagroup)
    return response

def switchView(vmanage, groupView):
    """
    Global netadmin switches to a different resource group view
    
    Parameters:
    groupView:	Global netadmin switches to a different resource group view
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/resourcegroup/switch"
    response = vmanage.apiCall("POST", endpoint, groupView)
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
    
    endpoint = f"dataservice/admin/resourcegroup/{groupId}"
    response = vmanage.apiCall("PUT", endpoint, updategroupdescription)
    return response

def deleteResourceGroup(vmanage, groupId):
    """
    Delete a group
    
    Parameters:
    groupId:    (string)    Resource group Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/resourcegroup/{groupId}"
    response = vmanage.apiCall("DELETE", endpoint)
    return response

def findUsers(vmanage):
    """
    Get all users
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/user"
    response = vmanage.apiCall("GET", endpoint)
    return response

def createUser(vmanage, user):
    """
    Create a user
    
    Parameters:
    user:	User
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/user"
    response = vmanage.apiCall("POST", endpoint, user)
    return response

def getActiveSessions(vmanage):
    """
    Get active sessions
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/user/activeSessions"
    response = vmanage.apiCall("GET", endpoint)
    return response

def updateAdminPassword(vmanage, user):
    """
    Update admin default password
    
    Parameters:
    user:	User
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/user/admin/password"
    response = vmanage.apiCall("POST", endpoint, user)
    return response

def validatePassword(vmanage, userpassword):
    """
    Validate user password
    
    Parameters:
    userpassword:	User password
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/user/password/validate"
    response = vmanage.apiCall("POST", endpoint, userpassword)
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
    
    endpoint = f"dataservice/admin/user/password/{userName}"
    response = vmanage.apiCall("PUT", endpoint, user)
    return response

def updateProfileLocale(vmanage, user):
    """
    Update profile locale
    
    Parameters:
    user:	User
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/user/profile/locale"
    response = vmanage.apiCall("PUT", endpoint, user)
    return response

def updateProfilePassword(vmanage, user):
    """
    Update profile password
    
    Parameters:
    user:	User
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/user/profile/password"
    response = vmanage.apiCall("PUT", endpoint, user)
    return response

def removeSessions(vmanage, user):
    """
    Remove sessions
    
    Parameters:
    user:	User
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/user/removeSessions"
    response = vmanage.apiCall("DELETE", endpoint, user)
    return response

def resetUser(vmanage, user):
    """
    Unlock a user
    
    Parameters:
    user:	User
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/user/reset"
    response = vmanage.apiCall("POST", endpoint, user)
    return response

def resourceGroupName(vmanage):
    """
    Get the name of the resource group associated with the current logged in user
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/user/resourceGroupName"
    response = vmanage.apiCall("GET", endpoint)
    return response

def findUserRole(vmanage):
    """
    Check whether a user has admin role
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/user/role"
    response = vmanage.apiCall("GET", endpoint)
    return response

def findUserAuthType(vmanage):
    """
    Find user authentication type, whether it is SAML enabled
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/user/userAuthType"
    response = vmanage.apiCall("GET", endpoint)
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
    
    endpoint = f"dataservice/admin/user/{userName}"
    response = vmanage.apiCall("PUT", endpoint, user)
    return response

def deleteUser(vmanage, userName):
    """
    Delete user
    
    Parameters:
    userName	 (string):	User name
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/user/{userName}"
    response = vmanage.apiCall("DELETE", endpoint)
    return response

def findUserGroups(vmanage):
    """
    Get all user groups
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/usergroup"
    response = vmanage.apiCall("GET", endpoint)
    return response

def createUserGroup(vmanage, usergroup):
    """
    Create user group
    
    Parameters:
    usergroup:	User group
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/usergroup"
    response = vmanage.apiCall("POST", endpoint, usergroup)
    return response

def createGroupGridColumns(vmanage):
    """
    Get user groups in a grid table
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/usergroup/definition"
    response = vmanage.apiCall("GET", endpoint)
    return response

def findUserGroupsAsKeyValue(vmanage):
    """
    Get user groups as key value map
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/usergroup/keyvalue"
    response = vmanage.apiCall("GET", endpoint)
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
    
    endpoint = f"dataservice/admin/usergroup/{userGroupId}"
    response = vmanage.apiCall("PUT", endpoint, usergroup)
    return response

def deleteUserGroup(vmanage, userGroupId):
    """
    Delete user group
    
    Parameters:
    userGroupId	 (string):	User group Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/usergroup/{userGroupId}"
    response = vmanage.apiCall("DELETE", endpoint)
    return response

def getVpnGroups(vmanage):
    """
    Get VPN groups
    
    Parameters:
            
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/vpngroup"
    response = vmanage.apiCall("GET", endpoint)
    return response

def createVpnGroup(vmanage, vpngroup):
    """
    Add VPN group
    
    Parameters:
    vpngroup:	VPN group
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/vpngroup"
    response = vmanage.apiCall("POST", endpoint, vpngroup)
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
    
    endpoint = f"dataservice/admin/vpngroup/{id}"
    response = vmanage.apiCall("PUT", endpoint, vpngroup)
    return response

def deleteVpnGroup(vmanage, id):
    """
    Delete VPN group
    
    Parameters:
    id	 (string):	VPN group Id
    
    Returns
    response    (dict)
    
    
    """
    
    endpoint = f"dataservice/admin/vpngroup/{id}"
    response = vmanage.apiCall("DELETE", endpoint)
    return response


