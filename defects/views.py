# Create your views here.
from defects.models import *
from django.views.generic.simple import direct_to_template


def defect_list(request, project_slug):
    
    return direct_to_template(request, template="defects/defect_list.html", extra_context=context)

def defect_detail(request, defect_id):
    
    return direct_to_template(request, template="defects/defect_detail.html", extra_context=context)