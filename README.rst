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
    cdvirtualenv bin
    echo ". ~/projects/{{ project_name }}/bin/postactivate" >> postactivate
    echo ". ~/projects/{{ project_name }}/bin/postdeactivate" >> postdeactivate
    cd -
    setup.py


You're good to go!
