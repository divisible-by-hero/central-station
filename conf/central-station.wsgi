import os, sys, site


# Fix markdown.py (and potentially others) using stdout
sys.stdout = sys.stderr

#add virtual env path
site.addsitedir('/home/dstegelman/.virtualenvs/central-station/lib/python2.7/site-packages/')

#Root of Project is up one directory
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, os.path.join(PROJECT_ROOT, "apps"))


from django.conf import settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.production'
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()

