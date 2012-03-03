from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from projects.models import App
from profile.forms import *

def all_users(request):
    context = {'users': User.objects.all()}

    return render(request, 'profile/user_list.html', context)

def settings(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            obj = form.save()
    else:
        form = ProfileForm(instance=user_profile)
    context = {'form':form}
    return render(request, 'profile/settings.html', context)

def app_user_list(request, app_slug):
    context = {'app':get_object_or_404(App, slug=app_slug)}
    
    return render(request, 'profile/project_user_list.html', context)
    
    