'''
    Author: Derek Stegelman
    Package: Projects App

'''

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from projects.models import *
from projects.forms import *
from django.contrib.auth.models import User
from issues.models import Milestone
from django.contrib.auth.decorators import login_required
from newsfeed.models import Activity

@login_required
def version_list(request):
    context = {'versions': Version.objects.all()}
    return render(request, 'projects/version_list.html', context)

@login_required
def app_list(request):
    context = {'apps': App.objects.all()}
    return render(request, 'projects/app_list.html', context)

@login_required
def add_application(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            app = form.save()
            activity = Activity(application=app)
            activity.action = "Created a new application, %s" % app.name
            activity.user = request.user
            activity.save()
            return redirect("app", app.slug)
    else:
        form = ApplicationForm()
    context = {'form': form}

    return render(request, 'projects/add_form.html', context)

@login_required
def add_version(request):
    context = {'form': VersionForm()}
    return render(request, 'projects/add_form.html', context)

@login_required
def app(request, app_slug):
    context = {'app': get_object_or_404(App, slug=app_slug)}
    context['feed'] = Activity.objects.by_app(app_slug)
    context['milestones'] = Milestone.objects.filter(app__slug=app_slug)
    return render(request, 'projects/app_index.html', context)

'''
    Settings View - Show and enable the change of settings per project
'''
@login_required
def settings(request, app_slug):
    app = get_object_or_404(App, slug=app_slug)
    if request.method == "POST":
        form = ApplicationForm(request.POST, instance=app)
        if form.is_valid():
            new_app = form.save()
            activity = Activity(application=app)
            activity.action = "Updated the settings on %s" % app.name
            activity.user = request.user
            activity.save()
            return redirect('app', app.slug)
    else:
        form = ApplicationForm(instance=app)
    context = {'form':form, 'app':app}
    return render(request, 'projects/project_settings.html', context)

@login_required
def users(request, app_slug):
    context = {}
    app = get_object_or_404(App, slug=app_slug)
    context['users'] = User.objects.all()
    context['app'] = app
    return render(request, "projects/users.html", context)


## View using pagination
#def top_rated(request):
#    extra_context = { }
#    extra_context['top_rated'] = True
#    extra_context['photo_recipes'] = Recipe.objects.published()[:12]
#    recipes = Recipe.objects.order_by("-rating")
#    paginator = Paginator(recipes, 6)
#    page = request.GET.get('page', 1)
#    try:
#        extra_context['recipes'] = paginator.page(page)
#    except PageNotAnInteger:
#        extra_context['recipes'] = paginator.page(1)
#    except EmptyPage:
#        extra_context['recipes'] = paginator.page(paginator.num_pages)
#    return direct_to_template(request, template='cookbook/recipes.html', extra_context=extra_context)
#  
#  
#  # view using login_required and a form.
#@login_required
#def add(request):
#
#    if request.method == "POST":
#        form = RecipeForm(request.POST, request.FILES)
#
#        if form.is_valid():
#            form.save()
#            return redirect("homepage")
#    else:
#        form = RecipeForm()
#        extra_context = { }
#        extra_context['photo_recipes'] = Recipe.objects.published()[:9]
#        extra_context['form'] = form
#
#    return direct_to_template(request, template='cookbook/add.html', extra_context=extra_context)