from django.contrib import admin
from issues.models import *

class IssueAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('description', 'type', 'status', 'application')
    
admin.site.register(Issue, IssueAdmin)

