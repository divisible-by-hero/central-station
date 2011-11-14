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

def kick_apache():
    with cd('~/apache2/bin'):
        run("./restart")

def virtualenv(command):
    with cd(env.directory):
        run(env.activate + '&&' + command)

def pip_install_req(env):
    if env == 'local':
        local("pip install -r conf/requirements.txt")
    else:
        virtualenv('pip install -r conf/requirements.txt') 

def get_code():
    with cd(env.directory):
        run('git pull origin production')
        
def copy_static():
    with cd(env.directory + 'assets'):
        run('cp -r * ' + env.static_dir)

def sync_db(env):
    if env == "local":
        local("python manage.py syncdb --settings=settings.local")
    else:
        virtualenv('python manage.py syncdb --settings=settings.production')
    
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
    

def setup():
    local("clear")
    print("Running Setup Script..I think..")
    
    #run("mkdir " + env.directory)
    #with cd(env.virtual_dir):
    #    run('virtualenv %s --no-site-packages' % PROJECT_ID)
    #run("git clone " + env.git_repo + " " + env.directory)
    #with cd(env.directory):
    #    run('git checkout production')
    virtualenv("easy_install http://downloads.sourceforge.net/project/mysql-python/mysql-python-test/1.2.3c1/MySQL-python-1.2.3c1.tar.gz?use_mirror=voxel")
    deploy()

#Local Commands
def run_local():
    local('python manage.py runserver --settings=settings.local')
  
#Utils    
def samuel_l_jackson():
    local('clear')
    print('access main program')
    time.sleep(1)
    print('access main security')
    time.sleep(1)    
    print('access main program grid')
    time.sleep(3)    
    print('')
    print('')
    print('Hold on to yer butts...')
    print('')
    print('')
    
    

def deploy():
    local("clear")
    #samuel_l_jackson()
    pip_install_req()
    get_code()
    #copy_static()
    sync_db("production")
    migrate("production")
    kick_apache()
    print("Deployment completed.")

def run_local_server():
    build_docs()
    pip_install_req('local')
    sync_db('local')
    migrate('local')
    run_local()

       
    

    
    
    