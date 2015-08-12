from rest_framework import generics,viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from schools.serializers import (
    StudentSerializer,
)

from schools.models import (
    Student, 
)

''' Returns the list of students. Paginates by 10. Set this globally in settings?'''
class StudentsListViewSet(viewsets.ModelViewSet):
    query_set=Student.objects.all()
    serializer_class = StudentSerializer

