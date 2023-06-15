# Config/urls.py 

# Django and third parties modules
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Locals

urlpatterns = [
    
    # Post
    path('', include('App.Post.urls')),
    path('admin/', admin.site.urls),
]

# This is used for
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
