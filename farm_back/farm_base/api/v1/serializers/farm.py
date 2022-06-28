from django.contrib.gis.geos import GEOSGeometry
from osgeo import ogr
from rest_framework import serializers
from rest_framework_gis.fields import GeometryField

from farm_base.api.v1.serializers.owner import OwnerDetailSerializer
from farm_base.models import Farm


class FarmListSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(FarmListSerializer, self).__init__(*args, **kwargs)
        request = kwargs['context']['request']
        include_geometry = request.GET.get('include_geometry', "false")

        if include_geometry.lower() == "true":
            self.fields['geometry'] = GeometryField(read_only=True)

    class Meta:
        model = Farm
        fields = ['name', 'owner', 'centroid', 'area', 
        'municipality', 'state' ]
        read_only_fields = ['id', 'centroid', 'area', 'state']


class FarmCreateSerializer(serializers.ModelSerializer):
    def validate_geometry(self, data):
        if data.hasz:
            g = ogr.CreateGeometryFromWkt(data.wkt)
            g.Set3D(False)
            data = GEOSGeometry(g.ExportToWkt())
        return data

    class Meta:
        model = Farm
        fields = ['id', 'name', 'geometry', 'municipality',
         'centroid', 'state','area', 'owner']
        extra_kwargs = {
            'owner': {'required': True}, 
            'geometry': {'required': True},
            'municipality': {'required': True},
            'state': {'required': True},
            'name': {'required': True},
        }
        read_only_fields = ['id', 'centroid', 'area']


class FarmFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = ['name', 'owner.name', 'owner.document', 
        'municipality', 'state', 'id']
    

class FarmDetailSerializer(serializers.ModelSerializer):
    owner = OwnerDetailSerializer(read_only=True)

    class Meta:
        model = Farm
        fields = ['id', 'name', 'geometry', 'area', 
        'centroid', 'owner', 'creation_date', 'municipality', 
        'state', 'last_modification_date', 'is_active', 
        'owner']
        read_only_fields = ['id', 'centroid', 'area']
