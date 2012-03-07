from django.shortcuts import render, redirect
from core.models import *
from core.forms import *
from django.contrib import messages

def change_settings(request):
    context = {}
    settings = Settings.objects.get(pk=1)
    if request.method == "POST":
        form = SettingsForm(request.POST, instance=settings)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Settings Saved")
            return redirect("core.views.change_settings")
    else:
        form = SettingsForm(instance=settings)
    context['form'] = form
    return render(request, "core/settings.html", context)
    
    