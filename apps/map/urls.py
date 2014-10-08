from django.conf.urls import patterns, include, url
from apps.map import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^gainesville$', views.CampusGainesvilleView.as_view()),
    url(r'^oconee$', views.CampusOconeeView.as_view()),
    url(r'^cumming$', views.CampusCummingView.as_view()),
    url(r'^dahlonega$', views.CampusDahlonegaView.as_view()),
    url(r'^aboutus$', views.AboutusView.as_view()),
    url(r'^directories$', views.DirectoriesView.as_view()),
)