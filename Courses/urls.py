from django.urls import  path
from .views import indexclass, GetAllCourses

app_name = 'Courses'  # url namespace
urlpatterns = [
    path('', indexclass.as_view(), name='index'),
    path('GetCourses/', GetAllCourses.as_view(), name='GetCourses'),
]