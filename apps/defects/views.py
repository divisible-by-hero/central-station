from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from defects.models import *
from defects.forms import *
import datetime
from django.contrib.auth.decorators import login_required

def defect_list(request):
    context = {'defect_count': Defect.objects.count()}
    context['defects'] = Defect.objects.all()
    paginator = Paginator(context['defects'], 40)
    page = request.GET.get('page', 1)
    try:
        context['defects'] = paginator.page(page)
    except PageNotAnInteger:
        context['defects'] = paginator.page(1)
    except EmptyPage:
        context['defects'] = paginator.page(paginator.num_pages)
    return render(request, 'defects/defect_list.html', context)

@login_required
def defect_detail(request, defect_id):
    context = {'defect': get_object_or_404(Defect, pk=defect_id)}

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
        context['form'] = form
    return render(request, 'defects/defect_detail.html', context)

@login_required
def add_defect(request):
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
    context = {'form': form }
    return render(request, 'defects/add_defect.html', context)


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