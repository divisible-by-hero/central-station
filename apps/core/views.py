__author__ = 'Derek Stegelman'
__date__ = '10/17/12'

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from sprints.models import Sprint
from accounts.models import RoleAssigned

@login_required
def homepage(request):
    context = {'sprints': Sprint.objects.all()}
    teams = RoleAssigned.objects.filter(user=request.user)
    context['teams'] = teams
    return render(request, 'core/homepage.html', context)