.. {% comment %}

===============
Django Template
===============

``django_template`` is my personal template for starting a Django project. To use ``django_template`` run the following command::

     django-admin.py startproject --template=https://github.com/dansackett/django_template/zipball/master --extension=py,rst,gitignore project_name

.. note:: The text following this comment block will become the README.rst of the new project.

-----

.. {% endcomment %}

{{ project_name }}
======================

Quickstart
----------

Follow my instructions for setting up virtualenv and virtualenvwrapper here: https://github.com/dansackett/django_setup#virtualenv-and-virtualenv-wrapper

Do the following once setup::

    mkvirtualenv {{ project_name }}
    pip install -r reqs/dev.txt
    cp {{ project_name }}/settings/local.py.example {{ project_name
    }}/settings/local.py

- Edit the {{ project_name }}/settings/dev.py and {{ project_name }}/settings/prod.py files to reflect the database.
- Edit {{ project_name }}/settings/local.py and add the appropriate passwords.
- Edit {{ project_name }}/settings/local.py.example and remove the secret_key text.

Next::

    django-admin.py syncdb --migrate


You're good to go!
