from django.urls import path, include
from . import views

urlpatterns = [
    path(r'index', views.index),
]
