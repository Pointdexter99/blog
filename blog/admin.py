from django.contrib import admin
from django.urls import path, include
from .models import Post
# Register your models here.

admin.site.register(Post)