from django import forms
from django.forms import Textarea
from blog.models import *



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        