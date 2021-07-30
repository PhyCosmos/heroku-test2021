from django.shortcuts import render
from django.http import HttpResponse
from clipper.tests import get_title
from clipper.models import Site
# Create your views here.
def index(request):
    site_title = get_title()
    
    return HttpResponse(site_title)