__author__ = 'Derek Stegelman'
__date__ = '10/19/12'
from django.http import HttpResponse

def change_story(request):
    return HttpResponse(mimetype="text/plain")

def change_task(request, task_id, account, change):
    return HttpResponse(mimetype="text/plain")