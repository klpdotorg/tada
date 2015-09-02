from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets

from schools.api_filters import BoundaryFilter
from schools.serializers import (
    InstitutionSerializer, AssessmentSerializer, ProgrammeSerializer,
    BoundarySerializer, StaffSerializer
)
from schools.models import (
    Institution, AssessmentInstitution, ProgrammeInstitution,
    Boundary, Staff
)


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = AssessmentInstitution.objects.all()
    serializer_class = AssessmentSerializer


class ProgrammeViewSet(viewsets.ModelViewSet):
    queryset = ProgrammeInstitution.objects.all()
    serializer_class = ProgrammeSerializer


class BoundaryViewSet(viewsets.ModelViewSet):
    queryset = Boundary.objects.all()
    serializer_class = BoundarySerializer
    filter_class = BoundaryFilter

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class=StaffSerializer

