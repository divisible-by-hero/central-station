from django.shortcuts import render
from newsfeed.models import Activity


def dashboard(request):
    context = {'feed': Activity.objects.all() }
    return render(request, 'newsfeed/dashboard.html', context)