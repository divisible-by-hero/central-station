from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from issues.models import *
from issues.forms import *
import datetime
from newsfeed.models import Activity
from projects.models import App

def all_issues(request):
    context = {'issues': Issue.objects.open()}
    return render(request, 'issues/issue_list.html', context)

def issue_list(request):
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
    return render(request, 'issues/issue_list.html', context)

def open_app_issues(request, app_slug):
    app = get_object_or_404(App, slug=app_slug)
    context = {'issues': Issue.objects.all().by_app(app_slug), 'app':app}
    return render(request, 'issues/project_list.html', context)



def defect_detail(request, defect_id, app_slug=None):
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
        form = DefectForm(instance=context['defect'])
        context['form'] = form
    return render(request, 'issues/issue_detail.html', context)


def add_defect(request, app_slug):
    context = {}
    app = get_object_or_404(App, slug=app_slug)
    context['app'] = app
    if request.method == "POST":
        form = IssueForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.creator = request.user
            obj.status = "open"
            obj.application = app
            obj.save()

            activity = Activity(application=obj.application)
            activity.user = request.user
            activity.action = "Added a new defect #%s" % obj.id
            activity.issue = obj
            activity.save()

            return redirect("open_app_issues", app_slug=app.slug)
            #return redirect("defect_detail", defect_id=obj.id)
    else:
        form = IssueForm()
    context['form'] = form
    
    return render(request, 'issues/add_defect.html', context)
