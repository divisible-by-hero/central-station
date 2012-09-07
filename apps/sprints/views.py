__author__ = 'Derek Stegelman'
__date__ = '9/6/12'

from itertools import groupby

from django.views.generic import DetailView, ListView
from django.shortcuts import render, get_object_or_404, redirect

from braces.views import LoginRequiredMixin

from sprints.models import Sprint, Story
from sprints.choices import STORY_STATUS

class SprintListView(LoginRequiredMixin, ListView):
    model = Sprint
    template_name = "sprints/sprint_list.html"
    context_object_name = "sprints"

''' 
class SprintDetailView(LoginRequiredMixin, DetailView):
    model = Sprint
    template_name = 'sprints/sprint_detail.html'
    context_object_name = 'sprint'

'''
def sprint_detail(request, id):
    context = {}
    

    sprint = Sprint.objects.get(id=id)
    context['sprint'] = sprint

    #Stories, all
    stories = sprint.story_set.all()
    context['stories'] = stories


    #Columns, all
    column_list = []    
    for col in STORY_STATUS:
        column = {}
        column['id'] = col[0]
        column['stories'] = []
        column_list.append(column)

    context['columns'] = column_list

    #Stories, sorted by Column
    for key, group in groupby(stories, lambda x: x.status):
        column = {}
        column['id'] = key
        column['stories'] = []        
        for item in group:
            column['stories'].append(item)

        for emtpy_column in column_list:
            if emtpy_column['id'] == column['id']:
                index = column_list.index(emtpy_column)
                column_list[index] = column

    context['sorted_stories'] = column_list

    
    return render(request, 'sprints/sprint_detail.html', context)



class StoryListView(LoginRequiredMixin, ListView):
    template_name = 'sprints/story_list.html'

    def get_queryset(self):
        return Story.objects.all()
