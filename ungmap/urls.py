from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.map.views import MainView

admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    url(r'^$', MainView.as_view(), name='main_page'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('apps.map.urls', namespace='map')),
    url(r'^api/v1/', include('apps.map.api_urls', namespace='ungmap_api')),
    url(r'^search/', include('haystack.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),

)
