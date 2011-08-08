from django.conf.urls.defaults import *
from piston.resource import Resource
from blog.api.handlers.post import PostHandler
from api_manager.utils import CsrfExemptResource

post_handler = CsrfExemptResource(PostHandler)

urlpatterns = patterns('',
    url('^posts/$', post_handler),
    
    

)