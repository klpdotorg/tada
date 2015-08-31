from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets

from schools.filters import (
    BoundaryFilter, ProgrammeFilter, AssessmentFilter,
    InstitutionFilter,
)
from schools.serializers import (
    InstitutionSerializer, AssessmentSerializer, ProgrammeSerializer,
    BoundarySerializer
)
from schools.models import (
    Institution, AssessmentInstitution, ProgrammeInstitution,
    Boundary
)


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    filter_class = InstitutionFilter


class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = AssessmentInstitution.objects.all()
    serializer_class = AssessmentSerializer
    filter_class = AssessmentFilter


class ProgrammeViewSet(viewsets.ModelViewSet):
    queryset = ProgrammeInstitution.objects.all()
    serializer_class = ProgrammeSerializer
    filter_class = ProgrammeFilter


class BoundaryViewSet(viewsets.ModelViewSet):
    queryset = Boundary.objects.all()
    serializer_class = BoundarySerializer
    filter_class = BoundaryFilter
