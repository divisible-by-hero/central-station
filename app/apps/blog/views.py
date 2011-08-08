# Below are some common methods/functions used in my views.

from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.simple import direct_to_template
# Import your models.
from blog.models import *
# Import forms
from blog.forms import PostForm
# Import tagging stuff if you are using the tagging module. Remove if not.
from tagging.models import Tag, TaggedItem
# Authentication stuff.  This is a handly decorator used to force a user to login.
from django.contrib.auth.decorators import login_required

'''
    The following are a few random views that you can use.  

'''

def post(request, post_slug):
    context = {'blog_post': get_object_or_404(Post, slug=post_slug)}
    return render(request, 'blog/blog_post.html', context)


def homepage(request):
    blog_posts = Post.objects.published()
    # Set up the paginator with how many objects you want to limit each page to.
    paginator = Paginator(blog_posts, 4)
    # Get the page paramter to decide what page you want.  Default is set to the first page.
    page = request.GET.get('page', 1)
    try:
        context = {'blog_posts': paginator.page(page)}
    except PageNotAnInteger:
        context = {'blog_posts': paginator.page(1)}
    except EmptyPage:
        context = {'blog_posts': paginator.page(paginator.num_pages)}
    '''
     Its important to note that when the view sends the blog_posts objects back you have to extract the actual objects
     using the object_list.  So to loop through blog posts in the template, it would be like this::
     
     {% for post in blog_posts.object_list %}
    
    '''
    return render(request, 'blog/index.html', context)


def tag(request, tag_slug):
    query_tag = Tag.objects.get(slug=tag_slug)
    blog_posts = TaggedItem.objects.get_by_model(Post, query_tag)
    paginator = Paginator(blog_posts, 4)
    page = request.GET.get('page', 1)
    try:
        context = {'blog_posts': paginator.page(page)}
    except PageNotAnInteger:
        context = {'blog_posts': paginator.page(1)}
    except EmptyPage:
        context = {'blog_posts': paginator.page(paginator.num_pages)}
    
    return render(request, 'blog/index.html', context)



def category(request, category_slug):
    blog_posts = Post.objects.published().by_category(category_slug)
    paginator = Paginator(blog_posts, 4)
    page = request.GET.get('page', 1)
    try:
        context = {'blog_posts': paginator.page(page)}
    except PageNotAnInteger:
        context = {'blog_posts': paginator.page(1)}
    except EmptyPage:
        context = {'blog_posts': paginator.page(paginator.num_pages)}
        
    return render(request, 'blog/index.html', context)


  # view using login_required and a form.
@login_required
def add(request):

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect("homepage")
    else:
        form = PostForm()
    context = {'form' : form}
    return render(request, 'blog/add_post.html', context)