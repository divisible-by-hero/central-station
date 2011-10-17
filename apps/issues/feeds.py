from django.contrib.syndication.views import Feed
from issues.models import *

class IssueFeed(Feed):
    title = "Brews"
    link = "/brews/"
    description = "This is some brew"
    
    def items(self):
        return Issue.objects.all()[:5]
    
    def item_title(self, item):
        return item.status
    
    def item_description(self, item):
        return item.description   