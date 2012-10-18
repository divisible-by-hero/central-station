__author__ = 'Derek Stegelman'
__date__ = '10/18/12'

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from projects.models import Project


class AddProject(CreateView):
    model = Project
    success_url = reverse_lazy('homepage')
