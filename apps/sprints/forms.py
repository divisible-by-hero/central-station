from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset

from sprints.models import Story, Roadblock, Sprint, Task


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

# These are scumbag violations of DRY.  Doing this to patch
# the app until a better solution is found.
# Love, Derek
class NewStoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Field('title'),
        )

        super(NewStoryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Story
        exclude = ('deleted', 'deleted_date', 'position')


class NewTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()
        self.helper.form_tag = False

        super(NewTaskForm, self).__init__(*args, **kwargs)


    class Meta:
        model = Task
        exclude = ('deleted', 'deleted_date')

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

class StoryTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()
        self.helper.form_tag = False

        super(StoryTaskForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Task
        exclude = ('deleted', 'deleted_date', 'story')

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

