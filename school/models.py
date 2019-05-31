import datetime
from django.db import models
from django.utils import timezone


class Faculty(models.Model):
    name = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=20)
    rank = models.CharField(max_length=20, choices=[('Instructor', 'Instructor'), ('Part_Time', 'Part_Time'),('Professor', 'Professor')])

    def __str__(self):
        return self.name

class Course(models.Model):
    course_id = models.CharField(max_length=9)
    course_name = models.CharField(max_length=30)
    start_date = models.DateTimeField('date started')
    end_date = models.DateTimeField('date ended')
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE,related_name='courses')
    def __str__(self):
        return self.course_id


