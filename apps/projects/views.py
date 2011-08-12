from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from projects.models import *
from projects.forms import *
from django.contrib.auth.decorators import login_required
from newsfeed.models import Activity

def version_list(request):
    context = {'versions': Version.objects.all()}
    return render(request, 'projects/version_list.html', context)

def app_list(request):
    context = {'apps': App.objects.all()}
    return render(request, 'projects/app_list.html', context)

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

def add_version(request):
    context = {'form': VersionForm()}
    return render(request, 'projects/add_form.html', context)

def app(request, app_slug):
    context = {}
    return render(request, 'projects/app_list.html', context)

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