import json
from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Course
from .serializers import CourseSerializer

# Create your views here.

@api_view(['GET'])
def index(request):
    courses = Course.objects.filter(demo=False)
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def demo(request):
    courses = Course.objects.filter(demo=True)
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def course(request, id):
    course = get_object_or_404(Course, id=id)
    serializer = CourseSerializer(course)
    return Response(serializer.data)