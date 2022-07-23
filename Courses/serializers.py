from rest_framework import serializers
from .models import Courses

class GetAllCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ('id', 'title', 'price',)


class CoursesSerializer(serializers.Serializer):
    title1 = serializers.CharField(max_length=12)
    price1 = serializers.IntegerField(default=0)
    content1 = serializers.CharField(max_length=12)
