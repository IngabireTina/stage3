import django_filters
from .models import *


class StockFilter(django_filters.FilterSet):
    class Meta:
        model = Stock
        fields = ['code', 'name']
