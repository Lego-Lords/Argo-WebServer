from django.conf.urls import patterns, include, url
import settings
from argo_app.views import getDataFromServer, getModelFromApp

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'argo_project.views.home', name='home'),
    # url(r'^argo_project/', include('argo_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^argo_app/', include('argo_app.urls')),
    url(r'^value/$', getDataFromServer),
    url(r'^model-id/$', getModelFromApp),
    url(r'^admin/', include(admin.site.urls)),
)
