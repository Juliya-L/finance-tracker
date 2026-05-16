import django_filters
from .models import Transaction

class TransactionFilter(django_filters.FilterSet):
    date_from = django_filters.DateFilter(filter_name='date', lookup_expr='gte')
    date_to = django_filters.DateFilter(field_name='data', lookup_expr='lte')

    month = django_filters.NumberFilter(field_name='date', lookup_expr='month')
    year = django_filters.NumberFilter(field_name='date', lookup_expr='year')

    class Meta:
        model = Transaction
        fields = ['type', 'category', 'date_from', 'date_to', 'month', 'year']