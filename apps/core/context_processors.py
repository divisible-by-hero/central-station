from core.models import *
from django.contrib.auth.forms import UserCreationForm

def settings(request):
    settings = Settings.objects.get(pk=1)
    context = {}
    context['settings'] = settings
    return context
    
    
def new_user_form(request):
    context = {}
    form = UserCreationForm()
    context['new_user_form'] = form
    return context