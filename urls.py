# food_recognition/urls.py

from django.urls import path
from . import views
from asgiref.sync import async_to_sync

urlpatterns = [
    path('', views.index, name='index'),
    path('process_image/', async_to_sync(views.process_image), name='process_image'),
]
