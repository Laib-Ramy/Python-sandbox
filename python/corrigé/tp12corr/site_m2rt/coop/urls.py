from django.urls import include, path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('add-tool/', views.add_tool, name = "add-tool"),
    path('delete-tools/', views.delete_tools, name = "delete-tools"),
    path('borrow-tools/', views.borrow_tools, name = "borrow-tools"),
    path('restitute-tools/', views.restitute_tools, name = "restitute-tools"),
]