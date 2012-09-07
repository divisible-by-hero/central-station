__author__ = 'Derek Stegelman'
__date__ = '9/6/12'


STORY_STATUS_CHOICES = (
    ('not-started', "Not Started"),
    ('in-progress', "In Progress"),
    ('testing', "Testing"),
    ('done', "Done"),
)

VALID_STORY_STATUSES = []
for choice in STORY_STATUS_CHOICES:
    VALID_STORY_STATUSES.append(choice[0])