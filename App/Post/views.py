# App/Post/views.py

# Django and third parties modules
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Locals
from App.Post.models import Post, Tag, Follow, Stream

app_name = 'Post'


def index(request):

    # loggedin_user is the current user that being logging in
    loggedin_user = request.user # user from the post table
    posts = Stream.objects.filter(user=loggedin_user) # user from the post table

    # posts = Stream.objects.all()

    group_ids = []

    for post in posts:
        group_ids.append(post.post_id)

    post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')

    context = {
        'post_items':post_items
    }
    
    return render(request, 'index.html', context)
