
from xmlrpc.client import ServerProxy
import ssl
import sys
import logging

log = logging.getLogger(__name__)

__virtualname__ = 'uyuni_org'
client = ServerProxy('http://localhost/rpc/api')

def __virtual__():
    '''
    Only Runs in suse manager server
    '''
    return  return  __virtualname__ if 'suse_manager_server' in __grains__['role'] else False

def check_present(org_name, first_username, first_password):
    # check if username and password are correct
    # user has organization admin role
    # and is part of 'org_name'
    try:
        key = client.auth.login(first_username, first_password)
        if ('org_admin' in client.user.listRoles(key, first_username)
            and org_name == client.user.getDetails(key, first_username)['org_name']):
            return 'present'
    except:
        log.debug('Unable to connect user or org do not exists')
    return 'absent'

def present(org_name,
            first_username,
            first_password,
            user_email,
            prefix = 'Sr.',
            firstName = None,
            lastName = None):
    # Method that creats a organization with the associated user.
    # I'm not sure about this hack, but for proof of concept I think it is ok.
    if firstName is None:
        firstName = first_username

    if lastName is None:
        lastName = first_username

    # Authenticate as admin and create org with admin user
    # In future analyze if it makes sense map the errors returned by the API to other error types.
    # For now, if API returns an error or exception it's propagate
    # I didn't add  support for PamAuth
    key = client.auth.login(__grains__['server_username'], __grains__['server_password'])
    return client.org.create(
        key,
        org_name, first_username, first_password,
        prefix, firstName, lastName, user_email, False)
