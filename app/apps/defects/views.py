## Below are some common methods/functions used in my views.
#
from django.shortcuts import get_object_or_404, redirect
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.simple import direct_to_template
## Import your models.
#from homebrew.models import *
from defects.models import *
from defects.forms import *
import datetime
## Import tagging stuff if you are using the tagging module. Remove if not.
#from tagging.models import Tag, TaggedItem
## Authentication stuff.  This is a handly decorator used to force a user to login.
from django.contrib.auth.decorators import login_required
#
#'''
#    The following are a few random views that you can use.  
#
#'''

def defect_list(request):
    defects = Defect.objects.all()
    extra_context = {}
    extra_context['defect_count'] = Defect.objects.count()
    extra_context['defects'] = defects
    return direct_to_template(request, template="defects/defect_list.html", extra_context=extra_context)

@login_required
def defect_detail(request, defect_id):
    defect = get_object_or_404(Defect, pk=defect_id)
    extra_context = {}
    extra_context['defect'] = defect
    if request.method == "POST":
        form = DefectForm(request.POST, instance=defect)
        if form.is_valid():
            obj = form.save()
            obj.status = "open"
            obj.last_modified_date = datetime.date.today()
            obj.save()
            return redirect("defect_detail", defect_id=obj.id)
    else:
        form = DefectForm(instance=defect)
        extra_context['form'] = form
        
    return direct_to_template(request, template="defects/defect_detail.html", extra_context=extra_context)

@login_required
def add_defect(request):
    extra_context = {}
    if request.method == "POST":
        form = DefectForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.creator = request.user
            obj.status = "open"
            obj.save()
            return redirect("defect_detail", defect_id=obj.id)
    else:
        form = DefectForm()
    extra_context['form'] = form
    return direct_to_template(request, template="defects/add_defect.html", extra_context=extra_context)


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