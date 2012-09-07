__author__ = 'Derek Stegelman'
__date__ = '9/6/12'

from itertools import groupby

from django.views.generic import DetailView, ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import simplejson # TODO, use python SL...but I'm on a plane right now

from braces.views import LoginRequiredMixin

from sprints.models import Sprint, Story
from sprints.choices import STORY_STATUS_CHOICES, VALID_STORY_STATUSES

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
    for col in STORY_STATUS_CHOICES:
        column = {}
        column['id'] = col[0]
        column['stories'] = []
        column_list.append(column)

    context['columns'] = STORY_STATUS_CHOICES

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
        


#Ajax Views

def update_story_status(request):
    """
    Looks for query parms, updates story and returns JSON

    """
    #Build reponse object conditions mature
    response = {'success':False}

    #Authed?
    if request.user.is_authenticated():
        pass
    else:
        response['expired'] = True
        response['message'] = "The current session has expired"
        json = simplejson.dumps(response)
        return HttpResponse(json, mimetype='text/json', status=200)   

    #Correct params?
    id = request.REQUEST['story_id']
    status = request.REQUEST['story_status']
        
    if id and status and status in VALID_STORY_STATUSES:
        try:
            story = Story.objects.get(id=id)
            story.status = status
            story.save()

            response['success'] = True        
            response['message'] = "Story: %s has been updated to status: %s" % (id,status)
            response['story_id'] = id
            json = simplejson.dumps(response)
            return HttpResponse(json, mimetype='application/json', status=200)
        except:
            response['success'] = False        
            response['message'] = "Story %s has been NOT updated" % id
            response['story_id'] = id
            json = simplejson.dumps(response)
            return HttpResponse(json, mimetype='application/json', status=200)

    else:
        response['success'] = False        
        response['message'] = "Invalid or missing parameters"
        json = simplejson.dumps(response)
        return HttpResponse(json, mimetype='application/json', status=400)
        
