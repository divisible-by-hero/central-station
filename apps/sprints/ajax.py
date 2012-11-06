from django.http import HttpResponse

from sprints.models import Task, Story, StoryStatus

__author__ = 'Derek Stegelman'
__date__ = '10/19/12'

def change_story(request, story_id, status_id):
    """
    Change story status via ajax
    """

    story = Story.objects.get(pk=story_id)
    status = StoryStatus.objects.get(pk=status_id)

    story.story_status = status
    story.save()

    return HttpResponse(mimetype="text/plain")

def change_task(request, task_id, change):
    """
    Change task status from complete/un-complete
    """
    task = Task.objects.get(pk=task_id)
    if change == "1":
        task.complete = True
    else:
        task.complete = False
    task.save()

    return HttpResponse(mimetype="text/plain")