from django.views.generic import ListView, CreateView
from django.shortcuts import get_object_or_404

from .models import Practice, Doctor, Category


class PracticesListView(ListView):

    model = Practice
    context_object_name = 'practices'
"""
    def get_context_data(self,**kwargs):
        context = super(PracticesListView,self).get_context_data(**kwargs)
        for practice in context['practices']:
            context['sums'][practice.id] = Practice.objects.filter(pk=practice.id).filter(doctors__scripts).count()
        return context
"""




class PracticeDoctorListView(ListView):
    model = Doctor
    context_object_name = 'doctors'

    def get_queryset(self):
        self.practice = get_object_or_404(Practice,pk=self.kwargs["pk"])
        return Doctor.objects.filter(practice=self.practice)


