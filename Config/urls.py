# Config/urls.py 

# Django and third parties modules
from django.contrib import admin
from django.urls import path, include

# Locals

urlpatterns = [
    
    # Post
    path('', include('App.Post.urls')),
    path('admin/', admin.site.urls),
]
