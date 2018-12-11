from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Job
# Create your views here.
def index(request):
    jobs = Job.objects
    return TemplateResponse(request, 'jobs/home_page.html', {'jobs': jobs})
