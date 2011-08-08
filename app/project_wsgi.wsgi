import os, sys, site


sys.path.append('/webapps/django')
sys.path.append('/webapps/django/htdocs')
site.addsitedir('/.virtualenvs/appname/lib/python2.7/site-packages')


os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.production'


from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
