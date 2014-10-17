from rest_framework_gis import serializers
from apps.map import models


class CampusSerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        model = models.Campus
        geo_field = 'geom'
        fields = ('id', 'name', 'location')


class BuildingSerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        model = models.Building
        geo_field = 'geom'
        field = ('id', 'name', 'desc', 'build_num')


class FacultySerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        model = models.Faculty
        geo_field = 'geom'
        field = ('id', 'name', 'title', 'campus', 'building', 'office_num', 'phone_num', 'email', 'primary_campus',
                 'department')


class RecreationSerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        model = models.Recreation
        geo_field = 'geom'
        field = ('id', 'name', 'campus')


class ClassroomSerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        model = models.Classrooms
        geo_field = 'geom'
        field = ('id', 'name', 'campus', 'num', 'building')


class ParkinglotSerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        model = models.ParkingLots
        geo_field = 'geom'
        field = ('id', 'lot_name', 'campus', 'desc')