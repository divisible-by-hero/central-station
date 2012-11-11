from django.http import HttpResponse
from django.utils import simplejson


from sprints.models import Task, Story, StoryStatus

__author__ = 'Derek Stegelman, Garrett Pennington'
__date__ = '10/19/12'

def update_status(request, story_id):
    """
    Change story status via ajax
    
    JSON Response format:
    {
        'success':true, (or false)
        'message':"Status saved.", (Human readable description of tranaction result)
        'value':'done', (New value of story, even if it was the old value)
        'error':"StoryStatus couldn't be found." (Optional technical explanation of error)
    }
    """

    #Get the story, but it mave have been deleted
    try:
        story = Story.objects.get(pk=story_id)
        current_status = story.story_status
    except Stort.DoesNotExist:
        response = simplejson.dumps({
            'success':False,
            'message':"Status not saved.",
            'value':current_status
        })
        return HttpResponse(response, mimetype='application/json', status=200)

    
    #Get the StoryStatus, but it may have been deleted
    try:
        story_status_id = request.POST.get('value')
        status = StoryStatus.objects.get(pk=story_status_id)
    except StoryStatus.DoesNotExist:
        response = simplejson.dumps({
            'success':False,
            'message':"Status not saved.",
            'value':current_status
        })
        return HttpResponse(response, mimetype='application/json', status=200)
    except Exception, e:
        #TODO use logging
        print e


    #If Story and StoryStatus are found, save story
    story.story_status = status
    story.save()
    response = simplejson.dumps({
        'success':True,
        'message':"Status not saved.",
        'value':status.slug
    })
    return HttpResponse(response, mimetype='application/json', status=200)


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