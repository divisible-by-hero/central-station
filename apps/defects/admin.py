from django.contrib import admin
from defects.models import *

class DefectAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('description', 'type', 'status', 'application')
    
admin.site.register(Defect, DefectAdmin)

