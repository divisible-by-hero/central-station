import factory

from sprints.models import Sprint, Story, Task

__author__ = 'Derek Stegelman'

class SprintFactory(factory.Factory):
    FACTORY_FOR = Sprint

class StoryFactory(factory.Factory):
    FACTORY_FOR = Story

class TaskFactory(factory.Factory):
    FACTORY_FOR = Task


