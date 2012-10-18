from __future__ import with_statement
from project import *
from fabric.api import *
import os
import glob
import time

env.id = PROJECT_ID
env.user = PROJECT_USER
env.hosts = PROJECT_HOSTS

env.directory = '~/projects/%s' % PROJECT_ID
env.virtual_dir = '~/.virtualenvs'
env.static_dir = '~/static/prod'
env.project_virtual = '~/.virtualenvs/%s' % PROJECT_ID
env.activate = 'source ~/.virtualenvs/%s/bin/activate' % PROJECT_ID
env.deploy_user = PROJECT_USER
env.apache_bin_dir = "~/webapps/django_env/apache2/bin"
env.log_location = "~/webapps/logs/dstegelman/error_django_env.log"
env.git_repo = "git@bitbucket.org:divisiblebyhero/%s.git" % PROJECT_ID
env.production_branch = "production"


from hadrian.conf.fab import *