from __future__ import with_statement
from fabric.api import local, cd
import os, glob

def compress_css():
    #local("cd assets/admin/css && rm -r build")
    #local("cd assets/admin/css && rm -r build")
    
    #local("cd assets/css && rm -r *.min.css")
    #local("cd assets/css && java -jar compressor.jar -o '.css$:.min.css' *.css")
    try:
        local("cd assets/admin/css && rm *.min.css")
    except:
        pass
    local("cd assets && java -jar compressor.jar -o '.css$:.min.css' assets/admin/css/(*.css)")

def compress_js():
    try:
        
        local("cd assets/admin/js && rm *.min.css")
    except:
        pass
    local("cd assets/admin/js && java -jar compressor.jar -o '.js$:.min.js' *.js")
    
def sync_db():
    local("python manage.py syncdb --settings=settings.local")
    # NEed to add support for settings.lcoal
def migrate():
    local("python manage.py migrate --settings=settings.local")
    
def run_server():
    local("python manage.py runserver --settings=settings.local")
    
def run_pip():
    local("pip install -r requirements.txt")
    
def build_migration(app):
    local("python manage.py schemamigration %s --auto --settings=settings.local" % app)


def sass():
    '''
        You need to add more instances of this method and function to each place you have css.
    
    '''
    path = 'media/css'
    for file in glob.glob(os.path.join(path, '*.sass')):
        basename, extension = os.path.splitext(file)
        local("sass %s:%s.min.css --style compressed" % (file, basename))

def run():
    run_pip()
    sync_db()
    migrate()
    run_server()

