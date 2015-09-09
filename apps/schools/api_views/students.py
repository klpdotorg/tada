from rest_framework import generics,viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from schools.filters import (
    StudentFilter
)
from schools.serializers import (
    StudentSerializer,
)
from schools.models import (
    Student, 
)

''' Returns the list of students. Paginates by 10. Set this globally in settings?'''
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_class = StudentFilter
