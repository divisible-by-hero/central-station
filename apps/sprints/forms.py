__author__ = 'Derek Stegelman'
__date__ = '10/17/12'

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

from sprints.models import Story, Sprint, Task

class StoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False

        super(StoryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Story

class SprintForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False

        super(SprintForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Sprint


class TaskForm(forms.ModelForm):
    def __init__