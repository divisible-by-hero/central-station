from django.http import HttpResponse

from sprints.models import Task, Story, StoryStatus

__author__ = 'Derek Stegelman, Garrett Pennington'
__date__ = '10/19/12'

def update_status(request, story_id):
    """
    Change story status via ajax
    """
    
    story_status_id = request.POST.get('value')
    
    story = Story.objects.get(pk=story_id)
    status = StoryStatus.objects.get(pk=story_status_id)

    story.story_status = status
    story.save()

    return HttpResponse(mimetype="text/plain")

def change_task(request, task_id):
    """
    Change task status from complete/un-complete
    """
    
    change = request.POST.get('value')
    
    task = Task.objects.get(pk=task_id)
    if change == "true":
        task.complete = True
    else:
        task.complete = False
    task.save()

    return HttpResponse(mimetype="text/plain")