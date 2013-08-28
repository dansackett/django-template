#! /usr/bin/env python
from subprocess import call
import random


def install_reqs():
    call("pip install -r reqs/dev.txt", shell=True)


def make_local_settings():
    SECRET_KEY = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])

    call("cp {{ project_name }}/settings/local.py.example {{ project_name }}/settings/local.py", shell=True)
    call("echo 'SECRET_KEY'='{}' >> myproject/settings/local.py".format(SECRET_KEY), shell=True)


def update_virtualenv_hooks():
    call("sed 's/PROJECT_NAME/{{ project_name }} > bin/postactivate'", shell=True)
    call("cdvirtualenv bin", shell=True)
    call("echo . ~/projects/{{ project_name }}/bin/postactivate >> postactivate'", shell=True)
    call("echo . ~/projects/{{ project_name }}/bin/postdeactivate >> postdeactivate'", shell=True)
    call("cd -", shell=True)
    call(". bin/postactivate", shell=True)


def setup_database():
    print "Let's setup the local MySQL Database:"
    local_db_name = raw_input('Local Database Name: ')
    local_db_user = raw_input('Local Database User: ')
    local_db_pwd = raw_input('Local Database Password: ')

    call("sed 's/DATABASE_NAME/{} > {{ project_name }}/settings/dev.py'".format(local_db_name), shell=True)
    call("sed 's/DATABASE_USER/{} > {{ project_name }}/settings/dev.py'".format(local_db_user), shell=True)
    call("sed 's/DATABASE_USER/{} > {{ project_name }}/settings/local.py'".format(local_db_pwd), shell=True)
    print "Local DB variables setup"

    print "Let's setup the production MySQL Database:"
    prod_db_name = raw_input('Production Database Name: ')
    prod_db_user = raw_input('Production Database User: ')

    call("sed 's/DATABASE_NAME/{} > {{ project_name }}/settings/prod.py'".format(prod_db_name), shell=True)
    call("sed 's/DATABASE_USER/{} > {{ project_name }}/settings/prod.py'".format(prod_db_user), shell=True)
    print "Production DB variables setup"
    print "NOTE: You will need to update your local.py file on production with the correct password."


def syncdb():
    call("django-admin.py syncdb --migrate", shell=True)


if __name__ == "__main__":
    print "\n==========================="
    print "\nInstalling Requirements\n"
    print "\n==========================="
    install_reqs()
    print "\n==========================="
    print "\nRequirements Installed\n"
    print "\n==========================="

    print "\n==========================="
    print "\nUpdating Local Settings\n"
    print "\n==========================="
    make_local_settings()
    print "\n==========================="
    print "\nLocal Settings Installed\n"
    print "\n==========================="

    print "\n==========================="
    print "\nUpdating Postactivate Hook\n"
    print "\n==========================="
    update_virtualenv_hooks()
    print "\n==========================="
    print "\nPostactivate Hook Fixed\n"
    print "\n==========================="

    print "\n==========================="
    print "\nAdding Database Information\n"
    print "\n==========================="
    setup_database()
    print "\n==========================="
    print "\nDatabase Information Saved\n"
    print "\n==========================="

    print "\n==========================="
    print "\nSyncing Database\n"
    print "\n==========================="
    syncdb()
    print "\n==========================="
    print "\nDatabase Synced\n"
    print "\n==========================="
