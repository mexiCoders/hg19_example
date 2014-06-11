from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'hg19.views.index', name='index'),
    url(r'^hg19/', include('hg19.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
