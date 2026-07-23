from django.urls import path
from . import views

urlpatterns = [
    path("", views.whisky_list, name="whisky_list"),
    path("create/", views.whisky_create, name="whisky_create"),
]