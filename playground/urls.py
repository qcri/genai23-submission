from django.urls import path
from . import views

urlpatterns=[
    path("", views.say_playgroundpage),
    path("hello/", views.say_hello)
]