
from xmlrpc.client import ServerProxy
import ssl
import sys
import logging

log = logging.getLogger(__name__)

__virtualname__ = 'uyuni_user'
client = ServerProxy('http://localhost/rpc/api')

def __virtual__():
    '''
    Only Runs in suse manager server
    '''
    return  __virtualname__ if 'suse_manager_server' in __grains__['role'] else False

def check_exists(name,
                password,
                org,
                first_name = None,
                last_name = None,
                email = ' ',
                org_admin=False):

    key = None
    try:
        key = client.auth.login(name, password)
        userDetails = client.user.getDetails(key, name)
        #$ check user information
        if(userDetails['first_name'] != first_name
            or userDetails['last_name'] != last_name
            or userDetails['email'] != email
            or userDetails['org_name'] != org):
                return 'absent'

        roles = client.user.listRoles(key, name)
        if((org_admin and 'org_admin' in roles)
            or not org_admin and 'org_admin' not in roles):
            return 'present'
    except:
        log.info('User does not exists')
    finally:
        if(key is not None):
            client.auth.logout(key)
    return 'absent'

def create_or_update(name,
            password,
            org,
            org_admin_username,
            org_admin_password,
            first_name = None,
            last_name = None,
            email=' ',
            org_admin=False):

    if first_name is None:
        firstNfirst_nameame = name

    if last_name is None:
        last_name = name

    key = client.auth.login(org_admin_username, org_admin_password)
    # check if user exists
    ## if not:  create it
    ## if exists, check password. Update user getDetails
    # add / remove admin role
    listUsers= client.user.listUsers(key)
    if(name in (u['login'] for u in listUsers)):
        #if we where able to login then user and password are ok
        client.user.setDetails(key, name, {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password
        })
    else:
        client.user.create(key, name, password, first_name, last_name, email)

    if(org_admin):
        client.user.addRole(key, name, "org_admin")
    else:
        client.user.removeRole(key, name, "org_admin")

    user_details = client.user.getDetails(key, name)
    client.auth.logout(key)
    return user_details
