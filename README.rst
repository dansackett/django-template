.. {% comment %}

===============
Django Template
===============

``django_template`` is my personal template for starting a Django project. To use ``django_template`` run the following command::

     django-admin.py startproject --template=https://github.com/dansackett/django_template/zipball/master --extension=py,rst,gitignore, project_name

.. note:: The text following this comment block will become the README.rst of the new project.

-----

.. {% endcomment %}

{{ project_name }}
======================

Quickstart
----------

To bootstrap the project::

    virtualenv {{ project_name }}
    source {{ project_name }}/bin/activate
    cd path/to/{{ project_name }}/repository
    pip install -r requirements.pip
    pip install -e .
    cp {{ project_name }}/settings/local.py.example {{ project_name }}/settings/local.py
    manage.py syncdb --migrate

Documentation
-------------

Developer documentation is available in Sphinx format in the docs directory.

Initial installation instructions (including how to build the documentation as
HTML) can be found in docs/install.rst.
