from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset

from sprints.models import Story, Roadblock, Sprint


__author__ = 'Derek Stegelman'
__date__ = '9/10/12'

class StoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('title'),
        )
        super(StoryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Story

class RoadBlockForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('title'),
        )

        super(RoadBlockForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Roadblock

class SprintForm(forms.ModelForm):

    def __init__(self):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('name'),
            Field('start_date'),
            Field('end_date'),
            Field('team')
        )

        super(SprintForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Sprint