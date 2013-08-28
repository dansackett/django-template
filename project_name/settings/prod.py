### Production Settings

from .base import *


##############
### Path Stuff
##############


####################
### General Settings
####################


########
### Apps
########


##############
### Middleware
##############


#############
### Databases
#############

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'NAME':     '',
        'USER':     '',
        'PASSWORD': '',
        'HOST':     'localhost',
        'PORT':     '',
    }
}


###########
### Logging
###########


#############
### Templates
#############


##################
### Media / Static
##################

STATIC_ROOT = ''
STATIC_URL = ''


#####################
### Email Information
#####################
