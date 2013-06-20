from django.conf.urls import patterns, include, url
from django.views.generic import ListView

from .views import PracticesListView, PracticeDoctorListView, CategoryCreateView

urlpatterns = patterns('',
    url(r'^$',PracticesListView.as_view(),name='practices'),
    url(r'(?P<pk>\d+)/doctors/',PracticeDoctorListView.as_view(),name='practices.doctors'),
    #url(r'search_practice/',PracticeListViewSearch.as_view(),name='search_practice'),
    #url(r'add_category$',CategoryCreateView.as_view(),name='add_category')
)
