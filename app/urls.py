from django.contrib import admin
from django.urls import path, include
from app import views


urlpatterns = [
    path("drf/",views.usernaes.as_view()),
    path("drf/<str:id>/",views.usernaes.as_view())
]