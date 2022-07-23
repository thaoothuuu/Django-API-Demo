from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GetAllCoursesSerializer, CoursesSerializer
from .models import Courses
# Create your views here.
from .services.services import CoursesService
from django.http import JsonResponse


class indexclass(View):
    def get(self, request):
        self.name = 'Stella'
        context = {
            'n': self.name
        }
        return render(request, template_name='Courses/index.html', context=context)



class GetAllCourses(APIView):
    def get(self, request):
        list_courses = Courses.objects.all()
        mydata = GetAllCoursesSerializer(list_courses, many=True)
        # list_courses = Courses.object.get(id=1)
        # mydata = GetAllCoursesSerializer(list_courses)
        return Response(data=mydata.data, status=status.HTTP_200_OK)


    def post(self, request):
        mydata = CoursesSerializer(data=request.data)
        if not mydata.is_valid():
            return Response('Dữ liệu sai', status=status.HTTP_400_BAD_REQUEST)
        else:
            title1 = mydata.data['title1']
            price1 = mydata.data['price1']
            content1 = mydata.data['content1']
            cs = Courses.objects.create(title=title1, price=price1, content=content1)
            return Response(data=cs.id, status=status.HTTP_200_OK)





def list_high_price(request):
    courses = Courses.objects.all()
    data = []
    for c in courses:
        if CoursesService.is_high_price(c.price):
            data.append(c.to_json())

    return JsonResponse({'data': data})

