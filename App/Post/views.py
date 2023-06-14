# App/Post/views.py

# Django and third parties modules
from django.shortcuts import render

# Locals

app_name = 'Post'

def index(request):
    return render(request, 'index.html')
