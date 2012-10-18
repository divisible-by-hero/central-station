__author__ = 'Derek Stegelman'
__date__ = '10/17/12'

from django.shortcuts import render

from sprints.models import Sprint

def homepage(request):
    context = {'sprints': Sprint.objects.all()}
    return render(request, 'base.html', context)