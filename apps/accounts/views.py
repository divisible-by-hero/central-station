from django.shortcuts import render

from accounts.forms import RegistrationForm
from accounts.models import Account

from sprints.models import Sprint

def registration(request):
    form = RegistrationForm()
    context = {'form': form}
    return render(request, "accounts/registration_form.html", context)

def account_home(request, account):
    account = Account.objects.get(slug=account)
    request.session['account_slug'] = account.slug
    sprints = Sprint.objects.current().filter(team__organization=account)
    context = {'account': account, 'sprints': sprints}
    return render(request, 'accounts/account_home.html', context)