from rest_framework import generics
from rest_framework.views import APIView

from .serializers import (
    InstitutionSerializer, StudentSerializer
)

from .models import (
    Institution, Student, 
)


class InstitutionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InstitutionSerializer

    def get_object(self):
        return Institution.objects.get(id=self.kwargs['pk'])

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer

    def get_object(self):
        return Student.objects.get(id=self.kwargs['pk'])
