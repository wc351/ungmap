from haystack import indexes
from .models import Campus, Building, Office, Faculty, Recreation, Classrooms, ParkingLots


class CampusIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Campus

    def index_queryset(self, using=None):
        return self.get_model().objects.filter()


class BuildingIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Building

    def index_queryset(self, using=None):
        return self.get_model().objects.filter()


class FacultyIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Faculty

    def index_queryset(self, using=None):
        return self.get_model().objects.filter()


class ParkinglotIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return ParkingLots

    def index_queryset(self, using=None):
        return self.get_model().objects.filter()


#class RecreationIndex(indexes.SearchIndex, indexes.Indexable):
#    text = indexes.CharField(document=True, use_template=True)
#
#    def get_model(self):
#        return Recreation
#
#    def index_queryset(self, using=None):
#        return self.get_model().objects.filter()


#class ClassroomIndex(indexes.SearchIndex, indexes.Indexable):
#    text = indexes.CharField(document=True, use_template=True)
#
#    def get_model(self):
#        return Classrooms

#    def index_queryset(self, using=None):
#        return self.get_model().objects.filter()


#class OfficeIndex(indexes.SearchIndex, indexes.Indexable):
#    text = indexes.CharField(document=True, use_template=True)
#
#    def get_model(self):
#        return Office
#
#    def index_queryset(self, using=None):
#        return self.get_model().objects.filter()