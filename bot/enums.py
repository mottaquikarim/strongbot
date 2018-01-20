from enum import Enum

class UserStatus(Enum):
    NO_NUMBER = 1
    NEW_USER = 2
    EXISTING_USER = 3

class SupportedCmds(object):
    INFO = ['more', 'm']
    GET_STARTED = ['get started', 'gs']
