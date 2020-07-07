from django.shortcuts import render

# Create your views here.
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView

from app.models import Book
from day13.filter import ComputerFilterSet
from day13.paginationss import MyPageNumberPagination
from day13.serializerss import ComputerModelSerializer


class ComputerListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = ComputerModelSerializer

    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]

    search_fields = ["book_name", "price"]

    ordering = ["price"]

    pagination_class = MyPageNumberPagination
    filter_class = ComputerFilterSet