from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name="list"),
    path("<slug>/", views.post_detail, name="detail"),
]
