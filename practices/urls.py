from django.conf.urls import patterns, include, url
from django.views.generic import ListView

from .views import PracticesListView, PracticeDoctorListView

urlpatterns = patterns('',
    url(r'^$',PracticesListView.as_view(),name='practices'),
    url(r'(?P<pk>\d+)/doctors/',PracticeDoctorListView.as_view(),name='practices.doctors')

)
