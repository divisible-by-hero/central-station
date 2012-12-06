__author__ = 'Derek Stegelman'
__date__ = '10/18/12'

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from projects.models import Project
from projects.forms import ProjectForm
from sprints.models import Sprint

class AddProject(CreateView):
    model = Project
    template_name = 'sprints/forms/edit.html'
    # This needs to be filtered to teh accounts the user owns.
    form_class = ProjectForm

    def get_sprint(self):
        return Sprint.objects.get(pk=self.request.POST.get('sprint'))

    def get_success_url(self):
        print(self.get_sprint())
        return self.get_sprint().get_absolute_url()
