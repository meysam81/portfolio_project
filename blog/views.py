from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

# Create your views here.
def index(request):
    blogs = Blog.objects
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})
