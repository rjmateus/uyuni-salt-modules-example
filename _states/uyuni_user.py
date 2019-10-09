
from xmlrpc.client import ServerProxy
import ssl
import sys
import logging

log = logging.getLogger(__name__)

__virtualname__ = 'uyuni_user'

def __virtual__():
    '''
    Only Runs in suse manager server
    '''
    return  'suse_manager_server' in __grains__['role'] and __virtualname__ or False

def present(name,
            password,
            org,
            org_admin_username,
            org_admin_password,
            first_name = None,
            last_name = None,
            email=' ',
            org_admin=False):

    if first_name is None:
        first_name = name

    if last_name is None:
        last_name = name

    ret = {'name': name,
           'changes': {},
           'result': None,
           'comment': ''}

    current_state = __salt__['uyuni_user.check_present'](name,
                    password,
                    org,
                    first_name,
                    last_name,
                    email,
                    org_admin)

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

    __salt__['uyuni_user.present'](name,
                password,
                org,
                org_admin_username,
                org_admin_password,
                first_name,
                last_name,
                email,
                org_admin)

    new_state = __salt__['uyuni_user.check_present'](name,
                    password,
                    org,
                    first_name,
                    last_name,
                    email,
                    org_admin)

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
