#from django import forms
#from django.forms import Textarea
#from bookmarks.models import *
#
#
#class BookmarkForm(forms.ModelForm):
#    class Meta:
#        model = Bookmark

from django import forms
from projects.models import *

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = App
        
class VersionForm(forms.ModelForm):
    class Meta:
        model = Version