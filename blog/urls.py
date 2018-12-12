from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'all_blogs'),
    path('<int:blog_id>/', views.detail, name = 'blog_detail'),
]
