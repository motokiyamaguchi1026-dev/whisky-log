from django.urls import path
from . import views

urlpatterns = [
    path("", views.whisky_list, name="whisky_list"),
    path("create/", views.whisky_create, name="whisky_create"),
    path("<int:pk>/", views.whisky_detail, name="whisky_detail"),
    path("<int:pk>/edit/", views.whisky_update, name="whisky_update"),
]