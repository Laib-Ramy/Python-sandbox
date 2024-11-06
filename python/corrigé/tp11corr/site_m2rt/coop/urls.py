from django.urls import include, path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('add-tool/', views.add_tool, name = "add-tool"),
    path('delete-tools/', views.delete_tools, name = "delete-tools"),
]