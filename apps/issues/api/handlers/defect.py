from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import *
from defects.models import *
from api_manager.utils import *

class DefectsHandler(BaseHandler):
    allowed_methods = ('GET',)
    model= Defect
    fields = ('description', 'status', 'type')

    @throttle(10, 5)
    def read(self, request):
        return Defect.objects.all()
