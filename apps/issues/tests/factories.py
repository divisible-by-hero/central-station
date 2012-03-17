import factory
from issues.models import Issue
from django.contrib.auth.models import User

class UserFactory(factory.Factory):
    FACTORY_FOR = User

    username = "test_user"

class IssueFactory(factory.Factory):
    FACTORY_FOR = Issue