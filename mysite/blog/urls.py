from django.urls import path
from . import views
from blog.views import post_detail

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('',views.post_detail,name='post_detail'),
    
]