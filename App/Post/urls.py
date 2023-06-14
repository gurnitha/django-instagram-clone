# App/Post/urls.py

# Django and third parties modules
from django.urls import path

# Locals
from App.Post.views import index

urlpatterns = [
    path('', index, name='index'),
]
