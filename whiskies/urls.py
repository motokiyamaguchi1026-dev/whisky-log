from django.urls import path
from . import views

urlpatterns = [
    path('', views.whisky_list, name='whisky_list'),
]