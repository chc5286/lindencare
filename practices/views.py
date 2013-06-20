from django.views.generic import ListView, CreateView
from django.shortcuts import get_object_or_404

from .models import Practice, Doctor, Category


class PracticesListView(ListView):
    model = Practice
    context_object_name = 'practices'


class PracticeDoctorListView(ListView):
    model = Doctor
    context_object_name = 'doctors'

    def get_queryset(self):
        self.practice = get_object_or_404(Practice,pk=self.kwargs["pk"])
        return Doctor.objects.filter(practice=self.practice)


class PracticeListViewSearch(PracticesListView):

    def get_queryset(self):
        queryset = super(PracticeListViewSearch,self).get_queryset()

        q = self.request.get("search_practice")
        if q:
            return queryset.filter(practice__icontains=q)
        return queryset

class CategoryCreateView(CreateView):
    model = Category