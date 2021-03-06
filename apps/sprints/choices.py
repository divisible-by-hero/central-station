__author__ = 'Derek Stegelman, Garrett Pennington'
__date__ = '9/6/12'
from django.conf import settings


STORY_STATUS_CHOICES = (
    ('not-started', "Not Started"),
    ('in-progress', "In Progress"),
    ('testing', "Testing"),
    ('done', "Done"),
    ('road-blocked', "Road Blocked"),
)

STORY_POINT_CHOICES = (
    (settings.CS_SMALL_POINT_VALUE, 'Small'),
    (settings.CS_MEDIUM_POINT_VALUE, 'Medium'),
    (settings.CS_HARD_POINT_VALUE, 'Hard'),
)

VALID_STORY_STATUSES = []
for choice in STORY_STATUS_CHOICES:
    VALID_STORY_STATUSES.append(choice[0])

STATUS_COLORS = {
    'grey': {
        'name':'Grey',
        'style_class':'',
        'hex':'cccccc'
    },
    'blue': {
        'name':'Blue',
        'style_class':'primary',
        'hex':'0000ff'
    },
    'light_blue': {
        'name':'Light Blue',
        'style_class':'info',
        'hex':'ccccff'
    },
    'green': {
        'name':'Green',
        'style_class':'success',
        'hex':'00ff00'
    },
    'yellow': {
        'name':'Yellow',
        'style_class':'warning',
        'hex':'00ffff'
    },
    'red': {
        'name':'Red',
        'style_class':'danger',
        'hex':'ff0000'
    }
}

def color_choices():
    choices = []
    colors = STATUS_COLORS.keys()
    for color in colors:
        color_info = STATUS_COLORS[color]
        choice = (color, color_info['name'])
        choices.append(choice)
    
    return choices
