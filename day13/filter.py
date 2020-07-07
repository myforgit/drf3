from django_filters.rest_framework import FilterSet

from app.models import Book


class ComputerFilterSet(FilterSet):
    from django_filters import filters
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = Book
        fields = ["brand", "min_price", "max_price"]