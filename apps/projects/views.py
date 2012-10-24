__author__ = 'Derek Stegelman'
__date__ = '10/18/12'

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from projects.models import Project
from projects.forms import ProjectForm

class AddProject(CreateView):
    model = Project
    success_url = reverse_lazy('homepage')
    template_name = 'sprints/forms/edit.html'
    # This needs to be filtered to teh accounts the user owns.
    form_class = ProjectForm
