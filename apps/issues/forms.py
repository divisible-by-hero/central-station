from django import forms
from issues.models import *
from projects.models import App

class IssueForm(forms.ModelForm):
    
    def __init__(self, app, *args, **kwargs):
        super(IssueForm, self).__init__(*args, **kwargs)
        self.fields['url'].widget.attrs['class'] = 'text'
        self.fields['milestone'].queryset = Milestone.objects.filter(app=app)
        self.fields['assigned_to'].queryset = app.users.all()

    class Meta:
        model = Issue
        exclude = ('creator', 'application')
        
        
        
class MilestoneForm(forms.ModelForm):
    class Meta:
        model = Milestone
        exclude = ('application')
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        exclude = ('author', 'issue')
        
