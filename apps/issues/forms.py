from django import forms
from issues.models import *

class IssueForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(IssueForm, self).__init__(*args, **kwargs)
        self.fields['url'].widget.attrs['class'] = 'text'

    class Meta:
        model = Issue
        exclude = ('creator', 'application')
        
        
        
class MilestoneForm(forms.ModelForm):
    class Meta:
        model = Milestone