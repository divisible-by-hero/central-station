from git import *
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from projects.models import App

def repos(request):
    context = {}
    return render(request, 'browser/repo.html', context)


def view_repo(request):
    branch = request.session.get('branch', 'develop')
    repo = Repo(settings.GIT_DIR)
    heads = repo.heads
    assert repo.bare == False
    repo.heads[branch].checkout()
    log = repo.head.log()
    tree = repo.heads[branch].commit.tree
    context = {}
    context['log'] = log
    context['tree'] = tree.blobs
    context['trees'] = tree.trees 
    context['branches'] = repo.heads
    return render(request, 'browser/repo.html', context)

def switch_branch(request, branch):
    request.session['branch'] = branch
    return redirect('view_repo')


def view_dir(request, app_slug, path):
    app = get_object_or_404(App, slug=app_slug)
    repo = Repo(app.git_repo_dir)
    
    branch = request.session.get('branch', 'develop')
    tree = repo.heads[branch].commit.tree
    context = {}
    context['tree'] = tree[path].blobs
    context['trees'] = tree[path].trees
    context['app'] = app
    context['app_slug'] = app.slug
    return render(request, 'browser/repo.html', context)


def view_file(request, file_name):
    file = open(settings.GIT_DIR + "/" + file_name, 'r')
    context = {'file': file}
    context['file_text'] = file.read()
    return render(request, 'browser/file.html', context)

def view_app_repo(request, app_slug):
    app = get_object_or_404(App, slug=app_slug)
    branch = request.session.get('branch', 'develop')
    repo = Repo(app.git_repo_dir)
    heads = repo.heads
    repo.heads[branch].checkout()
    log = repo.head.log()
    tree = repo.heads[branch].commit.tree
    context = {'log':log}
    context['tree'] = tree.blobs
    context['trees'] = tree.trees
    context['branches'] = repo.heads
    context['app'] = app
    context['app_slug'] = app.slug

    return render(request, 'browser/repo.html', context)