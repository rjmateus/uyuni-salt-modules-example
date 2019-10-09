
from xmlrpc.client import ServerProxy
import ssl
import sys
import logging

log = logging.getLogger(__name__)

__virtualname__ = 'uyuni_org'

def __virtual__():
    '''
    Only Runs in suse manager server
    '''
    return  'suse_manager_server' in __grains__['role'] and __virtualname__ or False

def present(name,
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

    ret = {'name': name,
           'changes': {},
           'result': None,
           'comment': ''}

    current_state = __salt__['uyuni_org.check_present'](name, first_username, first_password)

    if current_state == 'present':
        ret['result'] = True
        ret['comment'] = '{0} is already installed'.format(name)
        return ret

    if __opts__['test']:
        ret['result'] = None
        ret['comment'] = '{0} would be installed'.format(name)
        ret['changes'] = {
            'old': current_state
        }
        return ret

    __salt__['uyuni_org.present'](name,
                first_username, first_password, user_email,
                prefix, firstName, lastName)

    new_state = __salt__['uyuni_org.check_present'](name, first_username, first_password)

    ret['changes'] = {
        'old': current_state,
        'new': new_state
    }

    if new_state != 'present':
        ret['comment'] = '{0} failed to install'.format(name)
    else:
        ret['result'] = True
        ret['comment'] = '{0} was installed'.format(name)

    return ret
