from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import *
from projects.models import *

class AppsHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = App
    fields = ('name', 'slug')

    @throttle(10, 5) #Throttles if they make 10 requests within 5 seconds.  May need to expand/contract as it is seen fit.
    def read(self, request):
        return App.objects.all()
    