from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = "main_page.html"