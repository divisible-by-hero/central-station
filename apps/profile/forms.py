from django import forms
from profile.models import *

 
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)