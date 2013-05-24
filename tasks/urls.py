from django.conf.urls import patterns, url

from tasks import views

urlpatterns = patterns('',
   url(r'^tasks',views.task_list,name='tasks')
)
