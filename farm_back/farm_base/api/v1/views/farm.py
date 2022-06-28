from requests import Response
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from farm_base.api.v1.filters.farm import FarmFilter

from farm_base.api.v1.serializers import FarmListSerializer, \
    FarmCreateSerializer, FarmDetailSerializer
from farm_base.api.v1.serializers.farm import FarmFilterSerializer
from farm_base.models import Farm


class FarmListCreateView(generics.ListCreateAPIView):
    queryset = Farm.objects.filter(is_active=True)
    serializer_class = FarmListSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FarmListSerializer
        else:
            return FarmCreateSerializer

    def perform_create(self, serializer):
        farm = serializer.save()
        area = float(farm.geometry.area)
        centroid = farm.geometry.centroid
        serializer.save(area=area, centroid=centroid)

class FarmSearchView(generics.ListCreateAPIView):
    queryset = Farm.objects.filter()
    serializer_class = FarmFilterSerializer
    filter_backends = (DjangoFilterBackend,
                    filters.OrderingFilter)
    filterset_class = FarmFilter
    search_fields = ['name', 'id']

# class OwnerListCreateView(generics.ListCreateAPIView):
#     queryset = Owner.objects.filter(is_active=True)
#     serializer_class = OwnerListCreateSerializer
#     filter_backends = (DjangoFilterBackend,
#                        filters.OrderingFilter)
#     filterset_class = OwnerFilter
#     search_fields = ['name', 'document']


class FarmRetrieveUpdateDestroyView(
    generics.RetrieveUpdateDestroyAPIView):
    queryset = Farm.objects.filter(is_active=True)
    serializer_class = FarmDetailSerializer
