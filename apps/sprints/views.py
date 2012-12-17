__author__ = 'Derek Stegelman'
__date__ = '9/6/12'

from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib import messages
from django.utils import simplejson # TODO, use python SL...but I'm on a plane right now

from infuse.auth.permissions import LoginRequiredMixin

from accounts.models import Account
from sprints.models import Sprint, Story, Task, Status, SprintStory
from sprints.forms import StoryForm, TaskForm, StoryTaskForm, SprintForm, NewTaskForm, NewStoryForm
from projects.forms import ProjectForm
from sprints.choices import STORY_STATUS_CHOICES, VALID_STORY_STATUSES

#actions need messages
class MoveToNewSprint(CreateView):
    """ Take a given sprint, and move
    all non terminal stories to the next sprint.
    """
    model = Sprint
    template_name = 'sprints/forms/edit.html'
    form_class = SprintForm

    def form_valid(self, form):
        previous_sprint_id = self.kwargs.get('id')
        self.object = form.save()
        self.object.create(self.request)
        messages.add_message(self.request, messages.SUCCESS, "Sprint created.  Stories from previous sprint moved over.")
        sprint = Sprint.objects.get(pk=previous_sprint_id)
        sprint.complete(moved=True, sprint=self.object)
        return HttpResponseRedirect(self.get_success_url())

def move_to_backlog(request, id, account):
    """ Take a given sprint, and move
    all non terminal stories to the backlog.
    """
    sprint = Sprint.objects.get(pk=id)
    sprint.complete(moved=False)
    messages.add_message(request, messages.SUCCESS, 'Incomplete stories moved to backlog.')
    return redirect('account_home', account=account)


class Backlog(LoginRequiredMixin, ListView):
    queryset = Story.objects.filter(backlog=True)
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
    context_object_name = 'sprint_stories'

    def get_sprint(self):
        return Sprint.objects.get(pk=self.kwargs.get('id'))

    def get_account(self):
        return Account.objects.get(slug=self.kwargs.get('account'))

    def get_queryset(self):
        return SprintStory.objects.filter(sprint=self.get_sprint())

    def get_account_status(self):
        return Status.objects.filter(account=self.get_sprint().team.organization)

    def get_context_data(self, **kwargs):
        sprint = self.get_sprint()
        context = super(SprintStoryDetailView, self).get_context_data(**kwargs)
        context['statuses'] = self.get_account_status()
        context['task_form'] = TaskForm(sprint=sprint)
        context['story_form'] = StoryForm()
        context['story_task_form'] = StoryTaskForm()
        context['project_form'] = ProjectForm()
        context['sprint'] = sprint
        context['account'] = self.get_account()
        context['total_points'] = sprint.total_points
        context['completed_points'] = sprint.completed_points
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
        # Add sprint object to SprintStory object.
        self.object.add_to_sprint(self.object.sprint)
        messages.add_message(self.request, messages.SUCCESS, "%s story added." % self.object.title)
        return HttpResponseRedirect(self.get_success_url())

class AddTask(CreateView):
    model = Task
    template_name = 'sprints/forms/edit.html'
    form_class = NewTaskForm

    def get_success_url(self):
        return self.get_sprint().get_absolute_url() + "#task_%d" % self.object.id

    def get_sprint(self):
        return Sprint.objects.get(id=self.request.POST.get('sprint'))

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

def update_status(request):
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
    status = request.REQUEST['status']

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
        ss = Status.objects.get(slug=story['status'])  #THIS ADDS SO MANY QUERIES RIGHT NOW
        s.status = ss
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
    status = request.REQUEST['status']

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