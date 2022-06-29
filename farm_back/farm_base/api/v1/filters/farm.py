from django_filters import FilterSet, filters
from farm_base.api.v1.filters.fields import NumberInFilter, CharFilter
from farm_base.models import Farm


class FarmFilter(FilterSet):
    id = NumberInFilter(field_name='id')
    name = CharFilter(field_name='name')
    owner_id = CharFilter(field_name='owner__id')
    municipality = CharFilter(field_name='municipality')
    state = CharFilter(field_name='state')

    class Meta:
        model = Farm
        fields = ['id', 'name', 'owner_id', 'municipality', 'state']

