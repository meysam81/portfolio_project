from django.shortcuts import render
from django.template.response import TemplateResponse
# Create your views here.
def index(request):
    # return render(request, "home_page.html")
    return TemplateResponse(request, 'jobs/home_page.html')
