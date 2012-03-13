from django.contrib.syndication.views import Feed
from projects.models import *

class AppFeed(Feed):
    title = "Brews"
    link = "/brews/"
    description = "This is some brew"
    
    def items(self):
        return App.objects.all()[:5]
    
    def item_title(self, item):
        return item.name
    
    def item_description(self, item):
        return item.name
    