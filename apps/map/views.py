from django.views import generic


class MainView(generic.TemplateView):
    template_name = "map/main_page.html"

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