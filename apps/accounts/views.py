from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

from accounts.forms import RegistrationForm, UserProfileForm
from accounts.models import Account, RoleAssigned

from sprints.models import Sprint

def registration(request):
    context = {}
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            company = form.cleaned_data['company_name']
            try:
                User.objects.get(username=username)
                # No exception raised? Need to return to the form.
                messages.add_message(request, messages.ERROR, "The username %s is already taken." % username)
                context['form'] = form
                return render(request, 'accounts/registration_form.html', context)
            except User.DoesNotExist:
                # Can Create
                user = User.objects.create_user(username, email=email, password=password)

            company = Account.objects.create(company_name=company)




    context = {'form': form}
    return render(request, "accounts/registration_form.html", context)

def account_home(request, account):
    account = Account.objects.get(slug=account)
    request.session['account_slug'] = account.slug
    sprints = Sprint.objects.current().filter(team__organization=account)
    context = {'sprints': sprints}
    return render(request, 'accounts/account_home.html', context)

def profile(request):
    context = {}
    user = User.objects.get(pk=request.user.id)
    teams = RoleAssigned.objects.filter(user=request.user)

    context['teams'] = teams
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            if form.cleaned_data['change_password']:
                user.set_password(form.cleaned_data['change_password'])
            user.save()
            messages.add_message(request, messages.SUCCESS, "Your profile has been updated.")
    else:
        form_initial = {}
        form_initial['first_name'] = request.user.first_name
        form_initial['last_name'] = request.user.last_name
        form_initial['email'] = request.user.email


        form = UserProfileForm(initial=form_initial)
    context['profile_form'] = form

    return render(request, "accounts/profile.html", context)