#! /usr/bin/env python
from subprocess import call
import random


def install_reqs():
    call("pip install -r reqs/dev.txt", shell=True)


def make_local_settings():
    SECRET_KEY = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])

    call("cp {{ project_name }}/settings/local.py.example {{ project_name }}/settings/temp_local.py", shell=True)
    call("echo 'SECRET_KEY'='{}' >> myproject/settings/temp_local.py".format(SECRET_KEY), shell=True)


def update_virtualenv_hooks():
    call("sed 's/PROJECT_NAME/{{ project_name }}/' bin/temp_postactivate > bin/postactivate", shell=True)
    call(". bin/postactivate", shell=True)


def setup_database():
    print "Let's setup the local MySQL Database:"
    local_db_name = raw_input('Local Database Name: ')
    local_db_user = raw_input('Local Database User: ')
    local_db_pwd = raw_input('Local Database Password: ')

    call("sed 's/DATABASE_NAME/{}/' {{ project_name }}/settings/temp_dev.py > {{ project_name }}/settings/dev.py".format(local_db_name), shell=True)
    call("sed 's/DATABASE_USER/{}/' {{ project_name }}/settings/temp_dev.py > {{ project_name }}/settings/dev.py".format(local_db_user), shell=True)
    call("sed 's/DATABASE_USER/{}/' {{ project_name }}/settings/temp_local.py > {{ project_name }}/settings/local.py".format(local_db_pwd), shell=True)
    print "\nLocal DB variables setup\n"

    print "Let's setup the production MySQL Database:"
    prod_db_name = raw_input('Production Database Name: ')
    prod_db_user = raw_input('Production Database User: ')

    call("sed 's/DATABASE_NAME/{}/' {{ project_name }}/settings/temp_prod.py > {{ project_name }}/settings/prod.py".format(prod_db_name), shell=True)
    call("sed 's/DATABASE_USER/{}/' {{ project_name }}/settings/temp_prod.py > {{ project_name }}/settings/prod.py".format(prod_db_user), shell=True)
    print "\nProduction DB variables setup"
    print "NOTE: You will need to update your local.py file on production with the correct password.\n"


def syncdb():
    call("django-admin.py syncdb --migrate", shell=True)


if __name__ == "__main__":
    print "\nInstalling Requirements"
    print "===========================\n"
    install_reqs()
    print "...done!"

    print "\nUpdating Local Settings"
    print "===========================\n"
    make_local_settings()
    print "...done!"

    print "\nUpdating Virtualenv Hook"
    print "===========================\n"
    update_virtualenv_hooks()
    print "...done!"

    print "\nAdding Database Information"
    print "===========================\n"
    setup_database()
    print "...done!"

    print "\nSyncing Database"
    print "===========================\n"
    syncdb()
    print "...done!"
