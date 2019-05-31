from django.shortcuts import render
from .models import Course, Faculty
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404, render

from django.urls import reverse
from django.views import generic

# Create your views here.

class DetailView(generic.DetailView):
    model = Course
    template_name = 'school/course_detail.html'

class CourseListView(generic.ListView):
    model = Course

    def get_queryset(self):
        return Course.objects.all()

class FacultyListView(generic.ListView):
    model = Faculty

    def get_queryset(self):
        return Faculty.objects.all()

class CourseDetailView(generic.DetailView):
    model = Course


class FacultyDetailView(generic.DetailView):
    model = Faculty
