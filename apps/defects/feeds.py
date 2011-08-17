from django.contrib.syndication.views import Feed
from defects.models import *

class DefectFeed(Feed):
    title = "Brews"
    link = "/brews/"
    description = "This is some brew"
    
    def items(self):
        return Defect.objects.all()[:5]
    
    def item_title(self, item):
        return item.status
    
    def item_description(self, item):
        return item.description   