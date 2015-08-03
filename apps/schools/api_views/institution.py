from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets

from schools.serializers import (
    InstitutionSerializer, AssessmentSerializer,
)
from schools.models import (
    Institution, AssessmentInstitution,
)

class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer

class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = AssessmentInstitution.objects.all()
    serializer_class = AssessmentSerializer
