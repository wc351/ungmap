from rest_framework import mixins
from rest_framework import generics
from apps.map import models, serializers
import django_filters


class IntegerListFilter(django_filters.Filter):
    def filter(self, qs, value):
        if value not in (None, ''):
            integers = [int(v) for v in value.split(',')]
            return qs.filter(**{'{}__{}'.format(self.name, self.lookup_type):integers})
        return qs


class CampusFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Campus
        fields = ['id', 'name', 'location']


class BuildingFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Building
        fields = ['id', 'name', 'alter_name', 'desc', 'build_num']


class FacultyFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')
    campus = IntegerListFilter(name='campus', lookup_type='in')

    class Meta:
        model = models.Faculty
        fields = ['id', 'name', 'title', 'campus', 'building', 'office_num', 'phone_num', 'email', 'department']


class RecreationFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Recreation
        fields = ['id', 'name', 'campus']


class ClassroomFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Classrooms
        fields = ['id', 'name', 'campus', 'num', 'building']


class ParkinglotFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.ParkingLots
        fields = ['id', 'lot_name', 'campus', 'desc']


class ParkingSpotsFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.ParkingSpots
        fields = ['id', 'spot_type', 'campus']


class ParkingLotLinesFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.ParkingLotLines
        fields = ['id', 'name', 'campus']


class CallBoxFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.CallBoxes
        fields = ['id', 'name', 'campus']


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


class ParkingSpotCollection(generics.ListAPIView):
    queryset = models.ParkingSpots.objects.all()
    serializer_class = serializers.ParkingSpotSerializer
    filter_class = ParkingSpotsFilter


class ParkingLotLinesCollection(generics.ListAPIView):
    queryset = models.ParkingLotLines.objects.all()
    serializer_class = serializers.ParkingLotLinesSerializer
    filter_class = ParkingLotLinesFilter


class CallBoxCollection(generics.ListAPIView):
    queryset = models.CallBoxes.objects.all()
    serializer_class = serializers.CallBoxSerializer
    filter_class = CallBoxFilter
