# this is just a test file to check how modules work and have a litle fun...
# nothing usefull...
import logging

log = logging.getLogger(__name__)

__virtualname__ = 'who_is'


def __virtual__():
    return __virtualname__

def theMan(name):
    log.info("the man is" + name)
    return "the man is {}..".format(name)
