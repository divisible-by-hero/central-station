__author__ = 'Derek Stegelman'
__date__ = '9/6/12'

from django.views.generic import DetailView, ListView

from braces.views import LoginRequiredMixin

from sprints.models import Sprint, Story

class SprintListView(LoginRequiredMixin, ListView):
    model = Sprint
    template_name = "sprints/sprint_list.html"
    context_object_name = "sprints"

class SprintDetailView(LoginRequiredMixin, DetailView):
    model = Sprint
    



class StoryListView(LoginRequiredMixin, ListView):
    template_name = 'sprints/story_list.html'

    def get_queryset(self):
        return Story.objects.all()
