from django.conf.urls import patterns, include, url
from apps.map import views
from apps.map import models
from haystack.views import basic_search

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^campus/$', views.CampusListView.as_view(model=models.Campus), name='campus_lview'),
    url(r'^campus/(?P<pk>\d+)/$', views.CampusDetailView.as_view(), name='campus_dview'),
#    url(r'^building/$', views.BuildingListView.as_view(model=models.Building), name='building_lview'),
    url(r'^building/(?P<pk>\d+)/$', views.BuildingDetailView.as_view(), name='building_dview'),
    url(r'^gainesville$', views.CampusGainesvilleView.as_view(), name="gainesville"),
    url(r'^oconee$', views.CampusOconeeView.as_view(), name='occonee'),
    url(r'^cumming$', views.CampusCummingView.as_view(), name='cumming'),
    url(r'^dahlonega$', views.CampusDahlonegaView.as_view(), name='dahlonega'),
    url(r'^aboutus$', views.AboutusView.as_view(), name= 'aboutus'),
    url(r'^directories$', views.DirectoriesView.as_view(), name='directories'),
#    url(r'search$', name=basic_search(template='search.html')),
)