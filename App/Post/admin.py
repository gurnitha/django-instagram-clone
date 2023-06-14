# App/Post/admin.py

# Django and third parties modules
from django.contrib import admin

# Locals
from App.Post.models import Tag, Post, Follow, Stream

# Register your models here.

admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Follow)
admin.site.register(Stream)