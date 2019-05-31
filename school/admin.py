from django.contrib import admin

# Register your models here.
from .models import Course, Faculty

admin.site.register(Course)
admin.site.register(Faculty)