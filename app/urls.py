from django.contrib import admin
from django.urls import path, include
from app import views


urlpatterns = [
    path("drf/",views.usernaes.as_view()),
    path("drf/<str:id>/",views.usernaes.as_view()),
    path("drfer/",views.naes.as_view()),
    path("drfer/<str:id>/",views.naes.as_view())
]