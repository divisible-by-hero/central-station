from django.shortcuts import render
from django.contrib.auth.models import User


def all_users(request):
    context = {'users': User.objects.all()}

    return render(request, 'profile/user_list.html', context)