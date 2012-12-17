from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset

from sprints.models import Story, Roadblock, Sprint, Task

from chosen.widgets import ChosenSelect

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
        exclude = ('deleted', 'deleted_date', 'position', 'sprint')
        widgets = {
            'project': ChosenSelect(overlay="Project")
        }

# These are scumbag violations of DRY.  Doing this to patch
# the app until a better solution is found.
# Love, Derek
class NewStoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Field('title'),
            Field('status')
        )

        super(NewStoryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Story
        exclude = ('deleted', 'deleted_date', 'position', 'status')
        widgets = {
            'project': ChosenSelect(overlay="Project")
        }


class NewTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()
        self.helper.form_tag = False

        super(NewTaskForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Task
        exclude = ('deleted', 'deleted_date')
        widgets = {
            'story': ChosenSelect(overlay='Choose a story'),
            'assigned': ChosenSelect(overlay='Choose')
        }

class TaskForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        sprint = kwargs.pop('sprint')
        self.helper = FormHelper()
        self.helper.form_tag = False
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['story'].queryset = Story.objects.filter(sprint=sprint)

    class Meta:
        model = Task
        exclude = ('deleted', 'deleted_date')
        widgets = {
            'story': ChosenSelect(overlay='Choose a Story'),
            'assigned': ChosenSelect(overlay='Choose an assignee')
        }

class StoryTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        super(StoryTaskForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Task
        exclude = ('deleted', 'deleted_date', 'story', 'complete')


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

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('name', css_class='span12'),
            Field('start_date', css_class='datepicker'),
            Field('end_date', css_class='datepicker'),
            Field('team')
        )

        super(SprintForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Sprint
        exclude = ('deleted', 'deleted_date', 'locked')

