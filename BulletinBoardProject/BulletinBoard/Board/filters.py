from django_filters import FilterSet, filters
from .models import Notification


class ProductFilter(FilterSet):
    class Meta:
        model = Notification
        fields = {
            'title': ['icontains'],
            # 'text': ['icontains'],
        }
