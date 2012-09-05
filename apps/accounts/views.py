from django.shortcuts import render
from accounts.forms import RegistrationForm


def registration(request):
    form = RegistrationForm()
    context = {'form': form}
    return render(request, "accounts/registration_form.html", context)