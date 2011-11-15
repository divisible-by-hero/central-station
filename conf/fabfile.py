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
env.apache_bin_dir = "~/webapps/myproj/apache2/bin"
env.log_location = "~/webapps/logs/user/error_myproj.log"
env.git_repo = "git@github.com:myuser/%s.git" % PROJECT_ID
env.production_branch = "production"

# Utility Methods
def view_log():
    run('sudo cat %s' % env.log_location)

def kick_apache():
    with cd(env.apache_bin_dir):
        run("./restart")

def virtualenv(command):
    with cd(env.directory):
        run(env.activate + '&&' + command)

def install_requirements():
    virtualenv('pip install -r conf/requirements.txt')

def get_code():
    with cd(env.directory):
        run('git pull origin production')
        
def copy_static():
    with cd(env.directory + '/static'):
        run('cp -r * ' + env.static_dir)
        
def sync_db(env):
    if env == "local":
        local("python manage.py syncdb --settings=settings.local")
    else:
        virtualenv('python manage.py syncdb --settings=settings.%s' % env)
    
def migrate(env):
    if env == "local":
        local("python manage.py migrate --settings=settings.local")
    else:
        virtualenv('python manage.py migrate --settings=settings.production')

def build_migration(app):
    local("python manage.py schemamigration %s --auto --settings=settings.local" % app)
        
def quick_fix(msg):
    local("git add .&&git commit -m '%s'&&git checkout production&&git merge develop&&git push origin production develop&&git checkout develop" % msg)
    deploy()

def memory():
    run("ps -u %s -o pid,rss,command" % env.deploy_user)
    
def build_docs():
    local('cd docs && make html')
    



#Local Commands
def run_local():
    local('python manage.py runserver --settings=settings.local')
  
   

def deploy():
    install_requirements()
    pull()
    copy_static()
    sync_db("production")
    migration("production")
    # Either touch or restart of apache.
    local('touch ~/projects/%s/conf/%s.wsgi' % env.id)
    #kick_apache()
    print('Deployment of %s complete' % env.id)

def run_local_server():
    pip_install_req('local')
    build_docs()
    sync_db('local')
    migrate('local')
    run_local()

       
    

    
    
    