from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from schools.serializers import (
    StudentSerializer,
)

from schools.models import (
    Student, 
)

''' Returns the details of a student by student id (pk passed in via REST) '''
class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer

    def get_object(self):
        return Student.objects.get(id=self.kwargs['pk'])

''' Returns the list of students. Paginates by 10. Set this globally in settings?'''
class StudentsListView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        query_set=Student.objects.all()
        return query_set

