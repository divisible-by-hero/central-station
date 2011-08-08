from __future__ import with_statement
from fabric.api import local, cd


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
    local("python manage.py syncdb")
    # NEed to add support for settings.lcoal
def migrate():
    local("python manage.py migrate")
    
def run_server():
    local("python manage.py runserver")
    
def deploy_local():
    compress_css()
    #compress_js()
    #sync_db()
    #migrate()
    #run_server()
    

def get_code(env):
    # pull new code
    local("git pull origin %s" % env)
    # push to assets cdn.
    if env == "production":
        local("cd assets && cp -r * ~/static/prod")
    else:
        local("cd assets && cp -r * ~/static/staging")
        


    
def deploy(env):
    get_code(env)
    run_pip()
    sync_db(env)
    auto_migration(env)
    print("Migrations complete for %s" % env)
    restart_apache(env)
    print("Memory Usage")
    memory_usage()
    print("Deployment to %s server complete" % env)

