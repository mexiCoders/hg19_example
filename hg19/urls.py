from django.conf.urls import patterns, url, include

from hg19 import views

urlpatterns = patterns('',
    url(r'^search/$', views.search, name='search'),
    url(r'^lalignment/$', views.local_alignment, name='local_alignment'),
)
