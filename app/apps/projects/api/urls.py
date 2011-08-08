from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers.brew import BrewHandler
# You must use the CsrfExempt resource class becuase POSTING will fail otherwise.
from api.utils import CsrfExemptResource

brew_handler = CsrfExemptResource(BrewHandler)
urlpatterns = patterns('',
	url(r'^$', brew_handler),
	# OTher stuff can be added here..
)