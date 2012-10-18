from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset

from projects.models import Project

__author__ = 'Derek Stegelman'
__date__ = '9/10/12'

class ProjectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('title'),
        )

        super(ProjectForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Project



