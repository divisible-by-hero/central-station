from django import forms
from core.models import *
        
class SettingsForm(forms.ModelForm):
    
    class Meta:
        model = Settings
        
        
