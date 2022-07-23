from django.urls import  path
from .views import indexclass, GetAllCourses, list_high_price

app_name = 'Courses'  # url namespace
urlpatterns = [
    path('', indexclass.as_view(), name='index'),
    path('GetCourses/', GetAllCourses.as_view(), name='GetCourses'),
    path('high_price/', list_high_price, name='high_price'),
]