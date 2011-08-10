from django.conf.urls.defaults import *
from defects.api.handlers.defect import DefectsHandler 
from api_manager.utils import CsrfExemptResource

defects_handler = CsrfExemptResource(DefectsHandler)


urlpatterns = patterns('',
    url(r'^$', defects_handler),

)