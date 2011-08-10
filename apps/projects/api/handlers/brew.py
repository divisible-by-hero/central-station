from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import *
# Import models.
from brew.models import *
from django.http import *
from django.shortcuts import *
from django.db.models import Q


class BrewHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Brew
    fields = ('title', 'url', 'date_begins', 'date_ends', 'human_friendly_time', 'description', 'sponser')

    @throttle(10, 5) #Throttles if they make 10 requests within 5 seconds.  May need to expand/contract as it is seen fit.
    def read(self, request):
        base = Brew.objects.active()
        return base