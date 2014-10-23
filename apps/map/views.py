from django.views import generic
from apps.map import models


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


class CampusGainesvilleView(generic.TemplateView):
    """Loads Gainesville Campus"""
    template_name = 'map/gainesville.html'


class CampusOconeeView(generic.TemplateView):
    """Loads Gainesville Campus"""
    template_name = 'map/oconee.html'


class CampusCummingView(generic.TemplateView):
    """Loads Gainesville Campus"""
    template_name = 'map/cumming.html'


class CampusDahlonegaView(generic.TemplateView):
    """Loads Gainesville Campus"""
    template_name = 'map/dahlonega.html'


class AboutusView(generic.TemplateView):
    """Loads Gainesville Campus"""
    template_name = 'map/aboutus.html'


class DirectoriesView(generic.TemplateView):
    """Loads Gainesville Campus"""
    template_name = 'map/directories.html'