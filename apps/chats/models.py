from django.db import models
from django.contrib.auth.models import User
from nutsbolts.utils.slugs import unique_slugify

class Room(models.Model):
    title = models.CharField(max_length=250)
    password = models.CharField(max_length=250, blank=True, null=True)
    slug = models.SlugField(editable=False)
    
    @models.permalink
    def get_absolute_url(self):
        return ('chats.views.room', (), {'room_slug': self.slug})
    
    def save(self):
        unique_slugify(self, self.title)
        super(Room, self).save()
        
    
class Message(models.Model):
    content = models.TextField()
    author =  models.ForeignKey(User)
    room = models.ForeignKey(Room)