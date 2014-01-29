## Central Station

Central Station is a project management platform built with software development in mind.  It aims to provide
a centralized place for project management functions, issues, milestones and releases.  The goal is to use
Central Station as tool to facilitate Agile Methodology but it should be flexible enough to allow the customization
of any given workflow.

Central Station is a work in progress.


### Apps

Central station is broken up into a series of applications that provide it's overall functionality.

* Issues
* Projects
* Accounts
* Sprints

In Addition to these ``apps`` Central Station has a core module which provides a wrapper for 
common and distributed functionality.

### Getting started with Development

Central station includes a vagrant file and salt provisioning states to get you started right away.  In
order to get started you'll need to download vagrant and virtualbox.  Then simply run::

    vagrant up

from this repo.

This will set you up with a virtual machine that you can ssh into and begin to setup requirments, etc.

There are a few shortcuts to getting this started.

Once you have the VM built:

    vagrant ssh
    activate
    pip install -r conf/requirements.txt
    python manage.py syncdb --settings=settings.local
    python manage.py migrate --settings=settings.local
    run


Both activate, and run are bash alias's that you can find in the salt config.  salt/roots/salt/users/bashrc.  Activate
will activate the internal python virtualenv and run will run the django runserver_plus.  Port 8081 is forwarded
to 9091, so after running the django dev server on the vm you can view it on your host machine at localhost:9091.