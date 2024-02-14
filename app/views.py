from django.shortcuts import render

# Create your views here.

from app.models import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class SchoolList(ListView):
    model = School
    context_object_name = 'schools'

class SchoolDetail(DetailView):
    model = School
    context_object_name = 'schoolobject'

class SchoolCreate(CreateView):
    model = School
    fields = '__all__'

class SchoolUpdate(UpdateView):
    model = School
    fields = '__all__'

class SchoolDelete(DeleteView):
    model =School
    context_object_name = 'schoolobject'
    success_url = reverse_lazy('SchoolList')
