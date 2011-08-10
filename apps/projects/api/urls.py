from django.conf.urls.defaults import *
from projects.api.handlers.app import AppsHandler
from api_manager.utils import CsrfExemptResource

apps_handler = CsrfExemptResource(AppsHandler)
urlpatterns = patterns('',
	url(r'^$', apps_handler),
)