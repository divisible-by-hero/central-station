from django.shortcuts import render
from newsfeed.models import Activity
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    context = {'feed': Activity.objects.all() }
    return render(request, 'newsfeed/dashboard.html', context)