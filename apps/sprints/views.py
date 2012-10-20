__author__ = 'Derek Stegelman'
__date__ = '9/6/12'

from itertools import groupby

from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.utils import simplejson # TODO, use python SL...but I'm on a plane right now

from braces.views import LoginRequiredMixin

from sprints.models import Sprint, Story, Task
from sprints.forms import StoryForm, TaskForm, SprintForm
from projects.forms import ProjectForm
from sprints.choices import STORY_STATUS_CHOICES, VALID_STORY_STATUSES

class Backlog(LoginRequiredMixin, ListView):
    queryset = Story.objects.filter(sprint__isnull=True)
    template_name = 'sprints/backlog.html'
    context_object_name = 'stories'

    def get_context_data(self, **kwargs):
        context = super(Backlog, self).get_context_data(**kwargs)
        context['story_form'] = StoryForm()
        context['project_form'] = ProjectForm()
        return context

class SprintListView(LoginRequiredMixin, ListView):
    model = Sprint
    template_name = "sprints/sprint_list.html"
    context_object_name = "sprints"


class SprintDetailView(LoginRequiredMixin, DetailView):
    # For an academic exercise, Derek will build the sprint_detail view func
    # into a Class.

    model = Sprint
    template_name = 'sprints/sprint_detail_table.html'
    context_object_name = 'sprint'
    stories = None
    pk_url_kwarg = 'id'

    def sort_out_columns(self):
        self.stories = self.get_object().story_set.all()
        column_list = []
        for col in STORY_STATUS_CHOICES:
            column = {}
            column['id'] = col[0]
            column['stories'] = []
            column_list.append(column)
            #Stories, sorted by Column
        for key, group in groupby(self.stories, lambda x: x.status):
            column = {}
            column['id'] = key
            column['stories'] = []
            for item in group:
                column['stories'].append(item)

            for emtpy_column in column_list:
                if emtpy_column['id'] == column['id']:
                    index = column_list.index(emtpy_column)
                    column_list[index] = column
        return column_list

    def get_context_data(self, **kwargs):
        context = super(SprintDetailView, self).get_context_data(**kwargs)
        context['stories'] = self.stories
        context['columns'] = STORY_STATUS_CHOICES
        context['sorted_stories'] = self.sort_out_columns()
        context['task_form'] = TaskForm(sprint=self.object)
        context['story_form'] = StoryForm()
        context['project_form'] = ProjectForm()
        return context

class StoryEditForm(UpdateView):
    model = Story
    template_name = 'sprints/forms/edit.html'
    form_class = StoryForm

    def form_valid(self, form):
        self.object = form.save()
        self.object.update(self.request)
        return HttpResponseRedirect(self.get_success_url())


class TaskEditForm(UpdateView):
    model = Task
    template_name = 'sprints/forms/edit.html'
    form_class = TaskForm

    def get_form_kwargs(self):
        kwargs = super(TaskEditForm, self).get_form_kwargs()
        kwargs.update(
            {'sprint': self.object.story.sprint}
        )
        return kwargs

class SprintEditForm(UpdateView):
    model = Sprint
    template_name = 'sprints/forms/edit.html'
    form_class = SprintForm
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        self.object = form.save()
        self.object.update(self.request)
        return HttpResponseRedirect(self.get_success_url())

class AddStory(CreateView):
    model = Story

    def get_success_url(self):
        return self.object.sprint.get_absolute_url()

    def form_valid(self, form):
        self.object = form.save()
        self.object.create(self.request)
        return HttpResponseRedirect(self.get_success_url())

class AddTask(CreateView):
    model = Task

    def get_success_url(self):
        return self.object.story.sprint.get_absolute_url()

class AddSprint(CreateView):
    model = Sprint

    def form_valid(self, form):
        self.object = form.save()
        self.object.create(self.request)
        return HttpResponseRedirect(self.get_success_url())


def sprint_detail(request, id):
    context = {}


    sprint = get_object_or_404(Sprint, pk=id)
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

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def update_stories(request):
    """
    Looks for query parms, updates story and returns JSON

    """

    _input = request.raw_post_data
    _input = simplejson.loads(request.raw_post_data)
    #print _input


    for story in _input['stories']:
        print story
        s = Story.objects.get(id=story['id'])
        s.position = story['position']
        s.status = story['status']
        s.save()

    json_response = simplejson.dumps({'success':True})
    return HttpResponse(json_response, mimetype='application/json', status=200)

    '''
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
    '''