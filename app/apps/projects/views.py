## Below are some common methods/functions used in my views.
#
#from django.shortcuts import get_object_or_404, redirect
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.simple import direct_to_template
from django.shortcuts import render
## Import your models.
from projects.models import *
from projects.forms import *
## Import tagging stuff if you are using the tagging module. Remove if not.
#from tagging.models import Tag, TaggedItem
## Authentication stuff.  This is a handly decorator used to force a user to login.
from django.contrib.auth.decorators import login_required
#
#'''
#    The following are a few random views that you can use.  
#
#'''
#

def project_view(request):
    return render(request, 'projects/dashboard.html')

def version_list(request):
    
    versions = Version.objects.all()
    
    extra_context = {}
    extra_context['versions'] = versions
    return direct_to_template(request, template="projects/version_list.html", extra_context=extra_context)


def app_list(request):
    
    apps = App.objects.all()
    extra_context = {}
    extra_context['apps'] = apps
    
    return direct_to_template(request, template="projects/app_list.html", extra_context=extra_context)

def add_application(request):
    extra_context = {}
    extra_context['form'] = ApplicationForm()
    
    return direct_to_template(request, template="projects/add_form.html", extra_context=extra_context)

def add_version(request):
    extra_context = {}
    extra_context['form'] = VersionForm()
    return direct_to_template(request, template="projects/add_form.html", extra_context=extra_context)
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