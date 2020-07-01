from django.contrib import admin
from django.urls import path, include
from drf4 import views

#登录，注册的url
urlpatterns = [
    path("drfe/",views.twousernaes.as_view({"put":"logint"})),
    path("drfe/<str:id>/",views.twousernaes.as_view({"put":"logint"}))
]