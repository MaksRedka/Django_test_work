from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('submit/', submit),
    path('greeting_list/', show_greetings)
]