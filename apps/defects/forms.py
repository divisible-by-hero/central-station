#from django import forms
#from django.forms import Textarea
#from bookmarks.models import *
#
#
#class BookmarkForm(forms.ModelForm):
#    class Meta:
#        model = Bookmark

from django import forms
from defects.models import *

class DefectForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(DefectForm, self).__init__(*args, **kwargs)
        self.fields['url'].widget.attrs['class'] = 'text'

    class Meta:
        model = Defect
        exclude = ('creator')
        
        