from django import forms
from projects.models import *

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = App
        exclude = ('users',)
        
class VersionForm(forms.ModelForm):
    class Meta:
        model = Version