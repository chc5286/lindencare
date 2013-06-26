from django.conf.urls import patterns, include, url
from django.views.generic import ListView

from .views import TaskListView

urlpatterns = patterns('',
    url(r'^$',TaskListView.as_view(),name='tasks'),
)
