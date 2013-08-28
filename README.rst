.. {% comment %}

===============
Django Template
===============

``django_template`` is my personal template for starting a Django 1.5 project. To use, run the following command::

     django-admin.py startproject --template=https://github.com/dansackett/django_template/zipball/master --extension=py,rst,gitignore project_name

-----

.. {% endcomment %}

{{ project_name }}
======================

Quickstart
----------

Follow my instructions for setting up virtualenv and virtualenvwrapper here: https://github.com/dansackett/django_setup#virtualenv-and-virtualenv-wrapper

**Note:** This assumes that you have a MySQL database already set up locally and you know the database name, username, and password.

Do the following once setup::

    mkvirtualenv {{ project_name }}
    cdvirtualenv bin
    echo ". ~/projects/{{ project_name }}/bin/postactivate" >> postactivate
    echo ". ~/projects/{{ project_name }}/bin/postdeactivate" >> postdeactivate
    cd -
    pip install Django==1.5
    setup.py
    . bin/postactivate
    django-admin.py syncdb --migrate

You're good to go! Now you have a great debugging server using: django-admin.py runserver_plus and an environment that you can begin working on right away. Good luck!
