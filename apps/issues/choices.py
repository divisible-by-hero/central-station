'''

This file is used for listing choices.   It is a good idea to keep them seperate from your models file to reduce clutter.

'''

STATUS_CHOICES = (
    ('open', 'Open'),
    ('in-progress', 'In Progress'),
    ('closed', 'Closed'),
)

ISSUE_TYPES = (
    ('bug', 'Bug'),
    ('feature', 'Feature'),
    ('to-do', 'To Do'),
)

ISSUE_PRIORITIES = (
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
    ('critical', 'Critical'),
)