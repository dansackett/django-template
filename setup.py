#! /usr/bin/env python
from subprocess import call
import random


def install_reqs():
    call(["pip install -r reqs/dev.txt"])

def make_local_settings():
    call(["cp {{ project_name }}/settings/local.py.example {{ project_name }}/settings/local.py"])
    SECRET_KEY = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
    call(["cat {{ project_name }}/settings/local.py >> 'SECRET_KEY'={}".format(SECRET_KEY)])


if __name__ == "__main__":
    print "\nInstalling Requirements\n"
    install_reqs()
    print "\nUpdating Local Settings\n"
    make_local_settings()
