from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.views import MainView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', MainView.as_view(), name='main_page'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
