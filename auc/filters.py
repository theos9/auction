import django_filters
from .models import AuctionModel,Category
from datetime import datetime, time

class EndOfDayDateFilter(django_filters.DateFilter):
    def filter(self, qs, value):
        if value:
            value = datetime.combine(value, time(23, 59, 59))
        return super().filter(qs, value)
    
class AuctionFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='current_price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='current_price', lookup_expr='lte')
    category = django_filters.CharFilter(method='filter_by_category')
    start_date = django_filters.DateFilter(field_name='start_date', lookup_expr='gte')
    end_date = EndOfDayDateFilter(field_name='end_date', lookup_expr='lte')


    def filter_by_category(self, queryset, name, value):
        try:
            category = Category.objects.get(name=value)
            descendants = category.get_descendants(include_self=True)
            return queryset.filter(category__in=descendants)
        except Category.DoesNotExist:
            return queryset.none()

    class Meta:
        model = AuctionModel
        fields = ['title', 'category', 'min_price', 'max_price','start_date','end_date']