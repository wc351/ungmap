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
        fields = ('id', 'name', 'alter_name', 'desc', 'build_num')


class FacultySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Faculty
        fields = ('id', 'name', 'alter_name' 'title', 'campus', 'building', 'office_num', 'phone_num', 'email', 'department')


class RecreationSerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        model = models.Recreation
        geo_field = 'geom'
        fields = ('id', 'name', 'campus')


class ClassroomSerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        model = models.Classrooms
        geo_field = 'geom'
        fields = ('id', 'name', 'campus', 'num', 'building')


class ParkinglotSerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        model = models.ParkingLots
        geo_field = 'geom'
        fields = ('id', 'lot_name', 'campus', 'desc')


class ParkingSpotSerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        model = models.ParkingSpots
        geo_field = 'geom'
        fields = ('id', 'spot_type', 'campus')


class ParkingLotLinesSerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        model = models.ParkingLotLines
        geo_field = 'geom'
        fields = ('id', 'name', 'campus')


class CallBoxSerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        model = models.CallBoxes
        geo_field = 'geom'
        fields = ('id', 'name', 'campus')