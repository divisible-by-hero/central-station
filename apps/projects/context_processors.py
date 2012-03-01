from projects.models import *

def apps(request):
    context = {}
    context['apps'] = App.objects.all()
    return context