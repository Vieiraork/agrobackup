from django_filters import FilterSet, filters
from farm_base.api.v1.filters.fields import NumberInFilter
from farm_base.models import Farm


class FarmFilter(FilterSet):
    ids = NumberInFilter(field_name='id', lookup_expr='in')

    class Meta:
        model = Farm
        fields = ['ids', 'name', 'area', 'owner']

