from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from .models import Practice, Doctor


class PracticesListView(ListView):
    model = Practice
    context_object_name = 'practices'


class PracticeDoctorListView(ListView):
    model = Doctor
    context_object_name = 'doctors'

    def get_queryset(self):
        self.practice = get_object_or_404(Practice,pk=self.kwargs["pk"])
        return Doctor.objects.filter(practice=self.practice)
