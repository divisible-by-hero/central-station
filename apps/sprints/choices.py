__author__ = 'Derek Stegelman'
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
