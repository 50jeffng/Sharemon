from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.event_list, name="event_list"),
    path('', views.post_list, name="list"),
    path("<slug>/", views.post_detail, name="detail"),
    path("events/<slug>/", views.event_detail, name="event_detail"),

]
