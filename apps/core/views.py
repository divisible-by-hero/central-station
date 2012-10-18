__author__ = 'Derek Stegelman'
__date__ = '10/17/12'

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from sprints.models import Sprint

@login_required
def homepage(request):
    context = {'sprints': Sprint.objects.all()}
    return render(request, 'base.html', context)