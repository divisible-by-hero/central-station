from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import *
from blog.models import Post
from django.http import *
from django.shortcuts import *
from django.db.models import Q
from api_manager.utils import *


class PostHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Post
    fields= ('title', 'slug', 'content', 'tags')
    
    @throttle(10, 5)
    def read(self, request):
        base = Post.objects.published()
        return base

