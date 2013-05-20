from django.conf.urls.defaults import patterns, include, url
from .views import hello

urlpatterns = patterns('',
    url(r'^hello/$', hello),
)
