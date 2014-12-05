from django.views import generic
from apps.map import models
from django.db.models import Q


class MainView(generic.TemplateView):
    template_name = "map/main_page.html"


class CampusListView(generic.ListView):
    model = models.Campus
    template_name = "map/campus_list.html"


class CampusDetailView(generic.TemplateView):
    template_name = "map/campus_detail.html"

    def get_context_data(self, **kwargs):
        """Adding images to context"""
        context = super(CampusDetailView, self).get_context_data()
        data = models.Campus.objects.filter(pk=kwargs['pk']).first()
        context['campus'] = data
        return context


class BuildingListView(generic.TemplateView):
    template_name = "map/building_list.html"

    def get_context_data(self, **kwargs):
        context = super(BuildingListView, self).get_context_data()
        data = models.Building.objects.filter(campus=kwargs['campus'])
        context['buildings'] = data
        return context


class BuildingDetailView(generic.DetailView):
    model = models.Building
    template_name = "map/building_detail.html"
    context_object_name = 'building'


class IndividualBuildingMapView(generic.TemplateView):
    template_name = 'map/individual_building_map.html'

    def get_context_data(self, **kwargs):
        context = super(IndividualBuildingMapView, self).get_context_data(**kwargs)
        building = models.Building.objects.filter(pk=kwargs['pk']).first()
        context['building'] = building
        return context


class ParkingLotListView(generic.TemplateView):
    template_name = "map/parkinglots_list.html"

    def get_context_data(self, **kwargs):
        context = super(ParkingLotListView, self).get_context_data()
        data = models.ParkingLots.objects.filter(campus=kwargs['campus'])
        context['parkinglots'] = data
        return context


class ParkingLotDetailView(generic.DetailView):
    model = models.ParkingLots
    template_name = "map/parkinglots_detail.html"
    context_object_name = 'parkinglot'


class IndividualParkinglotMapView(generic.TemplateView):
    template_name = 'map/individual_parkinglot_map.html'

    def get_context_data(self, **kwargs):
        context = super(IndividualParkinglotMapView, self).get_context_data(**kwargs)
        parkinglot = models.ParkingLots.objects.filter(pk=kwargs['pk']).first()
        context['parkinglot'] = parkinglot
        return context


class FacultyListView(generic.TemplateView):
    template_name = "map/faculty_list.html"

    def get_context_data(self, **kwargs):
        context = super(FacultyListView, self).get_context_data()
        data = models.Faculty.objects.filter(campus=kwargs['campus'])
        context['faculty'] = data
        return context


class FacultyDetailView(generic.DetailView):
    model = models.Faculty
    template_name = "map/faculty_detail.html"
    context_object_name = 'faculty'


class IndividualFacultyMapView(generic.TemplateView):
    template_name = 'map/individual_teacher_map.html'

    def get_context_data(self, **kwargs):
        context = super(IndividualFacultyMapView, self).get_context_data(**kwargs)
        faculty = models.Faculty.objects.filter(pk=kwargs['pk']).first()
        context['faculty'] = faculty
        return context


class AboutusView(generic.TemplateView):
    """Loads Gainesville Campus"""
    template_name = 'map/aboutus.html'


class DirectoriesView(generic.TemplateView):
    """Loads Gainesville Campus"""
    template_name = 'map/directories.html'
