from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from projects.models import App

def all_users(request):
    context = {'users': User.objects.all()}

    return render(request, 'profile/user_list.html', context)

def settings(request):
    return render(request, 'profile/settings.html')

def app_user_list(request, app_slug):
    context = {'app':get_object_or_404(App, slug=app_slug)}
    
    return render(request, 'profile/project_user_list.html', context)