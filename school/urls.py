from django.urls import path

from . import views


app_name = 'school'
urlpatterns = [
    path('course/', views.CourseListView.as_view(), name='course'),
    path('faculty/', views.FacultyListView.as_view(), name='faculty'),
    path('course/<int:pk>', views.CourseDetailView.as_view(), name='course-detail'),
    path('faculty/<int:pk>', views.FacultyDetailView.as_view(), name='faculty-detail'),

]