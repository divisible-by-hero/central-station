from django.shortcuts import render, get_object_or_404
from chats.models import *

def rooms(request):
    context = {}
    context['rooms'] = Room.objects.all()
    return render(request, "chats/rooms.html", context)
    
def room(request, room_slug):
    
    context = {}
    context['room'] = get_object_or_404(Room, slug=room_slug)
    return render(request, "chats/rooms.html", context)
    
