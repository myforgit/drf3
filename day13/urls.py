from django.conf.urls import url
from django.urls import path

from day13 import views

urlpatterns = [
    path("computers/", views.ComputerListAPIView.as_view()),
]
