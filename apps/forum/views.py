# Create your views here.
## Below are some common methods/functions used in my views.
#
from django.shortcuts import get_object_or_404, redirect, render
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.simple import direct_to_template
## Import your models.
#from homebrew.models import *
from issues.models import *
from issues.forms import *
import datetime
## Import tagging stuff if you are using the tagging module. Remove if not.
#from tagging.models import Tag, TaggedItem
## Authentication stuff.  This is a handly decorator used to force a user to login.
from django.contrib.auth.decorators import login_required
#
#''


def board(request, board_slug):
    
    posts = Post.objects.filter()
    return ''

def view_forum_app(request, app_slug):
    return render(request, 'defects/login.html')