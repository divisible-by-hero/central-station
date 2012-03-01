from django.shortcuts import render
from newsfeed.models import Activity
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def dashboard(request):
    context = {'feed': Activity.objects.all() }
    messages.add_message(request, messages.INFO, 'Hello world.')
    return render(request, 'newsfeed/dashboard.html', context)