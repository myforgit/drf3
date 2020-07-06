from sys import path

from django.conf.urls import url
from rest_framework_jwt.views import ObtainJSONWebToken

from day12 import views

urlpatterns = [
    url(r"User/", ObtainJSONWebToken.as_view()),
    path("login/", views.Login.as_view()),
]
