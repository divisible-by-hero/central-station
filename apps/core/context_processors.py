from core.models import *


def settings(request):
    settings = Settings.objects.get(pk=1)
    context = {}
    context['settings'] = settings
    return context
    