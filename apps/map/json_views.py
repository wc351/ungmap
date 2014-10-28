
from rest_framework import mixins
from rest_framework import generics
from apps.map import models, serializers
import django_filters


class CampusFilter(django_filters.Filter):

    class Meta:
        model = models.Campus
        fields = ['id', 'name', 'location']


class BuildingFilter(django_filters.Filter):

    class Meta:
        model = models.Building
        field = ['id', 'name', 'desc', 'build_num']


class FacultyFilter(django_filters.Filter):

    class Meta:
        model = models.Faculty
        field = ['id', 'name', 'title', 'campus', 'building', 'office_num', 'phone_num', 'email', 'primary_campus',
                 'department']


class RecreationFilter(django_filters.Filter):

    class Meta:
        model = models.Recreation
        field = ['id', 'name', 'campus']


class ClassroomFilter(django_filters.Filter):

    class Meta:
        model = models.Classrooms
        field = ['id', 'name', 'campus', 'num', 'building']


class ParkinglotFilter(django_filters.Filter):

    class Meta:
        model = models.ParkingLots
        field = ['id', 'lot_name', 'campus', 'desc']


class CampusCollection(generics.ListAPIView):
    queryset = models.Campus.objects.all()
    serializer_class = serializers.CampusSerializer
    filter_class = CampusFilter


class BuildingCollection(generics.ListAPIView):
    queryset = models.Building.objects.all()
    serializer_class = serializers.BuildingSerializer
    filter_class = BuildingFilter


class FacultyCollection(generics.ListAPIView):
    queryset = models.Faculty.objects.all()
    serializer_class = serializers.FacultySerializer
    filter_class = FacultyFilter


class RecreationCollection(generics.ListAPIView):
    queryset = models.Recreation.objects.all()
    serializer_class = serializers.RecreationSerializer
    filter_class = RecreationFilter


class ClassroomCollection(generics.ListAPIView):
    queryset = models.Classrooms.objects.all()
    serializer_class = serializers.ClassroomSerializer
    filter_class = ClassroomFilter


class ParkinglotCollection(generics.ListAPIView):
    queryset = models.ParkingLots.objects.all()
    serializer_class = serializers.ParkinglotSerializer
    filter_class = ParkinglotFilter