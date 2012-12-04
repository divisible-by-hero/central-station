__author__ = 'Derek Stegelman'
__date__ = '9/6/12'

from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib import messages
from django.utils import simplejson # TODO, use python SL...but I'm on a plane right now

from infuse.auth.permissions import LoginRequiredMixin

from sprints.models import Sprint, Story, Task, StoryStatus, SprintStory
from sprints.forms import StoryForm, TaskForm, StoryTaskForm, SprintForm, NewTaskForm, NewStoryForm
from projects.forms import ProjectForm
from sprints.choices import STORY_STATUS_CHOICES, VALID_STORY_STATUSES

#actions need messages

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

class SprintStoryDetailView(LoginRequiredMixin, ListView):
    template_name = 'sprints/sprint_detail.html'
    context_object_name = 'stories'

    def get_sprint(self):
        return Sprint.objects.get(pk=self.kwargs.get('id'))

    def get_queryset(self):
        return SprintStory.objects.filter(sprint=self.get_sprint())

    def get_account_story_status(self):
        return StoryStatus.objects.filter(account=self.get_sprint().team.organization)

    def get_context_data(self, **kwargs):
        context = super(SprintStoryDetailView, self).get_context_data(**kwargs)
        context['story_statuses'] = self.get_account_story_status()
        context['task_form'] = TaskForm(sprint=self.get_sprint())
        context['story_form'] = StoryForm()
        context['story_task_form'] = StoryTaskForm()
        context['project_form'] = ProjectForm()
        context['sprint'] = self.get_sprint()
        return context




class SprintDetailView(LoginRequiredMixin, DetailView):
    # For an academic exercise, Derek will build the sprint_detail view func
    # into a Class.

    model = Sprint
    template_name = 'sprints/sprint_detail.html'
    context_object_name = 'sprint'
    pk_url_kwarg = 'id'

    def get_account_story_status(self):
        return StoryStatus.objects.filter(account=self.get_object().team.organization)

    def get_context_data(self, **kwargs):
        context = super(SprintDetailView, self).get_context_data(**kwargs)
        context['story_statuses'] = self.get_account_story_status()
        context['task_form'] = TaskForm(sprint=self.object)
        context['story_form'] = StoryForm()
        context['story_task_form'] = StoryTaskForm()
        context['project_form'] = ProjectForm()
        return context

class StoryEditForm(UpdateView):
    model = Story
    template_name = 'sprints/forms/edit.html'
    form_class = StoryForm

    def form_valid(self, form):
        self.object = form.save()
        self.object.update(self.request)
        messages.add_message(self.request, messages.SUCCESS, "%s story updated." % self.object.title)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return self.object.sprint.get_absolute_url() + "#story_%d" % self.object.id

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
    
    def form_valid(self, form):
        self.object = form.save()
        self.object.update(self.request)
        return HttpResponseRedirect(self.get_success_url())

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Task updated.")
        return super(TaskEditForm, self).form_valid(form)

    def get_success_url(self):
        return self.object.story.sprint.get_absolute_url() + "#task_%d" % self.object.id

class SprintEditForm(UpdateView):
    model = Sprint
    template_name = 'sprints/forms/edit.html'
    form_class = SprintForm
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        self.object = form.save()
        self.object.update(self.request)
        messages.add_message(self.request, messages.SUCCESS, "Sprint updated.")
        return HttpResponseRedirect(self.get_success_url())

class AddStory(CreateView):
    model = Story
    template_name = 'sprints/forms/edit.html'
    form_class = NewStoryForm

    def get_success_url(self):
        return self.object.sprint.get_absolute_url() + "#story_%d" % self.object.id

    def form_valid(self, form):
        self.object = form.save()
        self.object.create(self.request)
        messages.add_message(self.request, messages.SUCCESS, "%s story added." % self.object.title)
        return HttpResponseRedirect(self.get_success_url())

class AddTask(CreateView):
    model = Task
    template_name = 'sprints/forms/edit.html'
    form_class = NewTaskForm

    def get_success_url(self):
        return self.object.story.sprint.get_absolute_url() + "#task_%d" % self.object.id

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Task added.")
        return super(AddTask, self).form_valid(form)

    def form_valid(self, form):
        self.object = form.save()
        self.object.create(self.request)
        return HttpResponseRedirect(self.get_success_url())

class AddSprint(CreateView):
    model = Sprint

    def form_valid(self, form):
        self.object = form.save()
        self.object.create(self.request)
        messages.add_message(self.request, messages.SUCCESS, "Sprint created.")
        return HttpResponseRedirect(self.get_success_url())

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
def update_stories(request, account):
    """
    Looks for query parms, updates story and returns JSON
    
    'account' does nothing right now

    """

    _input = request.raw_post_data
    _input = simplejson.loads(request.raw_post_data)

    for story in _input['stories']:
        s = Story.objects.get(id=story['id'])
        s.position = story['position']
        ss = StoryStatus.objects.get(slug=story['status'])  #THIS ADDS SO MANY QUERIES RIGHT NOW
        s.story_status = ss
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