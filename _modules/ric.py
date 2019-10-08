# this is just a test file to check how modules work.
# nothing usefull...
import logging

log = logging.getLogger(__name__)

__virtualname__ = 'ric'


def __virtual__():
    '''
    Only Runs in suse manager server
    '''
    return __virtualname__

def theMan(name):
    log.info("the man is" + name)
    return "the man is {}..".format(name)
