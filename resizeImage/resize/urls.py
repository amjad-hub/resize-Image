
from django.contrib import admin
from django.urls import path
from .views import resize_picture

urlpatterns = [
    path('resize_picture/', resize_picture.as_view(),name = 'image')
]
