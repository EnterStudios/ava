Developer's Guide
=================

We are on the look out for testers, Django/Python developers,
documentation folk, graphics wizards, and UX people to help make AVA
awesome. If you have some spare cycles and want to contribute get
stuck in.

Bootstrapping a developer environment
-------------------------------------

At this time, the Docker and Docker Compose configuration for AVA is
geared directly for development rather than production deployment. As
such, please refer to :ref:`install` for detailed instructions on
setting up your development environment.

Django project layout
---------------------

AVA is layed out as a typical Django project::

    ava  (project root)
    ├── ava  (Python package)
    │   ├── core  (Django apps)
    │   ├── core_auth  (...)
    │   ├── core_group
    │   ├── core_identity
    │   ├── core_project
    │   ├── import_google
    │   ├── import_ldap
    │   ├── settings
    │   ├── test
    │   ├── testdata
    │   ├── test_email
    │   ├── test_tracking
    │   ├── test_twitter
    │   └── vis_graph
    ├── bin  (utility scripts and tools)
    ├── docs  (project documentation 
    ├── requirements  (pip requirements)
    ├── static  (static assets)
    │   ├── css
    │   ├── fonts
    │   ├── images
    │   └── js
    └── templates  (Django templates)

Utility scripts
...............

Python development guidelines
-----------------------------

Template development guidelines
-------------------------------

Style development guidelines
----------------------------
