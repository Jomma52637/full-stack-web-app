
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.Home, name="recipes-home"),
    path("about/", views.About, name="recipes-about")
]
