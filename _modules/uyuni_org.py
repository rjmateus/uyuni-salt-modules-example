
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
    return  'suse_manager_server' in __grains__['role'] and __virtualname__ or False

def check_present(org_name, first_username, first_password):
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

    if firstName is None:
        firstName = first_username

    if lastName is None:
        lastName = first_username

    key = client.auth.login(__grains__['server_username'], __grains__['server_password'])
    return client.org.create(
        key,
        org_name, first_username, first_password,
        prefix, firstName, lastName, user_email, False)
